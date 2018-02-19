import RPi.GPIO as GPIO
import time
import os
import subprocess
#import uuid

GPIO.setmode(GPIO.BCM)

GPIO.setup(18,GPIO.IN)

directory = '/home/pi/photobooth/pictures'

while True:
    if (GPIO.input(18)):
        os.system('sudo killall fbi')
        os.system('clear')
        os.system('fbi -T 1 -a -t 1 -1 -noverbose /home/pi/photobooth/img/4.jpg /home/pi/photobooth/img/3.jpg /home/pi/photobooth/img/2.jpg /home/pi/photobooth/img/1.jpg /home/pi/photobooth/img/cheers.jpg')
        time.sleep(2)
        os.system('clear')
        #unique_number = uuid.uuid4()
        number_of_files = len([item for item in os.listdir(directory) if os.path.isfile(os.path.join(directory, item))])
        number = str(number_of_files + 1)
        cmd = "gphoto2 --capture-image-and-download --filename /home/pi/photobooth/pictures/photobooth\"{0}\".jpg --no-keep".format(number)
        #os.system(cmd)
        gpout = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True)
        print(gpout)
        os.system('clear')
        showfoto = "fbi -T 1 -t 7 -1 -a -noverbose /home/pi/photobooth/pictures/photobooth\"{0}\".jpg".format(number)
        os.system(showfoto)
        time.sleep(7)
        os.system('sudo killall gphoto2')
        os.system('clear')
        os.system('sudo killall fbi')
        os.system('fbi -T 1 -t 1 -a -noverbose /home/pi/photobooth/img/start.jpg')
    time.sleep(0)