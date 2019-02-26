#!/bin/bash

dt=$(date '+%d-%m-%Y-%H:%M:%S');

# start the python can script and save

python toyotaCAN/toyotaCan.py -c can0 -i socketcan -f "can_data/$dt.txt"
