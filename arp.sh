#!/bin/bash

arp-scan --interface=wlp3s0 --localnet > arp.txt
cat ./arp.txt
echo ''
python ./ips.py
python ./hn.py

