import logging, re
from yaml.loader import BaseLoader
from mkdocs.structure.pages import Page
from mkdocs.structure.files import File, Files


log = logging.getLogger('mkdocs')
link_re = re.compile(r"^\s*\[.*\]\((.*)\)\s*$")
wiki_files = {}
wiki_folder = 'Wiki'

def on_config(config):
  global wiki_folder
  wiki_folder = config.get("wikiFolder", wiki_folder)
  log.info(f"=> Wiki folder is {wiki_folder}")

def is_wiki_url(url):
  return url.startswith(wiki_folder)

# collect all the files under `Wiki` folder
def on_page_markdown(markdown: str, page: Page, config, files):
  if is_wiki_url(page.url):
    wiki_files[page.url] = page

def render_hierarchy(f, url):
  global wiki_files
  result = "<p>Hierarchy in wiki:</p>\n<ul>\n"
  for k, v in wiki_files.items():
    if url.startswith(k) and k != url:
      relpath = v.file.url_relative_to(f)
      result += f"<li><a href=\"{relpath}\">{v.meta.get('title', k)}</a></li>\n"
  return result + "</ul>\n<hr>\n"

def on_page_content(html: str, page: Page, config, files):
  if is_wiki_url(page.url):
    log.info(f"=> Rendering Wiki page {page.url}")
    result = render_hierarchy(page.file, page.url)
    return result + html