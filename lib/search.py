# Date: 03/18/2018
# Author: Ethical-H4CK3R
# Description: Search a login page using a search engine

from const import ENGINES
from const import USER_AGENT
from bs4 import BeautifulSoup
from dryscrape import Session 

class DuckDuckGo(object):
 def __init__(self, site_name):
  self.url = '{}{}+login+site'.format(ENGINES['DuckDuckGo'], '+'.join([_ for _ in site_name.split()]))
  self.url = self.url+'&t=hy&ia=web'
  
 def search(self):
  session = Session()
  session.set_header('User-Agent', USER_AGENT)
  try:
   session.visit(self.url)
   for result in BeautifulSoup(session.body(), 'html.parser').findAll('h2', {'class': 'result__title'})[0:2]:
   	if not 'http://duckduckgo.com/y.js' in result.find('a')['href']:
   	 return result.find('a')['href']
  except:
   exit('[!] Error: Unable to contact https://duckduckgo.com')

class Google(object):
 def __init__(self, site_name):
  self.url = '{}{}'.format(ENGINES['Google'], site_name)
  self.url = '{}+{}'.format(self.url, 'login+site')
  
 def search(self):
  session = Session()
  session.set_header('User-Agent', USER_AGENT)
  try:
   session.visit(self.url) 
   return BeautifulSoup(session.body(), 'html.parser').find('h3', {'class': 'r'}).find('a')['href']
  except:
   exit('[!] Error: Unable to contact https://google.com')  

class Bing(object):
 def __init__(self, site_name):
  self.url = '{}{}'.format(ENGINES['Bing'], site_name)
  self.url = '{}+{}'.format(self.url, 'login+site')
  
 def search(self):
   session = Session()
   session.set_header('User-Agent', USER_AGENT)
   try:
    session.visit(self.url) 
    for result in BeautifulSoup(session.body(), 'html.parser').findAll('h2'):
     if not 'r.bat.bing' in result.find('a')['href']:
      return result.find('a')['href']
   except:
    try:
     return BeautifulSoup(session.body(), 'html.parser').find('h2').find('a')['href']
    except:exit('[!] Error: Unable to contact https://www.bing.com')    