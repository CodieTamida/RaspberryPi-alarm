import RPi.GPIO as GPIO
from time import sleep
import pygame
import time
from datetime import datetime


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
alarm_on = True


def button_press(channel):
	global button_press_count, last_press, alarm_on
	
	if last_press and (datetime.now() - last_press).total_seconds() < 4:
		button_press_count += 1
	else:
		button_press_count =  1
		
	last_press = datetime.now()
	
	print("this is count before sleep: ", button_press_count)
	print(button_press_count)
	if button_press_count == 1:
		print(pygame.mixer.music.get_busy())
		if pygame.mixer.music.get_busy():
			print(pygame.mixer.music.get_busy())
			pygame.mixer.music.stop()
			print("Alarm is Stopped, detecting Snoze or Off")
			time.sleep(15)
			if alarm_on:
				pygame.mixer.music.play()

	elif button_press_count > 1:
		pygame.mixer.music.stop()
		alarm_on = False
		print("Alarm is Stopped")

	print("does the function end")
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=button_press, bouncetime=500)

def alarm_start_time(scheduled_time):
	global alarm_on
	while True:
		current_time = datetime.now()
		if current_time.hour == scheduled_time.hour and current_time.minute == scheduled_time.minute and alarm_on:	
			pygame.mixer.music.play()
			break
		time.sleep(1)
		
scheduled_time = datetime.now().replace(hour =18, minute = 59, second = 20, microsecond = 0)

def blinking_light():
	while True:
		GPIO.output(yellowLed, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(yellowLed, GPIO.LOW)
		time.sleep(1)

try:
	alarm_start_time(scheduled_time)
	blinking_light()
except KeyboardInterrupt:
			
	GPIO.cleanup()
