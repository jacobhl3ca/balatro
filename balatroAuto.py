import pyautogui # https://pyautogui.readthedocs.io/en/latest/quickstart.html
pyautogui.FAILSAFE = True
import time
import logging
import os
    
# Function to perform the automation
def automate_clicks():

    # Switch to the desired application using AppleScript
    os.system("osascript -e 'tell application \"System Events\" to key code 48 using {command down}'")
    time.sleep(0.5)  # Small delay to ensure the app switch completes

    # Press the escape key
    pyautogui.press('escape')
    
    # Coordinates to click
    positions = [
        # (477, 689), #from main menu
        (746, 340), # if already on challenege screen
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