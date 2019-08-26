import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

F_TRIG = 16
F_ECHO = 18

L_TRIG = 40
L_ECHO = 38

R_TRIG = 37
R_ECHO = 35

main_switch = 13
#main_switch_gnd = 9

buzzer = 29


right_vibration_motor = 22
#right_vibration_motor_gnd = 30

left_vibration_motor = 32


GPIO.setup(F_TRIG,GPIO.OUT)
GPIO.setup(F_ECHO,GPIO.IN)
GPIO.setup(L_TRIG,GPIO.OUT)
GPIO.setup(L_ECHO,GPIO.IN)
GPIO.setup(R_TRIG,GPIO.OUT)
GPIO.setup(R_ECHO,GPIO.IN)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(right_vibration_motor,GPIO.OUT)
GPIO.setup(left_vibration_motor,GPIO.OUT)

#GPIO.cleanup()


GPIO.output(buzzer,False)
GPIO.output(F_TRIG, False)
GPIO.output(R_TRIG, False)
GPIO.output(L_TRIG, False)
GPIO.output(right_vibration_motor,False)
GPIO.output(left_vibration_motor,False)
