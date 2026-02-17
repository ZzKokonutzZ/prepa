#include "HX711.h"

HX711 scale;
const uint8_t dataPin = 2;
const uint8_t clockPin = 3;

// Lit la moyenne de 'n' lectures. Retourne true si au moins 1 lecture valide.
// La valeur moyenne est placée dans 'out'.
bool readAverage(int n, long &out) {
  long sum = 0;
  int valid = 0;
  for (int i = 0; i < n; i++) {
    // attend que le module soit prêt (timeout 500 ms)
    if (!scale.wait_ready_timeout(500)) {
      // pas prêt -> on saute cette itération
      Serial.print("[!] wait_ready timeout pour lecture ");
      Serial.println(i);
      delay(10);
      continue;
    }
    long r = scale.read();
    // détecter les saturations 24 bits typiques
    if (r == 8388607L || r == -8388608L) {
      Serial.print("[!] lecture saturée (24-bit) idx=");
      Serial.println(i);
      continue;
    }
    sum += r;
    valid++;
    delay(5);
  }
  if (valid == 0) {
    return false; // aucune lecture valide
  }
  out = sum / valid;
  return true;
}

void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("Test HX711 - démarrage");
  scale.begin(dataPin, clockPin);

  // attente stabilisation
  Serial.println("Attente stabilisation 2s...");
  delay(2000);

  // Tare si possible
  Serial.println("Tare...");
  if (scale.wait_ready_timeout(2000)) {
    scale.tare();
    Serial.println("Tare OK");
  } else {
    Serial.println("Tare: module non prêt !");
  }
}

void loop() {
  long raw;
  bool ok = readAverage(5, raw);

  Serial.print("is_ready=");
  Serial.print(scale.is_ready() ? "1" : "0");
  Serial.print("  ");

  if (!ok) {
    Serial.println("Aucune lecture valide (toutes saturées ou timeout).");
  } else {
    Serial.print("raw moyenne=");
    Serial.print(raw);
    // détecter si la valeur est extrême (au cas où)
    if (raw == 8388607L || raw == -8388608L) {
      Serial.print("  <-- SATURATION 24-bit");
    }
    Serial.println();
  }

  delay(300);
}