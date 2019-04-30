import serial
import time
import sys, traceback

port = "/dev/ttyUSB0"  # Raspberry Pi 2

def main():
    try:
        participant = sys.argv[1]
        print(participant)

        # setup the csv file to save the data
        f = open(participant + '/' + 'gpsLog_' +  str(int(time.time())) + '.csv', 'w')

        # setup the USB GPS serial port
        ser = serial.Serial()
        print(ser)
        # ser.port = '/dev/cu.usbserial'
        ser.portal = port
        ser.baudrate = 4800
        ser.timeout = 1
        ser.open()

        while True:
            gpsData = ser.readline()
        # log the $GPRMC lines - these provide the following data [http://aprs.gids.nl/nmea/#rmc]
        # $GPRMC,hhmmss.ss,A,llll.ll,a,yyyyy.yy,a,x.x,x.x,ddmmyy,x.x,a*hh
        # 	= UTC of position fix
        #	= Data status (V=navigation receiver warning)
        #	= Latitude of fix
        #	= N or S
        #	= Longitude of fix
        #	= E or W
        #	= Speed over ground in knots
        #	= Track made good in degrees True
        #	= UT date
        #	= Magnetic variation degrees (Easterly var. subtracts from true course)
        #	= E or W
        #	= Checksum
            # print(gpsData[0:6].decode('utf-8'))
            try:
                if gpsData[0:6].decode('utf-8') == '$GPRMC':
                    # log the system timestamp (unix) an then the data
                    f.write(str(time.time()) + ',' + gpsData.decode('utf-8'))
                    print(str(time.time()) + ',' + gpsData.decode('utf-8'))
            except:
                pass

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
