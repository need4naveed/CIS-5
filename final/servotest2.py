# use this custom pin-factory to fix servo jitter. 
# IMPORTANT: make sure pigpio deamon is running: 'sudo pigpiod'
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Servo
from time import sleep

pigpio_factory = PiGPIOFactory()

servo = Servo(11, pin_factory=pigpio_factory)
servo.mid()
print("servo mid")
sleep(3)

while True:
  servo.min()
  print("servo min")
  sleep(3)

  servo.mid()
  print("servo mid")  
  sleep(3)

  servo.max()
  print("servo max")
  sleep(3)