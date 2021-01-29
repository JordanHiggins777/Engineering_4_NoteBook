from gpiozero import LED
from time import sleep

led1 = LED(17)

while True:
	led1.on()
	sleep(0.5)
	led1.off()
	sleep(0.5)
