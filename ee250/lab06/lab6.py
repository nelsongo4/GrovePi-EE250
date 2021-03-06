import requests
import sys
import time

sys.path.append('/home/pi/Dexter/GrovePi/Software/Python')

import grovepi
import grove_rgb_lcd as lcd

# Modules for my apps
import my_reddit
import my_weather
#import my_app  # TODO: Create my_app.py using another API, following the examples as a template
import my_app

PORT_BUZZER = 2     # D2
PORT_BUTTON = 4     # D4
POTENTIOMETER = 0   # A0
LCD_LINE_LEN = 16

# Setup
grovepi.pinMode(PORT_BUZZER, "OUTPUT")
grovepi.pinMode(PORT_BUTTON, "INPUT")

lcd.setRGB(0, 128, 0)

# Installed Apps!
APPS = [
    my_weather.WEATHER_APP,
    my_reddit.QOTD_APP,
    # TODO: Add your new app here
    my_app.GTLL_APP
]

# Cache to store values so we save time and don't abuse the APIs
CACHE = [''] * len(APPS)
for i in range(len(APPS)):
    # Includes a two space offset so that the scrolling works better
    CACHE[i] = '  ' + APPS[i]['init']()

app = 0     # Active app
ind = 0     # Output index

while True:
    try:
        # Check for input
        if grovepi.digitalRead(PORT_BUTTON):
            # BEEP!
            grovepi.digitalWrite(PORT_BUZZER, 1)

            # Switch app
            app = (app + 1) % len(APPS)
            ind = 0
        if grovepi.analogRead(POTENTIOMETER):
            if grovepi.analogRead(POTENTIOMETER) <204 and grovepi.analogRead(POTENTIOMETER)>=0:
                lcd.setRGB(0,0,0)
            if grovepi.analogRead(POTENTIOMETER) < 408 and grovepi.analogRead(POTENTIOMETER)>=204:
                lcd.setRGB(0,255,0)
            if grovepi.analogRead(POTENTIOMETER) < 612 and grovepi.analogRead(POTENTIOMETER)>=408:
                lcd.setRGB(255,0,0)
            if grovepi.analogRead(POTENTIOMETER) < 816 and grovepi.analogRead(POTENTIOMETER)>=612:
                lcd.setRGB(0,0,255)
            if grovepi.analogRead(POTENTIOMETER) <= 1023 and grovepi.analogRead(POTENTIOMETER)>=816:
                lcd.setRGB(255,255,255)
        time.sleep(0.1)

        grovepi.digitalWrite(PORT_BUZZER, 0)

        # Display app name
        lcd.setText_norefresh(APPS[app]['name'])

        # Scroll output
        lcd.setText_norefresh('\n' + CACHE[app][ind:ind+LCD_LINE_LEN])
        # TODO: Make the output scroll across the screen (should take 1-2 lines of code)
        #print('\n' +  CACHE[app][ind:ind+LCD_LINE_LEN])
        text = CACHE[app][ind:ind+LCD_LINE_LEN]
        for l in range(0,len(text)):
            lcd.setText_norefresh('\n' + CACHE[app][ind:ind+LCD_LINE_LEN])
            ind = ind + 1
    except KeyboardInterrupt:
        # Gracefully shutdown on Ctrl-C
        lcd.setText('')
        lcd.setRGB(0, 0, 0)

        # Turn buzzer off just in case
        grovepi.digitalWrite(PORT_BUZZER, 0)

        break

    except IOError as ioe:
        if str(ioe) == '121':
            # Retry after LCD error
            time.sleep(0.25)

        else:
            raise

