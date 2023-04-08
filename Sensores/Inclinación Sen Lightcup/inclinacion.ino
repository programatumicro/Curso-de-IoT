int sensorPin = 2; // pin digital al que está conectado el sensor
int ledPin = 3; //pin digital que controla el led
int sensorValue; // variable que almacena la lectura del sensor

void setup() {
  
  pinMode(sensorPin, INPUT); // Configura el pin del sensor como entrada
  pinMode(ledPin, OUTPUT); // Configura el LED integrado en la placa como salida
  Serial.begin(9600); // Inicia la comunicación serial para imprimir la lectura del sensor
  
}

void loop() {
  sensorValue = digitalRead(sensorPin); // Lee el valor del sensor
  
  if (sensorValue == LOW) { // Si el sensor detecta una inclinación
    digitalWrite(ledPin, HIGH); // Enciende el LED integrado en la placa
    Serial.println("Inclinacion detectada"); // Imprime un mensaje en el monitor serial
  } else {
    digitalWrite(ledPin, LOW); // Apaga el LED integrado en la placa
  }
  
  delay(100); // Espera un momento antes de leer el sensor nuevamente
}
