#include <Adafruit_NeoPixel.h>
#include <Arduino.h>

#define PIN 6
#define NUMPIXELS 70  // Popular NeoPixel ring size
#define BRIGHTNESS 80
const int ledPin = 13;  // the pin that the LED is attached to      // a
                        // variable to read incoming serial data into
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
#define DELAYVAL 25

void parseCommand(String command);
String splitValues(String data, char delimiter, uint8_t index);

void setup() {
    // initialize serial communication:
    Serial.begin(115200);
    // initialize the LED pin as an output:
    pinMode(ledPin, OUTPUT);
    pixels.begin();  // INITIALIZE NeoPixel strip object (REQUIRED)
    pixels.setBrightness(80);
}

String incomingData = "";

void loop() {
    while (Serial.available()) {
        char c = Serial.read();

        if (c != '\n')
            incomingData += c;
        else {
            parseCommand(incomingData);

            incomingData = "";
        }
    }
}

/*
 * This function parses the incoming command string and lits the correct leds
 */
void parseCommand(String cmd) {
    uint32_t color1 = splitValues(cmd, ',', 0).toInt() >> 8;
    uint32_t color2 = splitValues(cmd, ',', 1).toInt() >> 8;
    uint32_t color3 = splitValues(cmd, ',', 2).toInt() >> 8;

    Serial.print("Color[1]: "); Serial.println(color1);
    Serial.print("Color[2]: "); Serial.println(color2);
    Serial.print("Color[3]: "); Serial.println(color3);

    pixels.fill(color1, 0, 24);
    pixels.fill(color2, 24, 48);
    pixels.fill(color3, 48, 70);

    pixels.show();
}

// Splits a delimited string and returns the index positioned value as String
String splitValues(String data, char delimiter, uint8_t index) {
    int found = 0;
    int strIndex[] = {0, -1};
    int maxIndex = data.length() - 1;

    for (int i = 0; i <= maxIndex && found <= index; i++) {
        if (data.charAt(i) == delimiter || i == maxIndex) {
            found++;
            strIndex[0] = strIndex[1] + 1;
            strIndex[1] = (i == maxIndex) ? i + 1 : i;
        }
    }

    return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
};