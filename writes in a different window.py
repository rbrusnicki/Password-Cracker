# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import win32gui
import win32con

def send_text_to_window(window_title, text):
    # Find the window based on the title
    window_handle = win32gui.FindWindow(None, window_title)

    if window_handle == 0:
        print("Window not found.")
        return

    # Set the target window as the foreground window
    win32gui.SetForegroundWindow(window_handle)

    # Simulate typing by sending WM_CHAR messages
    for char in text:
        win32gui.SendMessage(window_handle, win32con.WM_CHAR, ord(char), 0)

    print("Text sent successfully.")


# Usage example
window_title = "Untitled - Notepad"  # Replace with the title of the desired window
text_to_send = "Hello, World!"  # Replace with the text you want to send

send_text_to_window(window_title, text_to_send)