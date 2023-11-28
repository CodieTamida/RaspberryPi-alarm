import RPi.GPIO as GPIO
from time import sleep
import pygame
import time
from datetime import datetime

# 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

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("/home/codie/Desktop/RaspberryPi-alarm/EarlyRiser.mp3")


yellowLed = 17
SNOOZE_PIN = 16
STOP_PIN = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(SNOOZE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(STOP_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

alarm_on = True

def snooze_button(channel):
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
		print("The Alarm is Snoozed")
		time.sleep(15)
		if alarm_on:
			pygame.mixer.music.play()
			
def stop_button(channel):
	global alarm_on
	pygame.mixer.music.stop()
	alarm_on = False
	print("The alarm has been shut off")
	
GPIO.add_event_detect(SNOOZE_PIN, GPIO.FALLING, callback=snooze_button, bouncetime=200)
GPIO.add_event_detect(STOP_PIN, GPIO.FALLING, callback=stop_button, bouncetime=200)


def alarm_start_time(scheduled_time):
	global alarm_on
	while True:
		current_time = datetime.now()
		if current_time.hour == scheduled_time.hour and current_time.minute == scheduled_time.minute and alarm_on:	
			pygame.mixer.music.play()
			break
		time.sleep(1)
		
scheduled_time = datetime.now().replace(hour =22, minute = 25, second = 20, microsecond = 0)

def blinking_light():
	while True:
		GPIO.output(yellowLed, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(yellowLed, GPIO.LOW)
		time.sleep(1)

try:
	alarm_start_time(scheduled_time)
	blinking_light()
	
	while alarm_on:
		time.sleep(.1)
	
except KeyboardInterrupt:
			
	GPIO.cleanup()
