import pyautogui  # Library for GUI automation (https://pyautogui.readthedocs.io/en/latest/quickstart.html)
# Enable fail-safe to stop the script by moving the mouse to the upper-left corner
pyautogui.FAILSAFE = True
import time
import os
# import logging
    
# Function to perform the automation
def automate_clicks():

    # Switch to the desired application using AppleScript
    os.system("osascript -e 'tell application \"System Events\" to key code 48 using {command down}'")
    time.sleep(0.5)  # Small delay to ensure the app switch completes

# URL has to be open in browser
# https://mail.google.com/mail/u/0/#search/from%3Ajacobhl3CA%40gmail.com+OR+jacob.heifetz-licht%40keplergrp.com+to%3Ame+in%3Ainbox 

    # Press the escape key
    pyautogui.press('escape')
    
    # Coordinates to click
    positions = [
        # from main menu
        # (477, 689) #comment/uncomment
        # if already on challenge screen
        (746, 340),  #comment/uncomment
        (805, 202),
        (706, 415),
        (512, 585),
        (490, 540),
        (869, 635)
    ]

    # Loop through each position and click
    for position in positions:
        pyautogui.moveTo(position[0], position[1], duration=0.2)  # Smooth movement to ensure accuracy
        pyautogui.click()
        time.sleep(0.2)  # Small delay to ensure stability

# Run the automation
automate_clicks()