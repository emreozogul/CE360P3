#include "BluetoothSerial.h"
#include "WiFi.h"

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  if (!SerialBT.begin("ESP32EmreMeren")) {
    Serial.println("Bluetooth init failed");
  } else {
    Serial.println("Bluetooth device is ready to pair");
  }
}

void loop() {
  if (SerialBT.available()) {
    String ssid = SerialBT.readStringUntil('\n');
    String password = SerialBT.readStringUntil('\n');
    ssid.trim();
    password.trim();

    Serial.print("Received SSID: ");
    Serial.println(ssid);
    Serial.print("Received password: ");
    Serial.println(password);

    WiFi.begin(ssid.c_str(), password.c_str());

    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }

    if (WiFi.isConnected()) {
      Serial.println("WiFi connected successfully");
      SerialBT.println("WiFi connected successfully");
    } else {
      Serial.println("Failed to connect to WiFi");
      SerialBT.println("Failed to connect to WiFi");
    }
  }
  delay(20);
}
