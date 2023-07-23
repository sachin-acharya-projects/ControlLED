// Importing Library
#include <ESP8266WiFi.h>

// Constants
int BAUDRATE = 115200;
int PORT = 80;
int ON = 1;
int OFF = 0;
const int PIN = BUILTIN_LED;

// WiFi Credentials
const char *SSID = "WIFI_SSID";
const char *PASSWORD = "WIFI_PASSWORD";

// Defining WiFiServer with PORT 80
WiFiServer server(PORT);

void setup()
{
    // Assigning OUTPUT pin
    pinMode(PIN, OUTPUT);

    // Starting Serial Connection
    Serial.begin(BAUDRATE);

    // Connecting to WiFi Network
    Serial.println(String("\nConnecting to WiFi Network (") + SSID + String(")"));
    WiFi.mode(WIFI_STA);
    WiFi.begin(SSID, PASSWORD);

    // Looping until WiFi connects
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println("\nConnected to WiFi network");
    // Print Local IP of Microcontroller
    Serial.println(String("IP ") + WiFi.localIP().toString());
    // Starting WiFi server
    server.begin();
    delay(1000);
}

void send_response(WiFiClient client, String str)
{
    // Sending Response Status (200)
    client.println("HTTP/1.1 200 OK");
    // Header ContentType - text/plain or text/html (others too)
    client.println("Content-Type: text/plain");
    // Require line-break
    client.println();
    // Can contain full html string
    client.println(str);
}

void loop()
{
    // Defining WiFiClient
    WiFiClient client;
    client = server.available(); // Available Client

    if (client)
    {
        // Waiting for client to send data
        while (client.connected() && !client.available())
            delay(1);

        // Reading Requested Parameter
        String request = client.readStringUntil('\n');
        int parameter = request.indexOf("GET /");
        if (parameter != -1)
        {
            int parameter_index = parameter + sizeof("GET /") - 1;
            int parameter_value = (int)request.substring(parameter_index, parameter_index + 1).toInt();

            Serial.println(String("Received ") + String(parameter_value));
            /*
             * Note that the 'LOW' is the voltage level but actually the LED
             * is on; this is because it is active low on the ESP8266.
             */
            if (parameter_value == ON)
            {
                digitalWrite(PIN, LOW);
                Serial.println("LED has TURNED ON");
                send_response(client, String("ON"));
            }
            else
            {
                digitalWrite(PIN, HIGH);
                Serial.println("LED has TURNED OFF");
                send_response(client, String("OFF"));
            }
            client.flush();
        }
    }
}