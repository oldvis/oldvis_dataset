import json
from typing import Any

import requests
from requests.exceptions import ConnectionError
from tqdm import tqdm


def download(url: str, path: str) -> None:
    """Download file from URL to path."""

    # The received content length would be
    # the size of compressed file without Accept-Encoding: identity.
    r = requests.head(url, headers={"Accept-Encoding": "identity"}, timeout=20)
    content_length = int(r.headers["Content-Length"])

    r = requests.get(url, stream=True, timeout=20)
    with open(path, "wb") as f, tqdm(unit="B", total=content_length) as pbar:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                pbar.update(len(chunk))
                f.write(chunk)


class Dataset:
    """
    The dataset class for downloading and loading remote datasets.
    """

    def __init__(self, name: str, url: str, format: str):
        self.name = name
        self.url = url
        self.format = format

    def load(self) -> Any:
        if self.format == "json":
            return json.loads(requests.get(self.url).content)
        raise ValueError(
            f"Unrecognized file format: {self.format}. Valid options are ['json']."
        )

    def download(self, path: str) -> None:
        try:
            download(self.url, path)
        except (ConnectionError, TimeoutError) as e:
            print("Download failed because of network connection issue.")
            raise e
