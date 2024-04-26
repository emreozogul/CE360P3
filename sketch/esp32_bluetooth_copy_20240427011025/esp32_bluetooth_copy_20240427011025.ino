#include "BluetoothSerial.h"
#include "WiFi.h"

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  if (!SerialBT.begin("ESP32BT")) { // Start Bluetooth device with name "ESP32BT"
    Serial.println("Bluetooth init failed");
  }

  Serial.println("Bluetooth device is ready to pair");
}

void loop() {
  if (SerialBT.available()) {
    String ssid = SerialBT.readStringUntil('\n');
    String password = SerialBT.readStringUntil('\n');
    ssid.trim();
    password.trim();

    WiFi.begin(ssid.c_str(), password.c_str());

    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    SerialBT.println("WiFi connected");
    Serial.println("WiFi connected successfully");
  }
  delay(20);
}
