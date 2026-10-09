#!/usr/bin/env python3
"""Check built page content, crawl paths, form contracts and SEO integrity."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / 'dist'
class Document(HTMLParser):
    def __init__(self):
        super().__init__(); self.tags=[]; self.text=[]; self.ids=set(); self.refs=[]; self.in_main=False; self.main_text=[]; self.ld=[]; self.in_ld=False
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); self.tags.append((tag,a))
        if a.get('id'): self.ids.add(a['id'])
        if tag=='main': self.in_main=True
        if tag=='script' and a.get('type')=='application/ld+json': self.in_ld=True
        for name in ('href','src','action'):
            if name in a: self.refs.append(a[name])
    def handle_endtag(self,tag):
        if tag=='main': self.in_main=False
        if tag=='script': self.in_ld=False
    def handle_data(self,data):
        self.text.append(data)
        if self.in_main: self.main_text.append(data)
        if self.in_ld: self.ld.append(data)

pages={}; titles=set(); descriptions=set()
for file in ROOT.rglob('*.html'):
    path='/'+str(file.relative_to(ROOT)).replace('index.html','')
    d=Document(); raw=file.read_text(); d.feed(raw); pages[path]=d
    assert '<html lang="en-GB">' in raw,file
    assert sum(t=='h1' for t,a in d.tags)==1, f'One h1 required: {file}'
    title=re.search(r'<title>(.*?)</title>',raw).group(1)
    assert title not in titles, f'Duplicate title: {title}'
    titles.add(title)
    desc=next(a['content'] for t,a in d.tags if t=='meta' and a.get('name')=='description')
    assert desc and desc not in descriptions, f'Duplicate/empty description: {file}'
    descriptions.add(desc)
    canonical=next(a['href'] for t,a in d.tags if t=='link' and a.get('rel')=='canonical')
    assert canonical.startswith('https://fencingmerseyside.co.uk/'),file
    for ld in d.ld: json.loads(ld)
    for t,a in d.tags:
        if t=='img': assert all(a.get(k) for k in ('alt','width','height')),f'Image attributes: {file}'
        if t=='form': assert a.get('method')=='POST' and a.get('action')=='https://formsubmit.co/hello@fencingmerseyside.co.uk',file
        if t=='label': assert a.get('for') in d.ids,f'Unbound label: {file}'
    for ref in d.refs:
        parts=urlsplit(ref)
        if parts.scheme or parts.netloc: continue
        target=ROOT/unquote(parts.path).lstrip('/') if parts.path else file
        if target.is_dir(): target=target/'index.html'
        assert target.exists(),f'Broken local reference {ref} in {file}'
        if parts.fragment:
            td=Document();td.feed(target.read_text())
            assert parts.fragment in td.ids, f'Broken fragment {ref} in {file}'

words=len(re.findall(r"\b[\w’-]+\b",' '.join(pages['/'].main_text)))
assert words>=1000,f'Homepage only {words} words'
print(f'PASS: homepage has {words} visible main-content words')
urls=[e.text for e in ET.parse(ROOT/'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls)==len(set(urls)), 'Duplicate sitemap entries'
map_refs=set(pages['/sitemap/'].refs)
for url in urls:
    path=urlsplit(url).path
    assert path in pages,f'Sitemap points to missing page: {path}'
    assert path in map_refs or path=='/sitemap/',f'Page missing from HTML sitemap: {path}'
assert 'Sitemap: https://fencingmerseyside.co.uk/sitemap.xml' in (ROOT/'robots.txt').read_text()
assert not any('/enquiry-received/' in u for u in urls)
print(f'PASS: {len(pages)} HTML pages; unique metadata, structured data, local links, images and labelled form contracts')
print(f'PASS: {len(urls)} indexable sitemap URLs, HTML sitemap and robots.txt')
