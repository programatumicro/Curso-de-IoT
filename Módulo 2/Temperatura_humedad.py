

import Adafruit_DHT
import time

sensor = Adafruit_DHT.DHT11
pin = 23

while True:
    
    humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
    
    if humedad is not None and temperatura is not None:
        print(f'Temperatura={temperatura:.2f}*C  Humedad={humedad:.2f}%')
        #print("Temperatura = {}°C humedad = {}% ".format(temperatura,humedad))  
    else:
        print('Fallo la lectura del sensor.Intentar de nuevo')
    
    time.sleep(5) 
