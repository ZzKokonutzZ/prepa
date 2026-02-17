#include <Servo.h>
#include "HX711.h"

#define LOADCELL_DOUT_PIN 3
#define LOADCELL_SCK_PIN 2

Servo ESC;
HX711 scale;
float trash;
int command = 1000;
int nbpoints=1;
float calibration_factor = 700;

void setup() {
  Serial.begin(115200);
  Serial.println("[OK]");
  ESC.attach(9);               
  ESC.writeMicroseconds(1000); 

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor);
  scale.tare();

  delay(3000);   
  
  Serial.println("[setup done]");


}

void loop() 
{


  trash=scale.read();
  if (Serial.available() )
  {
  if (Serial.read()=='s')
  {
    Serial.println("[START]");
    for (command=1250;command<=1750;command+=10) 
    {

      ESC.writeMicroseconds(command);
      for (int t=0;t<10;t+=1)
      {
        delay(10);
        trash=scale.read();
      }
      for (int t=0;t<nbpoints;t+=1)
      {
        float check=scale.read();
        while (check==-1.0){
          check=scale.read();
        }
        Serial.print(check);
        Serial.print("\t");
        Serial.println(command);
        delay(10);
      }
      
  
   
   
    }
    command=1000;
    ESC.writeMicroseconds(command);
  }
  }
  delay(10);
}