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
float t[75];
float mes[75];
float cmd[75];
int cmin=1300;
int cmax=1500;

void setup() {
  Serial.begin(115200);
  
  ESC.attach(9);               
  ESC.writeMicroseconds(1000); 

  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor);
  scale.tare();

  delay(3000);   
  Serial.println("[OK]");
  Serial.println("[setup done]");


}

void loop() 
{


  trash=scale.read();
  if (Serial.available() )
  {
  if (Serial.read()=='s')
  {
    ESC.writeMicroseconds(cmin);
    delay(1000);
    
    for (int i=0;i<25;i++)
    {
      t[i]=millis();
      mes[i]=scale.read();
      cmd[i]=cmin;
    }
    ESC.writeMicroseconds(cmax);
    for (int i=25;i<75;i++)
    {
      t[i]=millis();
      mes[i]=scale.read();
      cmd[i]=cmax;
    }
    ESC.writeMicroseconds(1000);
    for (int i=0;i<75;i++)
    {
      Serial.print(t[i]);
      Serial.print('\t');
      Serial.print(cmd[i]);
      Serial.print('\t');
      Serial.println(mes[i]);
    }
    delay(10);
  }
  }
}