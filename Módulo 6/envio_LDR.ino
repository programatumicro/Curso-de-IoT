
int pinAnalogico = A0; pin A0 analógico del arduino

void setup() {
  pinMode (pinAnalogico,INPUT);
  Serial.begin(9600);
   
}

void loop() {
  int valorPinAnalogico = analogRead(pinAnalogico);
  Serial.println(valorPinAnalogico);
  delay(500);

}
