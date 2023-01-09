// Importing required libraries
#include<ESP8266WiFi.h>

// WiFi Settings
const char* ssid = "asachin_fctwn_2";
const char* password = "CLEB12F6EF";

WiFiServer server(80);
void setup() {
  // put your setup code here, to run once:
  pinMode(BUILTIN_LED, OUTPUT);
  Serial.begin(115200);
  Serial.println("Connecting to WiFi network");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected to WiFi Network");
  Serial.println(WiFi.localIP());
  server.begin();
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  WiFiClient client;
  client = server.available();

  if (client == 1) {
    String request = client.readStringUntil('\n');
    client.flush();
    Serial.println(request);
    if (request.indexOf("ledon") != -1) {
      digitalWrite(BUILTIN_LED, LOW);
      Serial.println("LED has been turned OFF");
    } else if (request.indexOf("ledoff") != -1) {
      digitalWrite(BUILTIN_LED, HIGH);
      Serial.println("LED has been turned ON");
    }
  }
}
