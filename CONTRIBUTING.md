# Contributing

Thanks for being interested in contributing to this project!

## Development 

### Setup

Clone this repo to your local machine and install the dependencies.

```bash
poetry install
```

## Contributing

### Existing functions

Feel free to enhance the existing functions. Please try not to introduce breaking changes.

### New functions

There are some notes for adding new functions

- Before you start working, it's better to open an issue to discuss first.
- The implementation should be placed under `oldvis_dataset`

## Code Style

Use [Black](https://github.com/psf/black) to detect code style issues and fix the issues before committing.

## Publishing the Package

The steps to publish the package:

1. Bump the version in `pyproject.toml`.
2. create a new tag for the version with `git tag v*.*.*`.
3. push the tag to Github with `git push origin v*.*.*`, which will trigger the Github workflow at `.github/workflow/publish-to-pypi.yml` to automatically publish the package to PyPI.

## Thanks

Thank you again for being interested in this project! You are awesome!
