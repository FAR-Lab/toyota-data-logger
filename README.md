# toyota-data-logger
Scripts for data logging in the Toyota Prius


## To run gpsLogger_linux.py
Scripts store in local computer: DOcuments/recording/gpsLogger_linux.py
If the gps cannot load location, try following command in a new terminal.
    sudo systemctl stop gpsd.socket
    sudo systemctl disable gpsd.socket
****  after test, if want to enable default********
    sudo systemctl enable gpsd.socket
    sudo systemctl start gpsd.socket
***************************************************
    sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
    cgps -s