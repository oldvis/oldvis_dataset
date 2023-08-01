"""
Utility functions to download images from the urls stored in metadata.
"""

import json
import mimetypes
import os
from os import listdir
from os.path import isfile, join
from typing import List, TypedDict

import requests
from tqdm import tqdm


class ImageQuery(TypedDict):
    """
    The data structure of an image query.

    Attributes
    ----------
    url : str
        The url for fetching the image.
    uuid : str
        The UUID of the image.
    """

    url: str
    uuid: str


def filename2uuid(filename: str) -> str:
    return filename.split(".")[0]


def filter_queries(img_queries: List[ImageQuery], img_dir: str) -> List[ImageQuery]:
    """
    Filter URLs queried before according to the stored images.
    """

    filenames = [d for d in listdir(img_dir) if isfile(join(img_dir, d))]
    img_uuids = {filename2uuid(d) for d in filenames}
    return [d for d in img_queries if d["uuid"] not in img_uuids]


def fetch_images(
    metadata_path: str,
    img_dir: str,
) -> None:
    """
    Given base urls, generate image queries, and store the query results.

    Args
    ----
    metadata_path : str
        The path to the metadata file where image urls are stored.
    img_dir : str
        The path to the directory for storing the images.
    """

    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    s = requests.Session()

    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    queries = filter_queries(metadata, img_dir)
    for query in tqdm(queries, desc="Fetch Image Progress"):
        uuid = query["uuid"]
        response = s.get(query["downloadUrl"])
        extension = mimetypes.guess_extension(response.headers["content-type"])
        with open(f"{img_dir}/{uuid}{extension}", "wb") as f:
            f.write(response.content)
