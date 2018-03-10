# -*- coding: utf-8 -*-
# PiePlayer (c) ArtGames101 2018
import pygame, sys, os, time, subprocess
import random
import config

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def songloop():
    pygame.mixer.init()
    try:
        s = random.choice(config.songs)
        pygame.mixer.music.load("songs/{}".format(s))
        pygame.mixer.music.play()
        clear_screen()
        print("►   Song Playing\n"
              "====================")
        print("\n"
              "{}\n"
              "\n"
              "Next Song Will Play Soon...".format(s))
    except:
        clear_screen()
        input("❚❚ | Unable to play/load '{}'".format(choice))
        songloop()
    while pygame.mixer.music.get_busy() == True:
        continue
    subprocess.call((sys.executable, "applications/aroba_apps/play.py"))

clear_screen()
print("Song Log:\n")
print("CTRL + C Exit")
songloop()
