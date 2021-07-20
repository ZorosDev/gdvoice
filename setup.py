from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna","pyaudio","wave","audioop","pyautogui","time"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "GD Voice Controller",
    options = options,
    version = "v1.0",
    description = 'Voice controller for Geometry Dash',
    executables = executables
)
