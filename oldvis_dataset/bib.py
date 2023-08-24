"""
Store metadata in BibTeX.
"""

import json
from typing import List, Union

import bibtexparser
from bibtexparser import Library
from bibtexparser.model import Entry, Field
from langcodes import Language


def normalize(text: str) -> str:
    return text.replace("{", "").replace("}", "")


def get_author(d) -> Union[str, None]:
    if d["authors"] is None:
        return None
    return " and ".join(d["authors"])


def get_year(d) -> Union[str, None]:
    if isinstance(d["publishDate"], list):
        return f'{d["publishDate"][0]["year"]}--{d["publishDate"][1]["year"]}'
    if d["publishDate"] is None:
        return None
    return f'{d["publishDate"]["year"]}'


def get_keywords(d) -> Union[str, None]:
    if len(d["tags"]) == 0:
        return None
    return ", ".join(d["tags"])


def get_languages(d) -> Union[str, None]:
    if d["languages"] is None:
        return None
    languages = [Language.get(lang).language_name() for lang in d["languages"]]
    return ", ".join(languages)


def build_fields(d) -> List[Field]:
    fields = [
        Field("url", d["viewUrl"]),
        Field("file", d["downloadUrl"]),
    ]

    if d["displayName"] is not None:
        fields.append(Field("title", d["displayName"]))

    author = get_author(d)
    if author is not None:
        fields.append(Field("author", author))

    year = get_year(d)
    if year is not None:
        fields.append(Field("year", year))

    keywords = get_keywords(d)
    if keywords is not None:
        fields.append(Field("keywords", keywords))

    languages = get_languages(d)
    if languages is not None:
        fields.append(Field("languages", languages))

    if d["abstract"] is not None:
        fields.append(Field("abstract", d["abstract"]))

    for field in fields:
        field.value = normalize(field.value)
    return fields


def save_as_bib(metadata_path: str, bib_path: str) -> None:
    with open(metadata_path, "r", encoding="utf-8") as f:
        visualizations = json.load(f)
    library = Library(
        [
            Entry(entry_type="misc", key=d["uuid"], fields=build_fields(d))
            for d in visualizations
        ]
    )
    with open(bib_path, "w", encoding="utf-8") as f:
        f.write(bibtexparser.write_string(library))
