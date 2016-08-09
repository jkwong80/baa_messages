#!/bin/bash
brew install thrift
pip install -r requirements.txt
pre-commit install
vagrant up
vagrant halt
