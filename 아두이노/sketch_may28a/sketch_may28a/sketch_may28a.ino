#include <HuemonelabKit.h>
 SonarSensor sonar(5,6); 
 void setup() {
 Serial.begin(9600); 
 }

 void loop() {
 int value = sonar.read(); 
 Serial.println(value);
 delay(1000);
 }
