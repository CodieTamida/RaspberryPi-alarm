import RPi.GPIO as GPIO
from time import sleep
import pygame
import time
from datetime import datetime, timedelta


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("/home/codie/Desktop/RaspberryPi-alarm/EarlyRiser.mp3")
#pygame.mixer.music.play()


yellowLed = 17
BUTTON_PIN = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(yellowLed, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button_press_count= 0
last_press = None
blinking = False
alarm_on = True

def button_press(channel):
	global button_press_count, last_press, alarm_on
	current_time = datetime.now()
	
	if last_press and (current_time - last_press).total_seconds() < 5:
		button_press_count += 1
	else:
		button_press_count =  1
		
	last_press = current_time
	
	if button_press_count == 1:
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.stop()
			alarm_on = False
			print("Alarm is Snoozed")
			time.sleep(15)
			alarm_on = True
			pygame.mixer.music.play()
	elif button_press_count >= 2:
		pygame.mixer.music.stop()
		alarm_on = False
		print("Alarm is Stopped")

def button_callback(channel):
	global blinking
	blinking = not blinking
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
	else:
		pygame.mixer.music.play()
	
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_press, bouncetime=200)

def alarm_start_time(scheduled_time):
	global alarm_on
	while True:
		current_time = datetime.now()
		if current_time.hour == scheduled_time.hour and current_time.minute == scheduled_time.minute:
			if not pygame.mixer.music.get_busy() and alarm_on:
				pygame.mixer.music.play()
			break
		time.sleep(1)
		
scheduled_time = datetime.now().replace(hour =17, minute = 25, second = 0, microsecond = 0)

	

try:
	alarm_start_time(scheduled_time)
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
