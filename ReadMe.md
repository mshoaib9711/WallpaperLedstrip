# WallpaperLEDProject
This is a simple yet cool project that came to my mind in sleep. This project allows ambient lighting around your desk setup to match your wallpaper. So if you are looking to level up your desk setup apart from just getting some mainstream LED strips, this your project to jump in. 
## Getting Started
To get this up and running you will need quite a few basic hardware products that shouldn't cost you much for what the project is worth.
### Prerequisites
* Arduino Uno/Nano/Mega etc
* WS2812 LED strip
* 5V 2A adapter (Commonly can be found with Samsung charging bricks)

### Installation 
Before we jump straight into usage, we will need to install few pieces  of software to get this up and running. 

#### Installing Python
We will first be needing to install the latest version of [Python](https://www.python.org/downloads/).
#### Installing Arduino IDE
After installing python we then need to install [Arduino IDE](https://www.arduino.cc/en/Main/Software/).
Once done, we can now plug in our Arduino board which is ready to roll. 
## Setting Up
This is where we will be getting down and dirty, just kidding. We will need to make a few simple connections and install few libraries that make this project work as intended.
### Connections
![ALT](/Ledsetup.PNG)<br>
Here are the simple connections you will be needing to get the Arduino and LED strip ready.
### Python Libraries
Apart from using the in-built packages from python, we make use of 'PIL' package that needs to be installed on your PC. To do that we use this command in the terminal:
~~~
pip install Image
~~~
Or 
~~~
pip install Pillow
~~~
Once you are done with that, you can open the python script 'Wallpaperbot.py' and change the 'PATH' to your desired path of image folder.
~~~
PATH = r'C:\Users\Shoaib\Desktop\Wallpaper'
~~~
### Arduino Libraries
In the Arduino IDE from the __Sketch__ menu, > __Include Library__ > __Manage Libraries__...  In the text input box type in __"NeoPixel"__. Look for __"Adafruit NeoPixel by Adafruit"__ and select the latest version by clicking on the popup menu next to the __Install__ button. Then click on the __Install__ button. After it's installed, you can click the __"close"__ button. Next, you need to get the 'main.cpp' code on your sketch. Once you have that you can simply compile and upload the sketch to your Arduino board.<br> 
__Important Note. <br>You will need to make sure that the 'COM port' initalized in the Python script and Arduino Sketch is the same__.
On Arduino:
To check what COM port is being used, Go to __Tools__ > __Port:__ and click the one with your board name on it. <br>
On Python:
~~~
ser = serial.Serial("COM3", 115200, timeout = 1)
~~~
COM3 needs to be replaced with your corresponding COM port in use.

## Contributing

## Credits