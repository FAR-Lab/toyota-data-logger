#!/usr/bin/env python
"""
IMU Data logger
imu_logger.py

Author: Nik Martelaro
Last updated: 26 Jan 2017

Purpose: Log data from the in car IMU to a simple csv file. Timestamp every data
entry for data synchornization.
"""

import serial
import time
import sys, traceback

def main():
	try:
		participant = sys.argv[1]
		print(participant)

		# setup the USB serial port
		ser = serial.Serial()
		ser.port = "/dev/tty.usbserial-ADAPDYMqt"
		ser.baudrate = 115200
		ser.timeout = 1
		ser.open()

		# setup the csv file to save the data
		f = open(participant + '/' + 'imuLog_' +  str(int(time.time())) + '.csv', 'w')

		while True:
			imuData = ser.readline()
			# log the system timestamp (unix) an then the data
			f.write(str(time.time()) + ',' + imuData.decode("utf-8"))
			print(str(time.time()) + ',' + imuData.decode("utf-8"))

	except KeyboardInterrupt:
		print("\nShutdown requested...exiting")
		# close things cleanly
		f.close()
		ser.close()

	except Exception:
		traceback.print_exc(file=sys.stdout)
		sys.exit(0)

if __name__ == "__main__":
    main()
