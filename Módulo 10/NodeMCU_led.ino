int led = 14;// Variable que almacena el pin GPIO 14 de la placa NodeMCU

void setup () {
      
  pinMode( led , OUTPUT); // Configuramos el pin GPIO 14 como salida
    
}
void loop () {

  digitalWrite(led, HIGH);   // Encendemos el led
  delay(1000);                       // Tiempo de encendido 1 segundo
  digitalWrite(led, LOW);    // Apagamos el led 
  delay(1000);                       // tiempo de apagado 1 segundo

}
  
