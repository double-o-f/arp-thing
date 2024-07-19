#!/bin/bash

arp-scan --interface=wlp3s0 --localnet > arp.txt #--interface=wlp6s0 3  enp0s31f6
cat ./arp.txt
echo ''
python ./ips.py
python ./hn.py

