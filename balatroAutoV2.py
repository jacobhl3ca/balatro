import pyautogui
import time
import os

# Disable PyAutoGUI failsafe for uninterrupted automation
pyautogui.FAILSAFE = False

# Function to perform the automation
def automate_clicks():
    # Switch to the desired application using AppleScript
    os.system("osascript -e 'tell application \"System Events\" to key code 48 using {command down}'")
    time.sleep(0.2)  # Reduced delay for faster execution

    # Press the escape key
    pyautogui.press('escape')

    # Coordinates to click
    positions = [
        
        # (889, 640),  # click new run after loss
        # for some reason locations are different for
        # challenges etc when i click new run..


        # main use case: once starting a new game
        # , trying to find right blinds
        # (746, 340),  # IDK..: If already on challenge screen
        # (805, 202),
        # (706, 415),
        # (512, 585),
        # (490, 540),
        # (869, 635),
        # (504, 641)

        (767, 359),  # IDK..: If already on challenge screen
        (856, 197),
        (750, 465),
        (488, 693),
        (445, 627),
        (935, 738),
        (468, 760)
        
    ]

    # Loop through each position and click
    for position in positions:
        pyautogui.moveTo(*position, duration=0.1)  # Faster movement
        pyautogui.click()
        time.sleep(0.1)  # Minimal delay for stability

# Run the automation
automate_clicks()
