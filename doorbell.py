# -*- coding: utf-8 -*-
# I/O sekä aikafunktio viiveelle, äänikirjasto ja systeemikomennot
import RPi.GPIO as GPIO
from time import sleep
from os import system
from pygame import mixer
import logging
import telegram
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("projektiraspi@gmail.com", "Anjutu2018")

ledPin = 20

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s – %(name)s – %(levelname)s – %(message)$')


bot = telegram.Bot(token='509325077:AAHHB93B5FTvhtA6Vg7tVy67g52bDlTWVLk')

# GPIO -pinnien määrittely standardiksi
GPIO.setmode(GPIO.BCM)

# Määritellään pinni 18 sisääntuloksi sekä kytketään sisäinen vastus
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

# napinpainalluksen funktio try / finally -loopilla

try:
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            bot.sendMessage(chat_id=-1001261581372,
            text="Ovella on joku!")
            msg = "Ovella on joku!"
            server.sendmail("projektiraspi@gmail.com", "t6hiju02@students.oamk.fi", msg)
            #server.quit()
            GPIO.output(ledPin, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(ledPin, GPIO.LOW)
            


        #mixer.init()
        #mixer.music.load('/home/pi/Lataukset/doorbell-1.mp3')
        #mixer.music.play()
        #while mixer.music.get_busy() == True:
            continue

            sleep(1.0)
            

# 0.1 sekunnin tauko jotta säästetään prosessorin resursseja
            sleep(0.1)
            

finally:
# Resetoidaan napin tila ja lähetetään viesti jos ovikello hyytyy
    bot.sendMessage(chat_id=-1001261581372,
    text="Ovikello on pois päältä!")
    GPIO.cleanup()
