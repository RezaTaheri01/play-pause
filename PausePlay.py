from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from tendo import singleton
from time import sleep
import pyautogui
import keyboard
import ctypes
import os

me = singleton.SingleInstance()  # prevent duplicate
allow_list = []  # will not pause when item in this list playing
ctypes.windll.user32.ShowWindow(
    ctypes.windll.kernel32.GetConsoleWindow(), 0)  # hide

# region main code


def is_audio_playing():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        # 10872 is bucklespring
        # if session.State == 1 and session._ctl.GetProcessId() != 10872:  # State == 1 means the audio session is active
        # State == 1 means the audio session is active
        if session.State == 1 and session.Process.name() not in allow_list:
            return True
    return False


def main():
    global allow_list
    # if allow_list.txt file exist get from txt file else []
    if os.path.exists('./allow_list.txt'):
        file = open('./allow_list.txt', 'r')
        allow_list = file.read().split('\n')

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    start_volume = volume.GetMasterVolumeLevel()
    while True:
        # Check for Alt + Q combination to exit
        if keyboard.is_pressed('alt') and keyboard.is_pressed('q'):
            print("Alt + Q pressed. Exiting program.")
            break
        sleep(0.01)
        current = volume.GetMasterVolumeLevel()
        if int(current) != int(start_volume):
            if is_audio_playing():
                pyautogui.press('playpause')
                # volume.SetMasterVolumeLevelScalar(0.0, None) # set system volume to zero
                volume.SetMute(True, None) # mute
                # add actions as you wish (it's better to set sleep between your actions)
            start_volume = current


main()
# endregion
