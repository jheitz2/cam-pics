# Alex N.
# Wildlife Camera
# 3 / 13 / 18
# This is the program for my wildlife camera. It can turn on and off with the press of a button and can take pictures of animals automatically.

# Importing my stuff
from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep

# Setting variables
camera = PiCamera()
GPIO.setmode(GPIO.BCM)
LED = 21
button = 19
PIR = 12
on = False
images = 1
IRs = [4, 5, 6, 7, 8, 9, 10, 11, 13]

# Setting up GPIO
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(PIR, GPIO.IN)
GPIO.setup(button, GPIO.IN)
GPIO.output(LED, GPIO.LOW)
for IR in IRs:
    GPIO.setup(IR, GPIO.OUT)
    GPIO.output(IR, GPIO.LOW)

# Start a loop
while True:
    if on == True:
        GPIO.output(LED, GPIO.HIGH)
        for IR in IRs:
            GPIO.output(IR, GPIO.HIGH)
        for i in range(100):
            sleep(0.05)
            # Checking if the button is pressed while the program is waiting
            if GPIO.input(button):
                on = False
                GPIO.output(LED, GPIO.LOW)
                sleep(1)
                break
        if on == True and GPIO.input(PIR):
            # Code for taking a picture (very simple)
            try:
                sleep(0.2)
                camera.capture("/home/pi/cam-pics/Pictures/image%03d.jpg" % images)
                images += 1
            except:
                # If it (somehow) failed to take a picture, it gives this message and the light blinks:
                print("Sorry, something went wrong.")
                for ERROR_NOOO in range(5):
                    GPIO.output(LED, GPIO.LOW)
                    sleep(0.5)
                    GPIO.output(LED, GPIO.HIGH)
                    sleep(0.5)
    else:
        GPIO.output(LED, GPIO.LOW)
        for IR in IRs:
            GPIO.output(IR, GPIO.LOW)
        if GPIO.input(button):
            on = True
            GPIO.output(LED, GPIO.HIGH)
            sleep(1)
