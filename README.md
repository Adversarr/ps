# PS is not only for Physical Simulation

## Build

Requirements:
- Python(with pip)

Setup the environment:
```sh
pip install -r requirements.txt
```

To serve:
```sh
mkdocs --color serve
```

To setup your webpage, push this repo to your github, and workflow will run automatically. The branch `gh-pages` stores the generated files.

## Usage

The paper collection is automatic. See pages in `/docs/Papers/_articles` for details. References are:

1. [MkDocs](https://www.mkdocs.org)
2. [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

## Develop

Overview: most functionalities depends on `mkdocs-material` and `mkdocs`, see `mkdocs.yml` for detailed configurations. Two feature `wiki` and `registry` is implemented via two Python hooks, see folder `hooks` for details.

### Understanding the hook

Take paper registry as an example, The collection of paper is implemented in `registry.py`, to add your hook, modify 
```yaml
hooks:
  - hooks/registry.py
```
in `mkdocs.yml`


