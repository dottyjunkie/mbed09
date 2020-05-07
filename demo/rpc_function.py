import serial

import time

serdev = '/dev/ttyACM1'

s = serial.Serial(serdev)

s.write(bytes("/LEDControl/run 1 1\r", 'UTF-8'))
time.sleep(0.5)

s.write(bytes("/LEDControl/run 2 1\r", 'UTF-8'))
time.sleep(0.5)

s.write(bytes("/LEDControl/run 3 1\r", 'UTF-8'))
time.sleep(0.5)

while 1:
    s.write(bytes("/LEDControl/run 1 0\r", 'UTF-8'))
    time.sleep(0.5)

    s.write(bytes("/LEDControl/run 1 1\r", 'UTF-8'))
    time.sleep(0.5)

    s.write(bytes("/LEDControl/run 3 0\r", 'UTF-8'))
    time.sleep(0.5)

    s.write(bytes("/LEDControl/run 3 1\r", 'UTF-8'))
    time.sleep(0.5)

s.close()