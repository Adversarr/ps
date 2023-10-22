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

The paper collection is automatic. See pages in `/docs/Papers/_articles` for details.

## Develop

### Understanding the hook

The collection of paper is implemented in `libr.py`, to add your hook, modify 
```yaml
hooks:
  - libr.py
```
in `mkdocs.yml`


