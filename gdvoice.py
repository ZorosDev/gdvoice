import pyaudio
import wave
import audioop
import pyautogui
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5000
rms = 0
clicked = False
last = 1500
times = 0
p = pyaudio.PyAudio()

clicked2 = False


print("If you shout, your mouse will click even if you arn't in GD, so be aware\nThe program will log your mic sensitivity, the numbers must be greater than 4500 to register a click! Hit enter to continue")
x = input()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    rms = audioop.rms(data, 2)
    print(rms)

    if (rms > 4500 and rms < 7500):
        if (clicked2 == False):
            clicked = False

    if (rms > 7500):
        last = rms
        data = 0
        rms = 0

        if (clicked2 == True):
            pyautogui.mouseDown()
            clicked2 = False
        clicked = True
        rms = 0

    else:
        if (clicked2 == False):
            pyautogui.mouseUp()
            clicked2 = True
        clicked = False

stream.stop_stream()
stream.close()
p.terminate()
