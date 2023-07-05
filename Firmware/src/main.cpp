#include <Arduino.h>
#include "NeuralNetwork.h"
#include "model_data.h"

#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

NeuralNetwork *nn;
const char* ssid = "custodma_2G";
const char* password = "berserknd";
const char* serverUrl = "http://150.162.235.79:5000/data";

void setup()
{
  Serial.begin(115200);
  nn = new NeuralNetwork(converted_model_tflite);

  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  
  Serial.println("Connected to WiFi");
}

void loop()
{
  float number1 = random(100) / 100.0;
  float number2 = random(100) / 100.0;

  nn->getInputBuffer()[0] = number1;
  nn->getInputBuffer()[1] = number2;

  float result = nn->predict();

  const char *expected = number2 > number1 ? "True" : "False";

  const char *predicted = result > 0.5 ? "True" : "False";

  Serial.printf("%.2f %.2f - result %.2f - Expected %s, Predicted %s\n", number1, number2, result, expected, predicted);

  // Crie um objeto JSON e adicione os dados que deseja enviar
  StaticJsonDocument<200> jsonDocument;
  jsonDocument["sensor"] = "ESP32";
  jsonDocument["value"] = random(10);
  
  // Converta o objeto JSON em uma string
  String jsonString;
  serializeJson(jsonDocument, jsonString);

  // Crie uma instância do objeto HTTPClient
  HTTPClient http;
  
  // Faça uma requisição POST para o servidor com os dados JSON
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/json");
  int httpResponseCode = http.POST(jsonString);
  
  // Verifique a resposta do servidor
  if (httpResponseCode == HTTP_CODE_OK) {
    String response = http.getString();
    Serial.println("Data sent successfully");
    Serial.println("Server response: " + response);
  } else {
    Serial.print("Error sending data. HTTP response code: ");
    Serial.println(httpResponseCode);
  }
  
  // Libere os recursos
  http.end();

  delay(5000);
}