import RPi.GPIO as GPIO
import time
import nexmo

GPIO.setmode(GPIO.BOARD)

client = nexmo.Client(key="f799075d",secret='hy2CiHd87DTDXjxy')
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
#left_vibration_motor = 14

gps_switch = 33




print("Distance Measurement In Progress")

GPIO.setwarnings(False)

GPIO.setup(F_TRIG,GPIO.OUT)
GPIO.setup(F_ECHO,GPIO.IN)
GPIO.setup(L_TRIG,GPIO.OUT)
GPIO.setup(L_ECHO,GPIO.IN)
GPIO.setup(R_TRIG,GPIO.OUT)
GPIO.setup(R_ECHO,GPIO.IN)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(13,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(gps_switch,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(right_vibration_motor,GPIO.OUT)
GPIO.setup(left_vibration_motor,GPIO.OUT)

def calculate_distance(pulse_start,pulse_end):
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150
  distance = round(distance,2)
  return distance

def send_msg():
  client.send_message({
    'from':'Nexmo',
    'to':'918766875503',
    'text':'There is a emergency. The current GPS coordinates are : 20°00\'59.5"N 73°45\'22.0"E',

    })
  return
    
GPIO.output(buzzer,False)
GPIO.output(F_TRIG, False)
GPIO.output(R_TRIG, False)
GPIO.output(L_TRIG, False)
GPIO.output(right_vibration_motor,False)
GPIO.output(left_vibration_motor,False)
print("Waiting For Sensor To Settle")
time.sleep(2)



while True:
  
  main_switch_input = GPIO.input(13)
  #GPIO.output(right_vibration_motor,False)


  if main_switch_input == False:
    GPIO.output(F_TRIG, True)
    time.sleep(0.0001)
    GPIO.output(F_TRIG, False)


    while GPIO.input(F_ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(F_ECHO)==1:
      pulse_end = time.time()

    GPIO.output(R_TRIG, True)
    time.sleep(0.0001)
    GPIO.output(R_TRIG, False)
    

    while GPIO.input(R_ECHO)==0:
      R_pulse_start = time.time()

    while GPIO.input(R_ECHO)==1:
      R_pulse_end = time.time()

    GPIO.output(L_TRIG, True)
    time.sleep(0.0001)
    GPIO.output(L_TRIG, False)
    

    while GPIO.input(L_ECHO)==0:
      L_pulse_start = time.time()

    while GPIO.input(L_ECHO)==1:
      L_pulse_end = time.time()

    front_distance = calculate_distance(pulse_start,pulse_end)
    right_distance = calculate_distance(R_pulse_start,R_pulse_end)
    left_distance = calculate_distance(L_pulse_start,L_pulse_end)

    if(front_distance <= 60):
      GPIO.output(29,True)
    elif(left_distance <=50):
      GPIO.output(left_vibration_motor,True)
    elif(right_distance <= 50):
      GPIO.output(right_vibration_motor,True)
    else:
      GPIO.output(buzzer,False)
      GPIO.output(right_vibration_motor,False)
      GPIO.output(left_vibration_motor,False)
      
      

      
    
    print("F_Distance:",front_distance,"cm")
    #print("R_Distance:",right_distance,"cm")
    #print("L_Distance:",left_distance,"cm")
    gps_switch_state = GPIO.input(gps_switch)
    if(gps_switch_state == False):
      try:
        
        print("GPS SEND")
        client.send_message({
    'from':'Nexmo',
    'to':'918766875503',
    'text':'There is a emergency. The current GPS coordinates are : 20.013328, 73.822564 . Get Location by searching Coordinates at https://www.google.co.in/maps',

        })
      except:
        continue
  else:
   # print("Main switch off")
    GPIO.output(right_vibration_motor,False)
    GPIO.output(left_vibration_motor,False)
    GPIO.output(buzzer,False)

GPIO.cleanup()
