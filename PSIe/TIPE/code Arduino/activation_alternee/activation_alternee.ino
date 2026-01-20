#include <Servo.h>

Servo ESC;
String command;
int speed;
void setup() {
  ESC.attach(9, 1000, 2000);
  Serial.begin(9600);
  Serial.println("Arming ESC...");

  ESC.writeMicroseconds(1000); // signal bas pour armer
  delay(3000); // attendre 3 secondes

  Serial.println("ESC armed. Starting slowly...");
}

void loop() {
  if (Serial.available()) {
    command=Serial.readStringUntil('\n');
    command.trim();
    speed=command.toInt();
    ESC.writeMicroseconds(speed);
  }
  
}