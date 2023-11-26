import RPi.GPIO as GPIO
from time import sleep
import pygame
import time
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("/home/codie/Desktop/RaspberryPi-alarm/EarlyRiser.mp3")
#pygame.mixer.music.play()


yellowLed = 17
BUTTON_PIN = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

blinking = False

def button_callback(channel):
	global blinking
	blinking = not blinking
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
	else:
		pygame.mixer.music.play()
	
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
	while True:
		if blinking:
			print('press')
			GPIO.output(yellowLed, GPIO.HIGH)
			sleep(1)
			GPIO.output(yellowLed, GPIO.LOW)
			sleep(1)

		else:
			GPIO.output(yellowLed,GPIO.LOW)
			sleep(.1)
except KeyboardInterrupt:
			
	GPIO.cleanup()
