# RaspberryPi-alarm
Group Members:
Codie Tamida

Project Name:
Raspberry Pi Alarm Clock

Hardware used:
Raspberry Pi 3
Breadboard with transistors, jumpers, led lights, and buttons
Bluetooth speaker

Software used:
Raspberry Pi OS
Python


Problems that I ran into:
I had to learn how to connect the breadboard to the Raspberry Pi 3.  And how to get a light to turn on and where to put the transistors and the in relation to the Raspberry Pi and the breadboard.  While learning how to use the GPIO pin board and where pins should go.  Also, attaching a button and the Raspberry Pi read the response from a button click. Another problem that I ran into was trying to give a button multiple uses with multiple presses.  I want the button to snooze on 1 press and if there were 2 or more presses within 3 seconds I wanted that to turn off the alarm.  But I kept running into problems because of the sleep timer stopped recording presses and therefore the button presses never got past 1 press, and the user could only snooze the alarm.  I fixed the problem by introducing a second button, one that when pressed would snooze the alarm and the other when pressed would turn off the alarm.

Programming the script was a learning curve too because I was unfamiliar with thew GPIO, pygame.mixer packages. 

What I learned from this project:
This project taught me how to program a Raspberry Pi 3 with a breadboard to read button inputs to have light changes based on button presses.  Also, I learned how to connect Raspberry Pi hardware and use it to create an “Alarm Clock”-like project and the importance of being familiar with the Raspberry Pi pin board and how make sure the elements on the breadboard interact with the Raspberry Pi and Python script.






![image](https://github.com/CodieTamida/RaspberryPi-alarm/assets/93233657/d39826ff-3f7d-4abf-b974-34f6ea252be8)
