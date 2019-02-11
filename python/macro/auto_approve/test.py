# -*- coding: utf-8 -*-
import win32gui

def windowEnumerationHandler(hwnd, windows):
    windows.append((hwnd, win32gui.GetWindowText(hwnd)))

print(win32gui.GetCursorPos())
windows = []
win32gui.EnumWindows(windowEnumerationHandler, windows)
for window in windows:
    print(window)