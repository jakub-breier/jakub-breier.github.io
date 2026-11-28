"""Validate SEO output and CV links before Pages deployment."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import json
import xml.etree.ElementTree as ET

ROOT = Path("_site")
BASE = "https://jbreier.com"
PAGES = ("", "research/", "publications/", "teaching/", "service/", "talks/", "cv/")


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.meta = {}
        self.links = []
        self.schemas = []
        self.title = ""
        self.in_title = False
        self.in_schema = False
        self.buffer = ""
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta":
            self.meta[a.get("name") or a.get("property")] = a.get("content", "")
        if tag in ("a", "link", "script", "div"):
            self.links.append((tag, a))
        if tag == "title":
            self.in_title = True
        if tag == "script" and a.get("type") == "application/ld+json":
            self.in_schema = True
            self.buffer = ""

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_schema:
            self.buffer += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag == "script" and self.in_schema:
            self.schemas.append(json.loads(self.buffer))
            self.in_schema = False


descriptions = set()
titles = set()
for route in PAGES:
    page = Page((ROOT / route / "index.html").read_text(encoding="utf-8"))
    expected = BASE + "/" + route
    assert page.title.strip() and page.title not in titles, (route, "missing/duplicate title")
    titles.add(page.title)
    description = page.meta.get("description", "").strip()
    assert description and description not in descriptions, (route, "missing/duplicate description")
    descriptions.add(description)
    assert page.meta.get("og:url") == expected, (route, "og:url")
    assert page.meta.get("og:title") == page.title, (route, "og:title")
    assert page.meta.get("og:description") == description, (route, "og:description")
    assert page.meta.get("twitter:card") == "summary", (route, "social card")
    canonical = [a.get("href") for t, a in page.links if t == "link" and a.get("rel") == "canonical"]
    assert canonical == [expected], (route, "canonical URL", canonical)
    image = urlsplit(page.meta.get("og:image", ""))
    assert image.scheme == "https" and image.netloc == "jbreier.com" and (ROOT / image.path.lstrip("/")).is_file(), (route, "missing social image")
    graph = next(s["@graph"] for s in page.schemas if "@graph" in s)
    person = next(x for x in graph if x["@type"] == "Person")
    assert person["name"] == "Jakub Breier" and len(person["sameAs"]) >= 4, (route, "person identity")
    if not route:
        profile = next(x for x in graph if x["@type"] == "ProfilePage")
        assert profile["mainEntity"]["@id"] == person["@id"], "profile identity mismatch"
    if route == "cv/":
        preview = next(a for t, a in page.links if t == "div" and a.get("id") == "cv-preview")
        pdf = preview["data-pdf"]
        assert (ROOT / urlsplit(pdf).path.lstrip("/")).is_file(), "missing CV PDF"
        assert any(t == "a" and a.get("href") == pdf and "download" in a for t, a in page.links), "download link missing"
        assert any(t == "a" and a.get("href") == pdf and a.get("target") == "_blank" for t, a in page.links), "open link missing"
        assert (ROOT / "assets/js/cv-viewer.js").is_file(), "CV viewer script missing"
    print("OK:", expected)

sitemap = ET.parse(ROOT / "sitemap.xml")
urls = {el.text for el in sitemap.getroot().iter() if el.tag.endswith("}loc")}
assert {BASE + "/" + route for route in PAGES} <= urls, "Main pages missing from sitemap"
assert BASE + "/sitemap.xml" in (ROOT / "robots.txt").read_text(), "Sitemap missing from robots.txt"
print("SEO metadata, structured data, sitemap and CV link checks passed.")
