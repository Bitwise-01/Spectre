# Date: 03/18/2018
# Author: Ethical-H4CK3R
# Description: Scrape a site

from re import sub 
from const import USER_AGENT
from dryscrape import Session 
from cookielib import LWPCookieJar 
from mechanize import _http, Browser

class Scraper(object):
 def __init__(self, url, js):
  self.url = url  
  self.html = self.js_get_source() if js else self.no_js_get_source()
 
 def no_js_get_source(self):
  br = Browser()
  br.set_handle_equiv(True)
  br.set_handle_referer(True)
  br.set_handle_robots(False)
  br.set_cookiejar(LWPCookieJar())
  br.addheaders=[('User-agent', USER_AGENT)]
  br.set_handle_refresh(_http.HTTPRefreshProcessor(), max_time=10)
  try:return br.open(self.url).read()
  except:exit('[!] Failed to fetch html source')

 def js_get_source(self):
  session = Session()
  session.set_header('User-Agent', USER_AGENT)
  try:session.visit(self.url) 
  except:exit('[!] Failed to fetch html source')
  return session.body()