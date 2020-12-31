import RPi.GPIO as GPIO                    
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Trig = 23   #pin 23 como Trig                              
Echo = 24   #pin 24 como Echo
pulsador1 = 25    #pin 25 pulsador1 que se encarga de iniciar la medicion de distancia 
pulsador2 = 18    #pin 18 pulsador2 que se encarga de detener la medicion de distancia
v_sonido= 34300   # Velocidad del sonido 34300cm/s
iniciar_medicion = False  #variable de control para los pulsadores

print( "Medicion de la distancia en curso")

GPIO.setup(Trig,GPIO.OUT)    #TRIG como pin de salida        
GPIO.setup(Echo,GPIO.IN)     #ECHO como pin de entrada
GPIO.setup(pulsador1,GPIO.IN)  #Pulsador 1 como pin de entrada
GPIO.setup(pulsador2,GPIO.IN)  #Pulsador 2 como pin de entrada

GPIO.output(Trig, False)     #TRIG en estado bajo

print ("Sensor estabilizandonse")
time.sleep(2)    #Delay de 2 segundos para estabilizar al sensor
print ("Presione el pulsador 1 para medir la distancia")

  
while True:
    
    if GPIO.input(pulsador1) == 1: #verificamos si el pulsador 1 ha sido presionado para iniciar la medicion de distancia
        iniciar_medicion = True  #varible que indica que se puede iniciar con la medición dependiendo de su valor booleano

  
    while iniciar_medicion == True:
    
        GPIO.output(Trig, True)     #TRIG en estado alto          
        time.sleep(0.00001)         #Delay de 10 microsegundos           
        GPIO.output(Trig, False)    #TRIG en estado bajo               

        while GPIO.input(Echo)==0:    
            inicio_pulso = time.time()  # tiempo de inicio de pulso
            

        while GPIO.input(Echo)==1:
            fin_pulso = time.time()   # tiempo de fin de pulso
            
                        
        tiempo = fin_pulso - inicio_pulso   #Se obtienen la duración del pulso, calculando la diferencia entre inicio y fin del pulso
        distancia =  v_sonido * (tiempo/2)    #calculamos la distancia                 
        distancia = round(distancia, 2)     #se redondea a dos decimales       

        if distancia > 2 and distancia < 400:   #Comprueba si la distancia está dentro del rango de funcionamiento
            print( "Distancia: ",distancia,"cm")      #Imprime la distancia  

        else:
            print("Fuera de Rango")
        
        if GPIO.input(pulsador2) == 1:  #detecta si se ha presionado el pulsador 2
            print("Ha presionado el boton 2 por tal motivo se pausa la medición")
            iniciar_medicion = False   #cambia el estado de la variable para detener la medición
            print("Debe presionar el boton numero 1 para reiniciar la medición")
            
        time.sleep(1) #lectura de la distancia cada 1 segundo
        
