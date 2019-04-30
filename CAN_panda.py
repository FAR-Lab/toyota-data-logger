#!/usr/bin/env python
from __future__ import print_function
import binascii
import csv
import sys
from panda import Panda
import datetime
import time

def can_logger():
    try:
        print("Trying to connect to Panda over USB...")
        p = Panda()
    
    except AssertionError:
        print("USB connection failed. Trying WiFi...")

    try:
        p = Panda("WIFI")
    except:
        print("WiFi connection timed out. Please make sure your Panda is connected and try again.")
        sys.exit(0)

    try:
        participant_id = sys.argv[1]
        outputfile = open(participant_id + '/can_bus_panda.csv', 'wb')
        csvwriter = csv.writer(outputfile)
        #Write Header
        csvwriter.writerow(['Timestamp', 'Bus', 'MessageID', 'Message', 'MessageLength'])
        print("Participant: " + participant_id + ". Writing csv file output.csv. Press Ctrl-C to exit...\n")

        bus0_msg_cnt = 0
        bus1_msg_cnt = 0
        bus2_msg_cnt = 0

        while True:
            can_recv = p.can_recv()

            for address, _, dat, src  in can_recv:
                csvwriter.writerow([str(time.time()), str(src), str(hex(address)), "0x" + binascii.hexlify(dat), len(dat)])

            if src == 0:
                bus0_msg_cnt += 1
            elif src == 1:
                bus1_msg_cnt += 1
            elif src == 2:
                bus2_msg_cnt += 1

            print("Message Counts... Bus 0: " + str(bus0_msg_cnt) + " Bus 1: " + str(bus1_msg_cnt) + " Bus 2: " + str(bus2_msg_cnt), end='\r')

    except KeyboardInterrupt:
        print("\nNow exiting. Final message Counts... Bus 0: " + str(bus0_msg_cnt) + " Bus 1: " + str(bus1_msg_cnt) + " Bus 2: " + str(bus2_msg_cnt))
        outputfile.close()

if __name__ == "__main__":
    can_logger()