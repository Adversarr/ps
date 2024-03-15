"""
This module defines classes and functions for managing paper sources and rendering them in a MkDocs site.

Classes:
- PaperSource: Represents a collection of papers.
- Paper: Represents a single paper with its metadata.
- 

Functions:
- on_config: Sets the path to the paper source index file.
- render: Renders the papers in a PaperSource object into HTML.
- on_page_markdown: Extracts metadata from a MkDocs page and adds a Paper object to the corresponding PaperSource.
- on_env: Renders the papers in all PaperSource objects and adds the HTML to the corresponding index file.
"""
import logging
from mkdocs.structure.pages import Page
from mkdocs.structure.files import File, Files
import re
# import pydoi


class PaperSource:
  def __init__(self, name):
    self.name = name
    self.papers = dict()
  
  def add_paper(self, paper):
    self.papers[paper.name] = paper

class Paper:
  def __init__(self, file, name, author, year, tags) -> None:
    self.file: File = file
    self.name = name
    self.tags = tags
    self.author = author
    self.year = year

log = logging.getLogger('mkdocs')
paper_source_index_path = ''
registry = {}
link_re = re.compile(r"^\s*\[.*\]\((.*)\)\s*$")
wiki_files = {}
wiki_folder = 'Wiki'

def on_config(config):
  global paper_source_index_path, wiki_folder
  paper_source_index_path = config.get("paperSourceIndexFile", paper_source_index_path)
  wiki_folder = config.get("wikiFolder", wiki_folder)
  log.info(f"=> Wiki folder is {wiki_folder}")

def render_hierarchy(f, url):
  global wiki_files
  result = "<p>Hierarchy in wiki:</p>\n<ul>\n"
  for k, v in wiki_files.items():
    if url.startswith(k) and k != url:
      relpath = v.file.url_relative_to(f)
      result += f"<li><a href=\"{relpath}\">{v.meta.get('title', k)}</a></li>\n"
  return result + "</ul>\n<hr>\n"

def render_paper_source(f:File, name, ps: PaperSource):
  log.info(f"=> Rendering Paper source {name}")
  result = f"<h2>{name}</h2>\n\n\n"
  years = set([p.year for p in ps.papers.values()])
  for y in years:
    result += f"<h3>{y}</h3><ul>\n\n"
    for k, p in ps.papers.items():
      if p.year != y:
        continue
      relative_url = p.file.url_relative_to(f)
      log.info(f"===> Render paper {k} Relative Path = {relative_url}")
      tg = ', '.join([f"<code>{t}</code>" for t in p.tags])
      result += f"<li><a href=\"{relative_url}\">{p.name}</a>: {tg}</li>\n"
    result += "</ul>\n"
  return result + "\n"

def is_page_paper(page: Page):
  return page.meta.get('paperSource', "") != ""

def is_page_wiki(page: Page):
  url = page.url
  return url.startswith(wiki_folder)


# def process_doi(doi: str):
#   log.info(pydoi.resolve(doi))

def process_paper(page: Page):
  paper_source_name = page.meta.get('paperSource', "").upper()
  title = page.meta.get('title', "")
  tags = page.meta.get('tags', [])
  author = page.meta.get('paperAuthor', "UNKNOWN")
  year = page.meta.get('paperYear', 0)
  if year < 100:
    log.warning(f"Year of {title} is less than 100, assuming it is 20{year}")
    year = year + 2000
  # doi = page.meta.get('doi', "")
  # if len(doi) > 0:
  #   doi = process_doi(doi)
  p = Paper(page.file, title, author, year, tags)
  log.info(f"=> Found paper: {title} by {author} (Year {year}, tags: {tags}, PS={paper_source_name})")
  if registry.get(paper_source_name) is None:
    ps = PaperSource(paper_source_name)
    ps.add_paper(p)
    registry[paper_source_name] = ps
  else:
    registry[paper_source_name].add_paper(p)

def process_wiki(page):
  wiki_files[page.url] = page

def on_page_markdown(markdown: str, page: Page, **kwargs):
  if is_page_paper(page):
    process_paper(page)
  elif is_page_wiki(page):
    process_wiki(page)

def on_page_content(html: str, page: Page, config, files):
  if is_page_wiki(page):
    log.info(f"=> Rendering Wiki page {page.url}")
    result = render_hierarchy(page.file, page.url)
    return result + html

def on_env(env, config, files: Files):
  for f in files:
    if f.src_path == paper_source_index_path:
      f.page.content += "\n".join([ render_paper_source(f, k, v) for k, v in registry.items() ])
  log.info("Registry Done.")