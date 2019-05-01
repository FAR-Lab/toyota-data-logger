# toyota-data-logger
Scripts for data logging in the Toyota Prius


## To run gpsLogger_linux.py
Here I refer to this document https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi/setting-everything-up
Scripts store in local computer: Documents/recording/gpsLogger_linux.py
### Trouble Shooting
If the gps cannot load location, try following command in a new terminal.

    sudo systemctl stop gpsd.socket
    sudo systemctl disable gpsd.socket
    sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
After this, can test on terminal is it works well:

    cgps -s
### after test, if want to enable default
    sudo systemctl enable gpsd.socket
    sudo systemctl start gpsd.socket
 
 
 ## Read From Panda
 From Cloud:
    https://community.comma.ai/cabana/
 From USB:
    pip install pandacan
