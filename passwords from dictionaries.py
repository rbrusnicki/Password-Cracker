# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 18:56:59 2023

@author: ge62gas
"""

import pyautogui
import time

def read_file(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove leading/trailing whitespace
            lines.append(line)
    return lines





filename = 'usernames.txt'  # Replace with your file path or name

words = read_file(filename)

# Start time
start_time = time.time()

count = 10000
flag = 0

for word in words[count:]:
        
    # Activate the window with the specified title
    window = pyautogui.getWindowsWithTitle("Log In")
    if (flag < 3):
        if (window == [] ):
            # Wait for a moment to ensure the window is activated
            time.sleep(0.01)
            flag += 1
        else:
            flag = 0
            window[0].activate()
        
            pyautogui.typewrite(word)
            
            # Wait for a moment to ensure the window is activated
            time.sleep(0.001)
            
            pyautogui.typewrite("\n\n" )
            
            print(count)
            count += 1
            
            # Wait for a moment to ensure the window is activated
            time.sleep(0.002)
    else:
        print(f"The window was not found 3 times consecutively")
        break
    
# End time
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

print(f"The code took {elapsed_time:.2f} seconds to run.")