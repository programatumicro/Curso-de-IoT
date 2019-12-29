import serial

#nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()

while True:
    
    try:
        
        lineBytes = ser.readline()
        line = lineBytes.decode('utf-8').strip()
        print(line)
        
    except KeyboardInterrupt:
        break
        
