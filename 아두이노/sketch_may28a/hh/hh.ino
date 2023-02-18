 #include <HuemonelabKit.h>
 SonarSensor sonar(5,6); 
 Led green(9);

 void setup() {
 Serial.begin(9600); 
 }

 void loop() {
 int value = sonar.read(); 
 Serial.println(value); 
 if (value > 20) { 
  green.off();
  delay(500);
 } else if (value < 20){ 
  green.on();
  delay(500);
 }
}
