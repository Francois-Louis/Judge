"""Relevé technique ponctuel EXIST-007, sans qualification juridique ni configuration.

python -X utf8 backlog/02-plugins-existants/exist-007-sondages.py
Écrit uniquement exist-007-sources.json ; aucun compte ou secret utilisé.
"""

from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CATALOG = ROOT / 'regulatory-legal/skills/reg-feed-watcher/references/source-catalog.md'
LIMIT = 2 * 1024 * 1024
ENDPOINTS = [
    ('cnil_catalog_en', 'https://www.cnil.fr/en/rss.xml'),
    ('cnil_fr_candidate', 'https://www.cnil.fr/fr/rss.xml'),
    ('dila_jorf_listing', 'https://echanges.dila.gouv.fr/OPENDATA/JORF/'),
    ('eurlex_home', 'https://eur-lex.europa.eu/'),
    ('eurlex_webservice_doc', 'https://eur-lex.europa.eu/content/help/data-reuse/webservice.html?locale=en'),
    ('eurlex_rss_doc', 'https://eur-lex.europa.eu/content/help/my-eurlex/my-rss-feeds.html?locale=en'),
    ('edpb_catalog_page', 'https://www.edpb.europa.eu/news/news_en'),
]


def catalog_entries():
    entries, section = [], ''
    for line in CATALOG.read_text(encoding='utf-8').splitlines():
        if line.startswith('## '):
            section = line[3:]
        if not line.startswith('| '):
            continue
        cols = [c.strip() for c in re.split(r'(?<!\\)\|', line)[1:-1]]
        if cols[0] == 'Source' or all(set(c) <= set('-: ') for c in cols):
            continue
        if len(cols) not in (3, 6):
            continue
        row = {'section': section, 'source': cols[0],
               'declared_url_or_method': cols[1], 'declared_notes': cols[-1],
               'verification': 'declaration-heritee-non-certifiee'}
        if len(cols) == 6:
            row.update(declared_format=cols[2], declared_coverage=cols[3], declared_auth=cols[4])
        row['decision'] = (
            'Retirer du parcours France/UE par défaut ; piste étrangère explicitement choisie seulement.'
            if section.startswith('US ') else
            'Conserver comme piste secondaire à remonter vers source primaire, aucun effet juridique déduit.'
            if section.startswith('Secondary') else
            'Conserver comme piste à qualifier par territoire, format, accès et version ; pas de flux fonctionnel présumé.')
        entries.append(row)
    return entries


def probe(pair):
    ident, url = pair
    result = {'id': ident, 'url': url,
              'attempted_at_utc': datetime.now(timezone.utc).isoformat(),
              'authentication': 'aucun compte, cookie ou secret fourni', 'limit_bytes': LIMIT}
    try:
        request = Request(url, headers={
            'User-Agent': 'Judge-EXIST007-source-audit/1.0',
            'Accept': 'application/rss+xml, application/atom+xml, text/html;q=0.8, */*;q=0.5',
        })
        with urlopen(request, timeout=18) as response:
            body = response.read(LIMIT + 1)
            charset = response.headers.get_content_charset() or 'utf-8'
            result.update(http_status=response.status, final_url=response.url,
                          content_type=response.headers.get('Content-Type'),
                          body_bytes_read=len(body), truncated=len(body) > LIMIT,
                          sha256=hashlib.sha256(body).hexdigest())
        text = body.decode(charset, errors='replace')
        result['status'] = 'observed-page'
        if not body:
            result.update(status='empty-response', observed_format='empty')
            return result
        if len(body) > LIMIT:
            result.update(status='size-limit', observed_format='undetermined')
            return result
        try:
            root = ET.fromstring(body)
            tag = root.tag.rsplit('}', 1)[-1]
            result['xml_root'] = tag
            if tag in ('rss', 'feed'):
                result.update(status='observed-feed', observed_format='rss' if tag == 'rss' else 'atom',
                              item_count=len(root.findall('.//item')) if tag == 'rss'
                              else len(root.findall('{http://www.w3.org/2005/Atom}entry')))
            else:
                result['observed_format'] = 'xml-non-feed'
        except ET.ParseError:
            result['observed_format'] = 'html-or-other'
            result['javascript_challenge'] = any(t in text.lower() for t in (
                'verify that you', 'javascript is disabled', 'enable javascript', 'automated access'))
            result['advertised_feed_links'] = re.findall(
                r'<link[^>]+type=["\']application/(?:rss|atom)\+xml["\'][^>]*>', text, re.I)[:6]
            if result['javascript_challenge']:
                result['status'] = 'challenge'
            if ident == 'dila_jorf_listing':
                links = re.findall(r'href="([^"]+\.tar\.gz)"', text)
                result.update(archive_links=len(links), archive_examples=links[-3:])
    except HTTPError as exc:
        result.update(http_status=exc.code, status='http-error')
    except Exception as exc:
        result.update(status='network-error', error_type=type(exc).__name__, error=str(exc)[:250])
    return result


def main():
    entries = catalog_entries()
    with ThreadPoolExecutor(max_workers=4) as pool:
        probes = list(pool.map(probe, ENDPOINTS))
    report = {
        'story': 'EXIST-007', 'date': '2026-10-16', 'timezone': 'Europe/Paris',
        'catalog_path': CATALOG.relative_to(ROOT).as_posix(),
        'catalog_sha256': hashlib.sha256(CATALOG.read_bytes()).hexdigest(),
        'catalog_entries': entries, 'catalog_counts': dict(Counter(e['section'] for e in entries)),
        'technical_probes': probes,
        'indexed_official_documentation': [
            {'url': ENDPOINTS[4][1], 'status': 'contenu officiel indexé lu via recherche web le 16 octobre 2026 ; ouverture directe web : challenge JS',
             'finding': 'SOAP/XML après inscription et autorisation ; recherche de métadonnées, pas téléchargement direct des fichiers ; CELLAR distinct'},
            {'url': ENDPOINTS[5][1], 'status': 'contenu officiel indexé lu via recherche web le 16 octobre 2026 ; ouverture directe web : challenge JS',
             'finding': 'alertes RSS personnalisées avec compte connecté ; aucun accès authentifié local testé'},
        ],
        'limits': ['Sondages techniques ponctuels, aucun abonnement ou compte configuré.',
                   'Aucun texte normatif de scénario consulté ni applicabilité validée.',
                   'Pas de lecture des archives JORF/XML ; répertoire HTML distinct de RSS.',
                   'Les autres lignes restent des déclarations héritées, sans disponibilité certifiée.',
                   'Observations web indexées historiques, non rafraîchies par ce script HTTP.'],
    }
    (HERE / 'exist-007-sources.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print('Catalog rows:', len(entries))
    for item in probes:
        print(item['id'], item['status'], item.get('http_status'), item.get('observed_format'), item.get('item_count'))


if __name__ == '__main__':
    main()
