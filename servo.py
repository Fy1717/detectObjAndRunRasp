import RPi.GPIO as GPIO
import time

servo1 = 5
servo2 = 6
servo3 = 13
servo4 = 19

GPIO.setmode(GPIO.BOARD)

GPIO.setup(servo1, GPIO.OUT)
GPIO.setup(servo2, GPIO.OUT)
GPIO.setup(servo3, GPIO.OUT)
GPIO.setup(servo4, GPIO.OUT)
   

def rotate(servo, degree):
   servo.start(2.5)

   try:      
      servo.ChangeDutyCycle(degree)
      time.sleep(1)
            
   except KeyboardInterrupt:
      GPIO.cleanup()

def setStartPosition():
    rotate(servo1, 120) 
    rotate(servo2, 30) 
    rotate(servo3, 90)
    rotate(servo4, 90)

setStartPosition()

def runServo(xLocation, yLocation):
   degree1 = 10  #xLocation / 2 + yLocation / 2
   degree2 = 45  #xLocation / 2 + yLocation / 2
   degree3 = 80  #xLocation / 2 + yLocation / 2
   degree4 = 120 #xLocation / 2 + yLocation / 2

   servo1 = GPIO.PWM(servo1, degree1)
   rotate(servo1, degree1) # degree -> hertz

   time.sleep(1)

   servo2 = GPIO.PWM(servo2, degree2)
   rotate(servo2, degree2)

   time.sleep(1)

   servo3 = GPIO.PWM(servo3, degree3)
   rotate(servo3, degree3)

   time.sleep(1)

   servo4 = GPIO.PWM(servo4, degree4)
   rotate(servo4, degree4)

   