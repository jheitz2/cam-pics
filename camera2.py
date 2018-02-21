from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.exposure_mode ='beach'
sleep(5)
camera.capture('/home/pi/Desktop/beach.jpg')
camera.stop_preview()
