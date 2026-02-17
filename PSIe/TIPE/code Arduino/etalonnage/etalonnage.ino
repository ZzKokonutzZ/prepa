#include "HX711.h"

#define LOADCELL_DOUT_PIN 3
#define LOADCELL_SCK_PIN 2

HX711 scale;

float calibration_factor = 700;

void setup() {
  Serial.begin(115200);
  scale.begin(LOADCELL_DOUT_PIN,LOADCELL_SCK_PIN);
  scale.set_scale(calibration_factor);
  scale.tare();
  delay(3000);

}

void loop() {
  Serial.println(scale.read());

}
