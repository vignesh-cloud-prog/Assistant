
#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == "d":
            mixer.music.stop()
            break
        elif input_of_user=="x":
            exit()

def log_now(act,msg):
    if act=="water":
        with open("water.txt", "a") as f:
            f.write(f"{msg} {datetime.now()}\n")
            print("Succesfully logged")
    elif act=="eyes":
        with open("eyes.txt", "a") as f:
            f.write(f"{msg} {datetime.now()}\n")
            print("Succesfully logged")
    elif act=="physical":
        with open("physical.txt", "a") as f:
            f.write(f"{msg} {datetime.now()}\n")
            print("Succesfully logged")

# if __name__ == '__main__':
def healthy():
    # musiconloop("water.mp3", "stop")
    print("\n***** Start day with healthy mode, have a greate day *****\n")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40
    exsecs = 50
    eyessecs = 30

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. (Enter 'd' to stop the alarm & 'x' to exit.)")
            musiconloop('water.mp3')
            init_water = time()
            log_now("water","Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. (Enter 'd' to stop the alarm & 'x' to exit.)")
            musiconloop('eyes.mp3')
            init_eyes = time()
            log_now("eyes","Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. (Enter 'd' to stop the alarm & 'x' to exit.) ")
            musiconloop('physical.mp3')
            init_exercise = time()
            log_now("physical","Physical Activity done at")




