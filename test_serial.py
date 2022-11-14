import serial
import time


import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    # print(p)
    if "/dev/cu.usbmodem" not in p[0]:
        continue
    try:
        arduino = serial.Serial(
            port=p[0],
            baudrate=115200,
            timeout=1,
            bytesize=8)
        print(p[0])
        print(arduino)
        # break
    except Exception as e:
        print(e)
        pass

print("starting")
while True:
    # print("x")
    data_2 = arduino.read()
    # print(f"'{data_2}'")
    if len(data_2.strip()):
        try:
            print(data_2.strip().decode("utf-8"))
        except Exception as e:
            print(e)
            print(data_2)
