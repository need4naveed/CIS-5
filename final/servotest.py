from gpiozero import Servo
from time import sleep

servo = Servo(11)

while True:
    servo.min()
    sleep(0.5)
    servo.mid()
    sleep(0.5)
    servo.max()
    sleep(0.5)
