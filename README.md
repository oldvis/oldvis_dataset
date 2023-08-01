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

## Usage

### `oldvis_dataset.visualizations`

#### `oldvis_dataset.visualizations.download(path: str) -> None`

Request the [metadata of visualizations](https://github.com/oldvis/dataset/blob/main/dataset/output/visualizations.json) and store at `path`.

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
