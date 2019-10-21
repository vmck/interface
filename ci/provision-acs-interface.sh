#!/bin/bash -e

sudo apt-get update -qq
sudo apt-get -qq install python3-pip libsasl2-dev python-dev libldap2-dev libssl-dev
sudo pip3 install pipenv

cd /vagrant
pipenv install
mkdir -p data
pipenv run ./manage.py migrate

echo "✔ acs-interface installed successfully"
