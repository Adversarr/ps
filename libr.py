import logging, re
import mkdocs
import os
import yaml
from yaml.loader import BaseLoader
from mkdocs.structure.pages import Page
from mkdocs.structure.files import File, Files

class PaperSource:
  def __init__(self, name):
    self.name = name
    self.papers = dict()
  
  def add_paper(self, paper):
    self.papers[paper.name] = paper

class Paper:
  def __init__(self, url, name, author, year, tags) -> None:
    self.url = url
    self.name = name
    self.tags = tags
    self.author = author
    self.year = year

log = logging.getLogger('mkdocs')
psipath = ''
registry = {}

def on_config(config):
  global psipath
  psipath = config.get("paperSourceIndexFile", psipath)


def render(f:File, name, ps: PaperSource):
  log.info(f"=> Rendering Paper source {name}")
  result = f"<h2>{name}</h2>\n\n\n"
  years = set([p.year for p in ps.papers.values()])
  for y in years:
    result += f"<h3>{y}</h3><ul>\n\n"
    for k, p in ps.papers.items():
      if p.year != y:
        continue
      log.info(f"===> Render paper {k} Relative Path = {p.url}")
      tg = ', '.join([f"<code>{t}</code>" for t in p.tags])
      result += f"<li><a href=\"{p.url}\">{p.name}</a>: {tg}</li>\n"
    result += "</ul>\n"
  return result + "\n"


def on_page_markdown(markdown: str, page: Page, **kwargs):
  psname = page.meta.get('paperSource', "").upper()
  if psname == '':
    return
  title = page.meta.get('title', "")
  tags = page.meta.get('tags', [])
  author = page.meta.get('paperAuthor', "UNKNOWN")
  year = page.meta.get('paperYear', 1984)
  url = page.file.url_relative_to(psipath)
  p = Paper(url, title, author, year, tags)
  log.info(f"=> Found paper: {title} by {author} (Year {year}, tags: {tags}, PS={psname})")
  if registry.get(psname) is None:
    ps = PaperSource(psname)
    ps.add_paper(p)
    registry[psname] = ps
  else:
    registry[psname].add_paper(p)



def on_env(env, config, files: Files):
  for f in files:
    if f.src_path == psipath:
      f.page.content += "\n".join([ render(f, k, v) for k, v in registry.items() ])