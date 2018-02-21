from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.start_preview()
camera.image_effect='cartoon'
sleep(5)
camera.capture('/home/pi/Desktop/cartoon.jpg')
camera.stop_preview()

