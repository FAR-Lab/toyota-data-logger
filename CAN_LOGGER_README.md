# In-Car-Data-Record

Code to collect and process CAN data from Toyota Prius using the 8devices USB2CAN

**NOTE: This code require the use of Linux and `socketcan`**

## Files in this repo:

### `toyotaCan.py`
Python script to read, print, and log raw CAN data to a text file. It requires a connection to a `socketcan` interface. Requires python-can [https://python-can.readthedocs.io/en/latest/]

###  `start_can.sh`
Shell script to start reading and recording CAN data. This calls `toyotaCAN.py`. Save data with the date and time as the filename. Note that this saves the data in a directory called `can_data\`

### `process_can.py`
Python script to process and plot CAN data. Requires Python 2.7, numpy, and matlpotlib

## Instructions

### Logging Data
1. Connect USB2CAN to computer - there should be a red light on the device
2. Open the terminal to set up can link using `socketcan` (you may need to be root for the follwing commands) [1]
3. run `ip link set can0 type can bitrate 500000 listen-only on`
4. run `ip link set can0 up` (you should see the light on the USB2CAN turn green)
5. run `sh start_can.sh`
6. run `Ctrl+c` to exit and stop data capture
  
If everything is working, you should see the code start printing CAN data with the following format to the screen:

`Timestamp: 1472338941.008826        ID: 0224    000    DLC: 8    00 00 00 00 00 00 00 08`

This should also be saving this stream to a text file in `can_data\`

## Hardware
I have tested this using the 8devices USB2CAN [http://www.8devices.com/products/usb2can/]. To get this to work, you need to rewire an OBD-DB9 cable [https://www.sparkfun.com/products/10087] for CAN communication. When you buy it, it is setup for OBD2 which has a different wire configuration.

You only need three wires hooked up CAN_H, CAN_L, and GND for CAN communication.

This table shows what connections should be wired together.

| DB9 | Pin Description | OBDII |
|-----|-----------------|-------|
| 2   | CAN High        | 14    |
| 3   | CAN Low         | 5     |
| 7   | Ground          | 6     |

**NOTE: Using the stock cable shorts connections and will cause issues with your car!**

## References
[1] https://fabiobaltieri.com/2013/07/23/hacking-into-a-vehicle-can-bus-toyothack-and-socketcan/

[2] 
