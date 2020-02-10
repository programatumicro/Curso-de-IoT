int pinAnalogico = A0; 
int led = 13;

void setup () {
      pinMode (pinAnalogico,INPUT);
      pinMode( led , OUTPUT);
      Serial.begin(9600); 
}
void loop () {

 int valorPinAnalogico = analogRead(pinAnalogico);
 Serial.println(valorPinAnalogico);
 delay(100);

if (Serial.available()>0){

  String dato = Serial.readStringUntil('\n');
  if (dato == "noche"){
    digitalWrite(led,HIGH);
  }
   else if (dato == "dia"){
    digitalWrite(led,LOW);
   }
}delay(100);
}
  
  
