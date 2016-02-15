#!/bin/bash

if [ ! -d "env" ]; then
  virtualenv env
  env/bin/pip install -r requirements.pip
fi

env/bin/python initdb.py
env/bin/python run.py
