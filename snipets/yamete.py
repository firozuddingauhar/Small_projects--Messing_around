from playsound import playsound
import keyboard

while True:
    # if keyboard.is_pressed('a'):
    if keyboard.read_event().event_type==keyboard.KEY_DOWN:
        playsound("..\Yamete Kudasai-YoutubeConvert.cc.wav")