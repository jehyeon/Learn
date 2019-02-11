# from pywinauto.findwindows    import find_window
# from pywinauto.win32functions import SetForegroundWindow

import win32gui, win32api, win32con, win32com
import time

def click(x, y):
      win32api.SetCursorPos((x,y))
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
      win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def windowEnumerationHandler(hwnd, windows):
        windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if __name__ == '__main__':
        windows = []
        win32gui.EnumWindows(windowEnumerationHandler, windows)
        for window in windows:
                print(window)
                if u'카카오톡' in window[1].lower():
                        win32gui.ShowWindow(window[0],5)
                        win32gui.SetForegroundWindow(window[0])
        click(1853, 153)
        # time.sleep(3)
        # click(1458,118)