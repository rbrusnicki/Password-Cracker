# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:04:47 2023

@author: ge62gas
"""

import pyautogui
import time

#char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def output_text(window_title, text):
    # Activate the window with the specified title
    pyautogui.getWindowsWithTitle(window_title)[0].activate()

    
    # Type the text into the window
    pyautogui.typewrite(text)

    # Wait for a moment to ensure the window is activated
    time.sleep(0.001)



# Example usage
window_title = "Log In"  # Replace with the title of the desired window

# Activate the window with the specified title
pyautogui.getWindowsWithTitle(window_title)[0].activate()

# Start time
start_time = time.time()

for i in range(1, 37):
    for j in range(1, 2):
        
        selected_chars = [char_list[position - 1] for position in [i, j]]
        
        # Type the text into the window
        pyautogui.typewrite(''.join(selected_chars) )
        
        # Wait for a moment to ensure the window is activated
        time.sleep(0.001)
        
        pyautogui.typewrite("\n\n" )
        
        #output_text(window_title, ''.join(selected_chars) )
        #output_text(window_title, "\n\n")


# End time
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print(f"The code took {elapsed_time:.2f} seconds to run.")