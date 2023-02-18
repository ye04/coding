#include <HuemonelabKit.h>
 ServoMotor motor; 
void setup() {
  // put your setup code here, to run once:
 Serial.begin(9600);
 motor.attach(7);

}

void loop() {
  // put your main code here, to run repeatedly:
  int soil = analogRead(A0); 
  Serial.println(soil);
  if (soil < 1000) {
    motor.write(0); 
    delay(1000); 
  } else {
    motor.write(90); 
    delay(1000);   
  }

}
