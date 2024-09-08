Volume Monitoring Script
========================

This Python script monitors the system's master volume for changes and automatically pauses audio playback when the volume is altered, provided the active audio session is not in the allow list.

Features
--------

*   **Auto Pause on Volume Change**: When the system's master volume changes while any non-allowed audio is playing, the script automatically simulates a "play/pause" action.
    
*   **Allow List**: Add processes to the `allow_list` so that the script ignores them when checking if audio is playing.

Prerequisites
-------------

Ensure the following dependencies are installed before running the script:

*   [Pycaw](https://github.com/AndreMiras/pycaw) (Python Core Audio API Wrapper)
*   [Tendo](https://github.com/pycontribs/tendo) (for singleton functionality)
*   [PyAutoGUI](https://github.com/asweigart/pyautogui) (for simulating keypresses)
*   `comtypes` (for interacting with Windows audio interfaces)
*   `keyboard`

You can install these with pip:

```
pip install pycaw tendo pyautogui comtypes keyboard
```
or
```
pip install -r req.txt
```

Usage
-----

1.  **Allow List**: If you want to exclude specific processes from triggering the "play/pause" action, create a `allow_list.txt` file in the same directory as the script. In this file, list process names, one per line.
    
    Example of `allow_list.txt`:    
    ```
    process1.exe
    process2.exe
    ```
    
3.  **Running the Script**: Simply run the script using Python. It will monitor the system volume and pause audio playback if the conditions are met.

    ```
    python PlayPause.py
    ```

3.  **Process-Specific Behavior**: The script is configured to ignore a specific process (e.g., `bucklespring`) based on its process ID in the `is_audio_playing` function. You can modify this based on your needs.

Notes
-----

*   To stop program press alt + q
*   This script is set to hide the console window when running. To view the console, you can comment out the line that hides it:   

    python
    
    ```
    # ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)  # hide
    ```

*   It uses a singleton instance to prevent multiple instances of the script from running simultaneously.
