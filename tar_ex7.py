import time
from pygame import mixer
# initial = time.time()


def getdate():
    import datetime
    return datetime.datetime.now()


def music_play(mp3, stopper):
    mixer.init()
    mixer.music.load(mp3)
    mixer.music.play()
    while True:
        word = input("enter")
        if word == stopper:
            mixer.music.stop()
            break
        else:
            break
    return word


def log(mess):
    with open("detail.txt", "a") as f:
        f.write(f" {mess} at {str(getdate())} \n")
        print("Good keep the spirit")


def check(a):
    if a == "Drank":
        log("Water drank")
        print("done")

    elif a == "Eydone":
        log("Eyes Exercise done ")
        print("eyes ex done")
    elif a == "Exdone":
        log("Exercise done ")
        print("Ex done")


eyes = 0
water = 0
physical_ex = 0
while True:
    if water <= 18:
        time.sleep(30)
        print("Drink water")
        a = music_play("water.mp3", "Drank")
        check(a)
        water = water + 1
    if eyes <= 16:
        time.sleep(10)
        print("eyes")
        a = music_play("water.mp3", "Eydone")
        check(a)
        eyes = eyes + 1
    if physical_ex <= 10:
        time.sleep(5)
        print("Do some Exercise")
        a = music_play("water.mp3", "Exdone")
        check(a)
        physical_ex = physical_ex + 1
    if water <= 18 or physical_ex <= 10 or eyes <= 16:
        continue
    else:
        print("Very well done")
        break
