# WallpaperLEDProject
This is a simple yet cool project that came to my mind in sleep. This project allows ambient lighting around your desk setup to match your wallpaper. So if you are looking to level up your desk setup apart from just getting some mainstream LED strips, this your project to jump in. <br>

![ALT](ezgif.com-video-to-gif.gif)
## Getting Started
To get this up and running you will need quite a few basic hardware products that shouldn't cost you much for what the project is worth.
### Prerequisites
* Arduino Uno/Nano/Mega etc
* WS2812 LED strip
* 5V 2A adapter (Commonly can be found with Samsung charging bricks)

## Installation 
Before we jump straight into usage, we will need to install few pieces  of software to get this up and running. 

### Installing Python
So if you don't already have Python installed on your PC we will first be needing to install the latest version  from [here](https://www.python.org/downloads/).
### Installing Arduino IDE
And for those who don't have Arduino IDE installed we then would need to install [Arduino IDE](https://www.arduino.cc/en/Main/Software/).
Once done, we can now plug in our Arduino board which is ready to roll. 
## Setting Up
Ok, this is where we will be getting down and dirty, just kidding. We will simply need to make a few easy connections and install few libraries that make this project work as intended.
### Connections
![ALT](/Ledsetup.PNG)<br>
Here are the simple connections you will be needing to get the Arduino and LED strip ready. Notice that the DC barrel jack only represents a 5V 2A power source. 
### Python Libraries
Apart from using the in-built packages from python, we make use of 'PIL' package that needs to be installed on your PC. To do that we use this command in the terminal:
~~~
pip install Image
~~~
Or 
~~~
pip install Pillow
~~~
Once you are done with that, you can open the python script __python Wallpaperbot.py and change the 'PATH' to your desired path of image folder.
~~~
PATH = r'C:\Users\Shoaib\Desktop\Wallpaper'
~~~
### Arduino Libraries
In the Arduino IDE from the __Sketch__ menu, > __Include Library__ > __Manage Libraries__...  In the text input box type in __"NeoPixel"__. Look for __"Adafruit NeoPixel by Adafruit"__ and select the latest version by clicking on the popup menu next to the __Install__ button. Then click on the __Install__ button. After it's installed, you can click the __"close"__ button. Next, you need to get the 'WallpaperLedstrip.ino' code on your sketch. Once you have that you can simply compile and upload the sketch to your Arduino board.<br> 
__Important Note. <br>You will need to make sure that the 'COM port' initalized in the Python script and Arduino Sketch is the same__.
On Arduino:
To check what COM port is being used, Go to __Tools__ > __Port:__ and click the one with your board name on it. <br>
On Python:
~~~
ser = serial.Serial("COM3", 115200, timeout = 1)
~~~
COM3 needs to be replaced with your corresponding COM port in use. <br> Then you can simply run the python script with the Arduino and see the output for yourself. To close the program use __CRTL+C__. <br>
You can change the speed of the program to your liking by tweaking in python script.
 ~~~
 time.sleep()
 ~~~

## Contributing
I truly believe there great scope in the future for this project as we have already began working on making this work for videos/games. <br> So if you wish to contribute with a great idea of yours and want to directly work/help with us, you can send a pull-request to us. Anyone can feel free to submit issues and enhancement requests. <br> 
### PlatformIO
We use PlatformIO extension on vscode for its superior embedded development experience compared to Arduino IDE. The configuration defaults example is as follows:
~~~
[env:uno]
platform = atmelavr
board = uno
framework = arduino

lib_extra_dirs = c:/Users/masha/Documents/Arduino/libraries, c:/Program Files (x86)/arduino/libraries
monitor_speed = 115200
build_flags = -Wunknown-pragmas
upload_port = COM5
~~~
This is an example and you will have to customize the 'board', 'lib_extra_dirs' and 'upload_port' for your own PC and hardware used. 
 __platformio.ini__ file. <br>


## Credits and Support 
If you find our project fun and wish to support us, you can help at [buymeacoffe](https://www.buymeacoffee.com/mshoaib9711) or at the least star our project to help motivate us and keep us going. This is only my first project and I wish to make many more fun open source projects in the coming future. Cheers!
<br>
* Contributors: [mshoaib9711](https://github.com/mshoaib9711), [Panalgin](https://github.com/panalgin), [Shahlin Ibrahim](https://github.com/shahlin).