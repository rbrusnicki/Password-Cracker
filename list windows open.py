# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 15:52:52 2023

@author: ge62gas
"""

import win32gui

def get_window_titles():
    def callback(hwnd, window_titles):
        if win32gui.IsWindowVisible(hwnd):
            window_text = win32gui.GetWindowText(hwnd)
            window_titles.append(window_text)

    window_titles = []
    win32gui.EnumWindows(callback, window_titles)
    return window_titles

# Usage example
titles = get_window_titles()
for title in titles:
    print(title)