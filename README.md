# Dynamic NeoPixel Desk Lights
This program examines an electronically stored image (i.e. video game artwork or movie poster) and cycles through the most popular colors on a NeoPixel LED strip. It is recommended to attach the NeoPixel LED strip to the back of a desk to use as mood lighting.

## Necessary Supplies
* Raspberry Pi ([2](https://www.adafruit.com/product/2358) or [3](https://www.adafruit.com/product/3055)) Model B 
* [Adafruit NeoPixel Digital RGB LED Strip - 30 LED](https://www.adafruit.com/product/1460)
* [Female DC Power adapter - 2.1mm jack to screw terminal block](https://www.adafruit.com/product/368)
* [5V 2A (2000mA) switching power supply](https://www.adafruit.com/product/276)
* [2-pin JST SM Plug + Receptacle Cable Set](https://www.adafruit.com/product/2880)
* [74AHCT125 - Quad Level-Shifter](https://www.adafruit.com/product/1787)
* [Adafruit Pi Cobbler + Kit- Breakout Cable for Pi B+/A+/Pi 2/Pi 3](https://www.adafruit.com/product/1990)
* Breadboard and Jumper Wires

## Hardware setup
Follow the guide provided at the Adafruit page of [NeoPixels on Raspberry Pi](https://learn.adafruit.com/neopixels-on-raspberry-pi/wiring) for wiring the NeoPixel LED strip correctly to the Raspberry Pi

## Software Installation
First, make sure to follow the steps for installing the __rpi_ws281x Library__ and __Python__ using the instructions found on the [Adafruit NeoPixel Software page](https://learn.adafruit.com/neopixels-on-raspberry-pi/software)

Next, install the SimpleCV library by following these [instructions](http://simplecv.readthedocs.io/en/latest/HOWTO-Install%20on%20RaspberryPi.html).

## Program Usage
To execute the LED program, run led_main.py with the image file defined as a command line argument as follows:

```bash
python led_main.py sample_images/shovel_knight
```
Note: You may have to run this command as super user (i.e. sudo).

Once this command executes, the program will take a moment to process the image and then the LEDs will display a starting color and slowly transition to new colors. Throughout this program, all 30 LEDS display the same color at a time. Additionally, the terminal continually displays the RGB values for the current color and the target color.

In order to close the program, use __ctrl + c__. Upon doing so, the LEDs will turn off and a message will apear in the terminal indicating that the program was terminated successfully.

## Contact:
David J. Glowny
djglowny@gmail.com