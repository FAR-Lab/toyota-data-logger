#!/bin/sh

#  start_all.sh
#  
#
#  Created by wangyue on 2019-04-23.
#  

dt = $(data '+%d-%m-%Y-%H:%M:%S');

echo "Participant ID : $1"
part_id = $1

# start CAN bus
ip link set can0 type can bitrate 500000 listen-only on
ip link set can0 up
can_file_path = part_id + "/can_data/$dt.txt"

python toyotaCan.py -c can0 -i socketcan -f can_file_path

# start GPS
python gpsLogger_linux.py part_id

#start IMU
python imu_logger.py part_id
