import gps
import time
import sys
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
participant = sys.argv[1]
print(participant)
f = open(participant + '/' + 'gpsLog_' +  str(int(time.time())) + '.csv', 'w')

session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
while True:
    try:
    #     participant = sys.argv[1]
    #     print(participant)

        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                # print(report)
                # <dictwrapper: {'class': 'TPV', 'device': '/dev/ttyUSB0', 'mode': 3, 'time': '2019-03-15T20:02:44.000Z', 'ept': 0.005, 'lat': 40.75534, 'lon': -73.955945, 'alt': 28.5, 'track': 15.87, 'speed': 0.051, 'climb': 0.0}>
                temp = str(report.time) + ',' + str(report.lon) +',' + str(report.lat)
                

                f.write(temp + '\n')
    except KeyError:
        pass
    except KeyboardInterrupt:
        f.close()
        quit()
    except StopIteration:
        session = None
        print("GPSD has terminated")
