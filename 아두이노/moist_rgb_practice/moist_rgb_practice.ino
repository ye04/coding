#include <HuemonelabKit.h>

RGBLed rgb(9,10,11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int soil = analogRead(A0);
  Serial.println(soil); 
  if (soil < 500) {
    rgb.setColor(255,0,0);
  } else {
    rgb.setColor(0,0,255);
  }
  delay(100);

}
