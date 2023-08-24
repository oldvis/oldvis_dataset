<a href="https://pypi.org/project/oldvis_dataset/">
    <img alt="Newest PyPI version" src="https://img.shields.io/pypi/v/oldvis_dataset.svg">
</a>
<a href="https://github.com/psf/black">
    <img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg">
</a>
<a href="http://commitizen.github.io/cz-cli/">
    <img alt="Commitizen friendly" src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg">
</a>

# oldvis_dataset

A Python package for downloading metadata and images of old visualizations in [oldvis/dataset](https://github.com/oldvis/dataset).

## Installation

```sh
pip install oldvis_dataset
```

## Usage Example

Downloading metadata of visualizations:

```python
from oldvis_dataset import visualizations
visualizations.download(path="./visualizations.json")
```

Downloading images:

```python
from oldvis_dataset import visualizations, fetch_image
visualizations.download(path="./visualizations.json")
fetch_images(metadata_path="./visualizations.json", img_dir="./images/")
```

Downloading images with filtering condition:

```python
import json
from oldvis_dataset import visualizations, fetch_image
metadata = visualizations.load()
# Download public domain images.
metadata = [d for d in metadata if d["rights"] == "public domain"]
path = "./visualizations.json"
with open(path, "w", encoding="utf-8") as f:
    json.dump(metadata, ensure_ascii=False)
fetch_image(metadata_path=path, img_dir="./images/")
```

## API

### `oldvis_dataset.visualizations`

#### `oldvis_dataset.visualizations.download(path: str) -> None`

Request the [metadata of visualizations](https://github.com/oldvis/dataset/blob/main/dataset/output/visualizations.json) and store at `path`.
Each store metadata entry follows the data structure `ProcessedMetadataEntry` ([Source](https://github.com/oldvis/libprocess/blob/main/libprocess/typing.py)).

```python
visualizations.download(path="./visualizations.json")
```

#### `oldvis_dataset.visualizations.load() -> List`

Request the [metadata of visualizations](https://github.com/oldvis/dataset/blob/main/dataset/output/visualizations.json) without saving.

```python
data = visualizations.load()
```

### `oldvis_dataset.authors`

#### `oldvis_dataset.authors.download(path: str) -> None`

Request the [metadata of authors](https://github.com/oldvis/dataset/blob/main/dataset/output/authors.json) and store at `path`.

```python
authors.download(path="./authors.json")
```

#### `oldvis_dataset.authors.load() -> List`

Request the [metadata of authors](https://github.com/oldvis/dataset/blob/main/dataset/output/authors.json) without saving.

```python
data = authors.load()
```

### `oldvis_dataset.fetch_images(metadata_path: str, img_dir: str) -> None`

Fetch images and store at `img_dir` according to the URLs in the downloaded metadata of visualizations stored at `metadata_path`.

```python
fetch_images(metadata_path="./visualizations.json", img_dir="./images/")
```

⚠️The image fetching can be slow.

### `oldvis_dataset.save_as_bib(metadata_path: str, bib_path: str) -> None`

Save the fetched metadata at `metadata_path` as a BibTeX file and store at `bib_path`.

```python
save_as_bib(metadata_path="./visualizations.json", bib_path="./visualizations.bib")
```
