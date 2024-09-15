from machine import Pin, PWM
import time

servo = PWM(Pin(12))
servo.freq(50)

max_duty = 65025
dig_0 = 0.0725    #0°
dig_90 = 0.12     #90°

while True:
    servo.duty_u16(int(max_duty*dig_0))
    time.sleep(1)
    servo.duty_u16(int(max_duty*dig_90))
    time.sleep(1) 
