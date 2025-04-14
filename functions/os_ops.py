import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'cmd': "cmd.exe",  
    'camera': "microsoft.windows.camera:"  
}

def open_notepad():
    """Open Notepad++"""
    try:
        if os.path.exists(paths['notepad']):
            os.startfile(paths['notepad'])
        else:
            os.system('notepad')
    except Exception as e:
        print(f"Error opening Notepad: {e}")

def open_cmd():
    """Open Command Prompt"""
    try:
        os.system(f'start {paths["cmd"]}')
    except Exception as e:
        print(f"Error opening Command Prompt: {e}")

def open_camera():
    """Open Camera App"""
    try:
        os.system(f'start {paths["camera"]}')
    except Exception as e:
        print(f"Error opening Camera: {e}")

def open_calculator():
    """Open Calculator"""
    try:
        if os.path.exists(paths['calculator']):
            sp.Popen(paths['calculator'])
        else:
            os.system('calc')
    except Exception as e:
        print(f"Error opening Calculator: {e}")