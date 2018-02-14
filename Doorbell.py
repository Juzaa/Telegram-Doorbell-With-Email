import RPi.GPIO as GPIO
from time import sleep
from os import system
from pygame import mixer
import logging
import telegram
import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("SENDER-EMAIL", "PASSWORD")

ledPin = 20

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s – %(name)s – %(levelname)s – %(message)$')
bot = telegram.Bot(token='TELEGRAM-BOT-TOKEN-HERE')

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

try:
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            bot.sendMessage(chat_id=-CHAT-TOKEN-HERE,
            text="Ovella on joku!")
            msg = "Ovella on joku!"
            server.sendmail("SENDER-EMAIL-HERE", "RECEIVER-EMAIL-HERE", msg)
            #server.quit()
            GPIO.output(ledPin, GPIO.HIGH)
            sleep(1.0)
            GPIO.output(ledPin, GPIO.LOW)
            
            continue

            sleep(1.0)

            sleep(0.1)
            

finally:
    bot.sendMessage(chat_id=-1001261581372,
    text="Ovikello on pois päältä!")
    GPIO.cleanup()
