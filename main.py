import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
i=2

while True:
    if i>10:
        break
    GPIO.setup(i,GPIO.OUT)	
    GPIO.output(i,GPIO.LOW)
    i+=1
while True:
    if i==0:
        break
    GPIO.setup(i,GPIO.OUT)	
    GPIO.output(i,GPIO.HIGH)
    time.sleep(0.25)
    i-=1
while True:
    if i>10:
        break
    GPIO.setup(i,GPIO.OUT)	
    GPIO.output(i,GPIO.LOW)
    time.sleep(0.25)
    i+=1

def int2bin (i):
    if i==0 :return "0"
    s=''
    while i:
        if i&1:
            s="1"+s
        else:
            s="0"+s
        i/=2
    print len(s)
    return s

def cleanup():
    z=2
    while True:
        if z>10:
            break
        GPIO.setup(z,GPIO.OUT)	
        GPIO.output(z,GPIO.LOW)
        z+=1
        
def reve(a_string):
    return a_string[::-1]

while True:
    try:
        i=int(raw_input("Enter an integer: "))
        
        if (i >= 256 or i < 0):
            continue
        a = int2bin(i)
        cleanup()
        print a
        a = reve(a)
        j=0
        while j<len(a):
            if a[j]=="1":
                GPIO.setup(j+2,GPIO.OUT)	
                GPIO.output(j+2,GPIO.HIGH)
            else:
                GPIO.setup(j+2,GPIO.OUT)	
                GPIO.output(j+2,GPIO.LOW)
            j+=1
        
    except:
        continue
'''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)	
GPIO.output(14,GPIO.HIGH)	
GPIO.setup(15,GPIO.OUT)	
GPIO.output(15,GPIO.HIGH)
'''
