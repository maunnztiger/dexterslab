#!/bin/bash
sudo rm -rf venv
sudo python3 -m virtualenv venv
sudo chown -R igor:igor venv/ && sudo chmod -R 777 venv/
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
