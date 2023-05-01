int sensorPin = A5; // Sensörün bağlı olduğu pin
float voltage = 0; // Sensör çıkış voltajı
float humidity = 0; // Nem oranı

void setup() {
  Serial.begin(9600); // Seri haberleşmeyi başlat
  pinMode(sensorPin, INPUT); // Sensör pinini giriş olarak ayarla
}

void loop() {
  voltage = analogRead(sensorPin) * 5.0 / 1023.0; // Sensör çıkış voltajını ölç
  humidity = (voltage - 0.8) * 50.0; // Nem oranını hesapla (referans voltaj 0.8 V)
  Serial.print(humidity); // Sadece nem oranını seri port üzerinden gönder
  Serial.println();
  delay(1000); // 1 saniye bekle

}
