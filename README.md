# Spectre
A simple program, for simple people, for doing simple social engineering attacks.

### Requirements
 - Kali Linux 2.0
 - Python v2.7

### Installation
```sh
$ git clone https://github.com/Ethical-H4CK3R/Spectre
$ cd Spectre
$ chmod +x install.sh
$ ./install.sh
```

### Usage

Help menu
```sh
$ python spectre.py --help
```

Clone Facebook by name using default engine
```sh
$ python spectre.py -n facebook
```

Clone Facebook with javascript
```sh
$ python spectre.py -n facebook --js
```

Clone Facebook by name using Bing
```sh
$ python spectre.py -n facebook -e bing
```

Clone Facebook by name using Google
```sh
$ python spectre.py -n facebook -e google
```

Clone Facebook by name using DuckDuckgo
```sh
$ python spectre.py -n facebook -e duckduckgo
```

Clone Facebook by url
```sh
$ python spectre.py -u https://facebook.com
```

Clone Facebook by url
```sh
$ python spectre.py -u https://facebook.com/login
```

### Disclaimers
 - Don't abuse this program, stay ethical.
 - This program will not working on every site.
 - Google will stop responing for a while if you over use it.
