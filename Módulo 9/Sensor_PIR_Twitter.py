import RPi.GPIO as GPIO #Libreria para configuracion de pines de las Raspberry Pi
import requests  #Libreria para envio de peticiones HTTP
import time #Libreria para hacer uso del modulo de tiempo y crear los delays


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


SENSOR_PIR = 24  #pin 24 Sensor PIR
GPIO.setup(SENSOR_PIR,GPIO.IN)     #SENSOR_PIR como pin de entrada
url = "https://api.thingspeak.com/apps/thingtweet/1/statuses/update"  #url que nos proporciona ThingTweet
data = {"api_key":"XXXXXXXXXXXXX","status":"Detección de Intruso"}


print ("Sensor estabilizandonse")
time.sleep(3)    #Delay de 2 segundos para estabilizar al sensor
print("Sensor Activado")

try:
    while True:
        
        
        if GPIO.input(SENSOR_PIR)==1:
            print("Intruso Detectado")
            resp =requests.post(url,data)
            print("Mensaje Publicado en Twitter")
            GPIO.input(SENSOR_PIR)==0
            time.sleep(5)
    
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
    
    
    
        
        
        
    
    
    
    
