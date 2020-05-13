#include <Arduino.h>

#include <Adafruit_NeoPixel.h>

#define PIN 6
#define NUMPIXELS 70 // Popular NeoPixel ring size
#define BRIGHTNESS 80
const int ledPin = 13; // the pin that the LED is attached to      // a variable to read incoming serial data into
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
#define DELAYVAL 25


void parseCommand(int incomingBytes[9]);

void setup()
{
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
  pixels.setBrightness(65);
}

void loop()
{
  // see if there's incoming serial data:
  if (Serial.available() >= 9)
  {
    int incomingBytes[9];

    for (int i = 0; i < 9; i++) {
      incomingBytes[i] = Serial.read();
    }

    parseCommand(incomingBytes);
  }
}

/*
* This function parses the incoming bytes and lits the correct leds
*/
void parseCommand(int incomingBytes[9])
{
  uint32_t color1 = pixels.Color(incomingBytes[0], incomingBytes[1], incomingBytes[2], 0);
  uint32_t color2 = pixels.Color(incomingBytes[3], incomingBytes[4], incomingBytes[5], 0);
  uint32_t color3 = pixels.Color(incomingBytes[6], incomingBytes[7], incomingBytes[8], 0);

  pixels.fill(color1, 0, 10);
  pixels.fill(color2, 11, 20);
  pixels.fill(color3, 21, 30);
  pixels.show();
}