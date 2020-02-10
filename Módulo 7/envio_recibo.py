import serial
import time

#nombre del dispositivo serial : dmesg | grep -v disconnect | grep -Eo "tty(ACM|USB)." | tail -1
ser = serial.Serial('/dev/ttyACM0',9600)
ser.flushInput()

def iluminacion (line):
    if int(line) < 800:
        dato = "noche"
    else:
        dato = "dia"
    return dato

while True:
    
    try:
        
        lineBytes = ser.readline()
        line = lineBytes.decode('latin-1').strip()
        print(line)  
        
        mensaje = iluminacion(line).encode('latin-1')
        ser.write(mensaje)
        time.sleep(0.5)
        
    except KeyboardInterrupt:
        break
