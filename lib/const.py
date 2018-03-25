# Date: 03/19/2018
# Author: Ethical-H4CK3R
# Description: Configuration file

from os import getcwd

FOLDER = 'index'
INDEX = '{}/index.html'.format(FOLDER)

PHP_SCRIPT_FILE = 'login.php'
CREDENTIALS_FILE = '{}/accounts.txt'.format(getcwd())
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

ENGINES = {
 'Bing': 'https://www.bing.com/search?q=',
	'DuckDuckGo': 'https://duckduckgo.com/?q=',
 'Google': 'https://www.google.com/search?q='
}

SYMBOL_SUBS = {
 '?': 'M0_0N',
 '&': 'L4ND',
 '%': 'M4RS'
}