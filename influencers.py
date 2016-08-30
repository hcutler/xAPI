import urllib
import wikipedia
from bs4 import BeautifulSoup
import yaml
import json
import sys
import encodings
from encodings import aliases
from unidecode import unidecode

data = []

# 2016 Time 100 Most Influential People (http://time.com/collection/2016-time-100/)
with open("influencers.yaml", "r") as yaml_file:
  entries = yaml_file.read().splitlines()

  for e in entries:
    try:
      title = wikipedia.page(e)
      pageurl = title.url
      summary = title.summary
      categs = title.categories
      outlinks = title.links
      sections = title.sections
      refs = title.references
      #content = title.content
      data.append({'summary': summary, 'url': pageurl ,
              'categories': categs, 'outlinks': outlinks,'sections': sections,
              'references': refs})  #'content': content, 'imageurl': imageurl} 'title': str(title)
      data.sort
      filename = (str(e) + '.yaml').replace(" ", "_")
      print filename
      with open(filename, 'w') as outfile:
        outfile.write( yaml.safe_dump(data,encoding='utf-8',default_flow_style=False,allow_unicode=True))
        data = []
    except wikipedia.exceptions.DisambiguationError as e:
      pass
    except wikipedia.exceptions.PageError as pe:
      pass
