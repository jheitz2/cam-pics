# Importing my stuff
from picamera import PiCamera
import RPi.GPIO as GPIO
from time import sleep
from random import randint

# Setting variables
camera = PiCamera()
GPIO.setmode(GPIO.BCM)
LED = 21
button = 19
PIR = 12
on = False
images = 1
IRs = [4, 5, 6, 7, 8, 9, 10, 11, 13]

# Defining annotations
annotations = ["Shhhh! Come here! Look!", "I seee you!", "Look! It's a wild Brogan! Wait, that isn't a wild Brogan...", "Is that... (gasp)", "Did yo see dat?"]

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
            if GPIO.input(button):
                on = False
                GPIO.output(LED, GPIO.LOW)
                sleep(1)
                break
        if on == True and GPIO.input(PIR):
            sleep(0.2)
            camera.annotate_text = annotations[randint(0,4)]
            camera.capture("/home/pi/cam-pics/Pictures/image%s.jpg" % images)
            images += 1
            
    else:
        GPIO.output(LED, GPIO.LOW)
        for IR in IRs:
            GPIO.output(IR, GPIO.LOW)
        if GPIO.input(button):
            on = True
            GPIO.output(LED, GPIO.HIGH)
            sleep(1)
