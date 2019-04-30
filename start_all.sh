#!/bin/sh

#  start_all.sh
#  
#
#  Created by wangyue on 2019-04-23.
#  




printf "Participant ID: "
read part_id
echo "$part_id"

printf "Use Panda to read CAN? y/n       "
read flag


mkdir "$part_id"


#start IMU
printf "Start running IMU..\n"
python imu_logger_linux.py $part_id &

# start CAN bus
if [ $flag = "y" ]
then
	printf "Start PANDA CANbus ...\n"
	# python CAN_panda.py $part_id &
else 
	ip link set can0 type can bitrate 500000 listen-only on
	ip link set can0 up

	path_2='/can_data.txt'
	path="$part_id$path_2"

	printf "Start CANbus ..\n."
	python toyotaCAN/toyotaCan.py -c can0 -i socketcan -f $path &
fi

# start GPS
printf "Start GPS...\n"
sudo systemctl stop gpsd.socket
sudo systemctl disable gpsd.socket
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
python gpsLogger_linux.py $part_id &

#start IMU
# printf "Start running IMU.."
# python imu_logger_linux.py $part_id
