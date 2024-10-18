#!/bin/bash
sudo rm -rf venv
sleep 1
sudo python3 -m virtualenv venv
sleep 1
sudo chown -R igor:igor venv/ && sudo chmod -R 777 venv/
sleep 1
source venv/bin/activate
sleep 1
pip install -r requirements.txt
sleep 1
python3 main.py
