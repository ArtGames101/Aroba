# -*- coding: utf-8 -*-
# PiePlayer (c) ArtGames101 2018
import pygame, sys, os, subprocess, time
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

def main():
    clear_screen()
    print("Choose a song!\n")
    subprocess.call(("dir", "songs"))
    print("\nType '0' to exit")
    sng = user_choice()
    if sng == "0":
        subprocess.call((sys.executable, "run.py"))
    else:
        play(sng)
    
def play(sng):
    clear_screen()
    pygame.mixer.init()
    if config.loopedsong == False:
        try:
            pygame.mixer.music.load("songs/{}".format(sng))
            pygame.mixer.music.play()
        except:
            clear_screen()
            input("❚❚ | Unable to play/load '{}'".format(sng))
            subprocess.call((sys.executable, "playr.py"))
        main()
    if config.loopedsong == True:
        try:
            pygame.mixer.music.load("songs/{}".format(sng))
            pygame.mixer.music.play()
        except:
            clear_screen()
            input("Unable to play/load '{}'".format(sng))
            subprocess.call((sys.executable, "applications/aroba_apps/playr.py"))
    while pygame.mixer.music.get_busy() == True:
        clear_screen()
        print("►   Song Playing\n"
              "====================")
        print("\n"
              "{}\n"
              "\n"
              "c. Change Song\n"
              "\n"
              "p. Pause\n"
              "\n"
              "e. Exit".format(sng))
        choice = user_choice()
        if choice == "c":
            pygame.mixer.music.stop()
            main()
        if choice == "p":
            pygame.mixer.music.pause()
            input("Push Enter to unpause")
            pygame.mixer.music.unpause()
        if choice == "e":
            pygame.mixer.music.stop()
            sys.exit(1)
        continue
        if config.loopedsong == True:
            play(choice)
        else:
            main()


main()
