"""TEI XML parsers for GROBID responses."""
from datetime import datetime
from typing import Any, Dict

from fastapi import HTTPException
from lxml import etree

TEI_NS = {"tei": "http://www.tei-c.org/ns/1.0"}


def parse_xml(xml_text: str):
    """Parse a GROBID XML string into an etree root."""
    try:
        return etree.fromstring(xml_text.encode("utf-8"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to parse GROBID XML response: {str(e)}")


def parse_header_xml(xml_text: str) -> dict:
    """Extract Dublin Core-compatible metadata from GROBID header XML."""
    root = parse_xml(xml_text)

    title = None
    title_xpaths = [
        "//tei:titleStmt/tei:title[@type='main']/text()",
        "//tei:titleStmt/tei:title[not(@type)]/text()",
        "//tei:titleStmt/tei:title/text()",
        "//tei:sourceDesc//tei:title[@level='a']/text()",
        "//tei:analytic/tei:title/text()",
        "//tei:head/text()",
    ]

    for xpath in title_xpaths:
        title_nodes = root.xpath(xpath, namespaces=TEI_NS)
        if title_nodes:
            for value in title_nodes:
                cleaned = value.strip() if value else ""
                if cleaned and len(cleaned) > 3:
                    title = cleaned
                    print(f"GROBID: Found title via {xpath}: {title[:50]}...")
                    break
            if title:
                break

    if not title:
        first_head = root.xpath("//tei:body//tei:head[1]/text()", namespaces=TEI_NS)
        if first_head and first_head[0].strip():
            title = first_head[0].strip()
            print(f"GROBID: Using first heading as title: {title[:50]}...")

    authors = []
    for author in root.xpath("//tei:author/tei:persName", namespaces=TEI_NS):
        forename = "".join(author.xpath("tei:forename/text()", namespaces=TEI_NS)) or ""
        surname = "".join(author.xpath("tei:surname/text()", namespaces=TEI_NS)) or ""
        full_name = f"{forename} {surname}".strip()
        if full_name:
            authors.append(full_name)

    doi_nodes = root.xpath("//tei:idno[@type='DOI']/text()", namespaces=TEI_NS)
    date_nodes = root.xpath("//tei:date[@type='published']/@when", namespaces=TEI_NS)
    if not date_nodes:
        date_nodes = root.xpath("//tei:date/text()", namespaces=TEI_NS)
    publisher_nodes = root.xpath("//tei:publicationStmt/tei:publisher/text()", namespaces=TEI_NS)
    journal_nodes = root.xpath("//tei:sourceDesc//tei:title[@level='j']/text()", namespaces=TEI_NS)
    abstract_nodes = root.xpath("//tei:profileDesc/tei:abstract//text()", namespaces=TEI_NS)
    keyword_nodes = root.xpath("//tei:keywords//tei:term/text()", namespaces=TEI_NS)

    all_idno = root.xpath("//tei:idno/text()", namespaces=TEI_NS)
    identifier = doi_nodes[0] if doi_nodes else (all_idno[0].strip() if all_idno else None)

    rights = None
    license_nodes = root.xpath("//tei:availability/@status", namespaces=TEI_NS)
    if license_nodes:
        rights = license_nodes[0]
    license_text = root.xpath("//tei:availability//tei:licence/@target", namespaces=TEI_NS)
    if license_text:
        rights = license_text[0]
    if not rights:
        license_p = root.xpath("//tei:availability//tei:p/text()", namespaces=TEI_NS)
        if license_p:
            rights = license_p[0].strip()

    print(f"GROBID: Extracted title = '{title}'")
    print(f"GROBID: DOI = {doi_nodes[0] if doi_nodes else None}, identifier = {identifier}, rights = {rights}")

    return {
        "title": title,
        "authors": authors,
        "doi": doi_nodes[0] if doi_nodes else None,
        "identifier": identifier,
        "publication_date": date_nodes[0] if date_nodes else None,
        "publisher": publisher_nodes[0] if publisher_nodes else None,
        "journal": journal_nodes[0] if journal_nodes else None,
        "abstract": " ".join(abstract_nodes).strip() if abstract_nodes else None,
        "keywords": keyword_nodes if keyword_nodes else [],
        "rights": rights,
    }


def format_metadata_for_database(metadata: Dict[str, Any], references: list[str] = None) -> dict:
    """Format extracted GROBID metadata to match the Dublin Core database schema."""
    authors = metadata.get("authors", [])
    keywords = metadata.get("keywords", [])
    references = references or []

    creator = authors[0] if authors else None
    contributor = ", ".join(authors[1:]) if len(authors) > 1 else None

    raw_date = metadata.get("publication_date")
    parsed_date = None
    if raw_date:
        for fmt in ["%Y-%m-%d", "%Y-%m", "%Y", "%d %B %Y", "%B %Y"]:
            try:
                parsed_date = datetime.strptime(raw_date, fmt).date()
                break
            except ValueError:
                continue

    title = metadata.get("title")
    if title:
        title = title.strip()
        if title.lower() in ["untitled", "title", "untitled document", ""]:
            title = None

    identifier = metadata.get("identifier") or metadata.get("doi")

    return {
        "title": title or 'Untitled',
        "creator": creator,
        "keywords": ", ".join(keywords) if keywords else None,
        "description": metadata.get("abstract"),
        "publisher": metadata.get("publisher"),
        "contributor": contributor,
        "date": parsed_date,
        "format": "application/pdf",
        "identifier": identifier,
        "source": metadata.get("journal"),
        "language": "en",
        "relation": ", ".join(references[:10]) if references else None,
        "coverage": metadata.get("coverage"),
        "rights": metadata.get("rights"),
        "doi": metadata.get("doi"),
        "abstract": metadata.get("abstract"),
        "citation_count": len(references),
    }
