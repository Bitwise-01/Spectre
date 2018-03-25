#!/usr/bin/env bash

install() {
 # configure the repository file
 echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list

 # update outdated 
 gpg --keyserver hkp://keys.gnupg.net --recv-key 7D8D0BF6
 gpg -a --export 7D8D0BF6 | apt-key add -

 # update 
 apt-get update 

 # install essentials
 apt-get install qt5-default libqt5webkit5-dev build-essential python-lxml python-pip xvfb -y
 apt-get install lighttpd php7.0-cgi -y

 # clean up
 apt-get autoremove -y

 # install requirements
 pip install -UI -r requirements.txt
}

install
install
