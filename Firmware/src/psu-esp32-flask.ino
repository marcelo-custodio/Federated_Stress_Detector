#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

// define as credenciais da rede WiFi
const char* ssid = "Rodrigo";
const char* password = "rodrigo0311";

// endereço do servidor Flask p GET
const char* getServerAddress = "http://192.168.2.18:5000/random_data";

// endereço do servidor Flask p POST
const char* postServerAddress = "http://192.168.2.18:5000/other_endpoint";

void setup() {
  Serial.begin(115200);

  // conecta WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // solicitação GET p servidor Flask
  HTTPClient http;
  http.begin(getServerAddress);

  int httpResponseCode = http.GET();
  if (httpResponseCode == 200) {
    String response = http.getString();
    Serial.println("Received random data: " + response);

    // envia os dados para a segunda URL como JSON usando POST
    // para nao ter nenhum problema entre o GET e o POST, foi melhor criar duas URL
    http.begin(postServerAddress);
    http.addHeader("Content-Type", "application/json");

    // construir o payload JSON com os dados recebidos
    DynamicJsonDocument jsonDoc(256);
    jsonDoc["value"] = response.toInt();

    String payload;
    serializeJson(jsonDoc, payload);

    int httpResponseCode = http.POST(payload);
    if (httpResponseCode == 200) {
      Serial.println("Data sent successfully");
    } else {
      Serial.print("Failed to send data, response code: ");
      Serial.println(httpResponseCode);
    }

    http.end();
  } else {
    Serial.print("Request failed, response code: ");
    Serial.println(httpResponseCode);
  }

  http.end();

  // delay normal
  delay(5000); // Aguardar 5 segundos
}
