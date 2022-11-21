![](https://img.shields.io/badge/code%20style-black-000000.svg)

Slides for a presentation about big O notation.

Slides available at: https://cjkjvfnby.github.io/big-o-easy-as-pie/

# Development

## Install dev requirements
```shell
pip install -r requirements-dev.txt
```

## Install pre-commit
- add hooks
  ```shell
  pre-commit install
  pre-commit install --hook-type commit-msg
  ```
- update to the latest versions
  ```shell
  pre-commit autoupdate
  ```

## Formatting and Linting
```shell
pre-commit run --all-files
```

## Regenerate graphs if somethng changed.

```shell
draw_graphs/make_images.py
```

## Build documentation

Using `make html` does not work with code samples.
If page was not changed, they will not be rendered.

```shell
sphinx-build . _build -W -a -j auto --keep-going
```
