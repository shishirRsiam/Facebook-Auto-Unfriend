"""
Facebook Auto-Unfriend Script
This script automates the process of unfriending Facebook friends using image recognition.
Note: Use responsibly and in accordance with Facebook's Terms of Service.
"""

import pyautogui as pg  # For GUI automation (mouse/keyboard control and image recognition)
import time  # For adding delays between actions

# Safety feature: Pause for 5 seconds to allow user to switch to the target window
# This prevents the script from running while you're still setting up
time.sleep(5)

def click_image(image_path, confidence=0.9):
    """
    Locate and click on an image on the screen.
    
    Parameters:
    - image_path (str): Path to the image file to search for
    - confidence (float): Accuracy threshold for image matching (0.0 to 1.0)
                          Higher values are more strict but may miss matches
    """
    try:
        # Search for the image on the screen
        location = pg.locateOnScreen(image_path, confidence=confidence)
        
        if location:
            # Click the center of the found image location
            pg.click(location)
            print(f"Clicked on image: {image_path}")
        else:
            print(f"Image not found on screen: {image_path}")
    except Exception as e:
        print(f"An error occurred in click_image: {e}")

def try_unfriend():
    """
    Perform the unfriend sequence by clicking through the required buttons.
    This function assumes the friend is already selected/hovered over.
    """
    try:
        # Step 1: Click the three dots menu (friends action menu)
        click_image('three_dots.png')
        time.sleep(0.5)  # Wait for menu to appear
        
        # Step 2: Click the unfriend option
        click_image('unfriend_button.png')
        time.sleep(0.2)  # Wait for confirmation dialog
        
        # Step 3: Confirm the unfriend action
        click_image('confirm_unfriend_button.png')
        print("Unfriend action completed.")
    except Exception as e:
        print(f"An error occurred in try_unfriend: {e}")

# Counter to track iterations for scrolling logic
count = 0

# Main loop: Runs continuously until manually stopped (Ctrl+C)
while True:
    count += 1
    
    # Every other iteration, scroll down to load more friends
    # This helps when you have many friends that don't all fit on one screen
    if count % 2 == 0:
        # Scroll down by 120 pixels (negative = down, positive = up)
        pg.scroll(-120)
        time.sleep(0.5)  # Wait for content to load after scrolling
    
    # Attempt to unfriend the currently visible/selected friend
    try_unfriend()
    
    # Short pause between actions to prevent overwhelming the system
    time.sleep(0.5)  # Adjust based on your system's response time

# Important Notes:
# 1. Requires image files (three_dots.png, unfriend_button.png, confirm_unfriend_button.png)
# 2. Images must be exact matches of what appears on your screen
# 3. Screen resolution and browser zoom affect image recognition
# 4. Script may fail if Facebook UI changes
# 5. Run at your own risk - excessive automation may trigger Facebook's security
