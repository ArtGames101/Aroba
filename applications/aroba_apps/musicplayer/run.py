# PiePlayer (c) ArtGames101 2018
import pygame, sys, os, subprocess, webbrowser, time

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
    print("PiePlayer\n"
          "================")
    print("\n"
          "l. Play Songs\n"
          "\n"
          "c. Changelog\n"
          "\n"
          "w. Find Songs on the web\n"
          "\n"
          "Config located applications/aroba_apps/musicplayer\n"
          "ArtSystem Edition")
    choice = user_choice()
    if choice == "l":
        clear_screen()
        print("PiePlayer Audio\n"
              "===================")
        print("\n"
              "1. Play Playlist (Python3)\n"
              "\n"
              "2. Play A Song (Python 3)\n"
              "\n"
              "i. Info\n"
              "0. Back")
        choice = user_choice()
        if choice == "1":
            subprocess.call((sys.executable, "applications/aroba_apps/musicplayer/play.py"))
        if choice == "2":
            subprocess.call((sys.executable, "applications/aroba_apps/musicplayer/playr.py"))
        if choice == "i":
            clear_screen()
            print("PiePlayer Audio\n"
                  "===================")
            print("\n"
                  "Playlist:\n"
                  "The Playlist is looped and shuffled!\n"
                  "\n"
                  "Play Song:\n"
                  "Choose a song to play (You can choose to loop from config)")
            input("\n"
                  "Back")
            main()
    if choice == "c":
        changelog()
    if choice == "w":
        webbrowser.open("https://ganna.com")
        print("Opening Please wait...")
        time.sleep(5)
        main()

def changelog():
    clear_screen()
    print("PiePlayer Changelog\n"
          "=======================")
    print("Whats New?\n"
          "\n"
          "* Added Changelog\n"
          "* Added Loop option for Play Song\n"
          "* Added Better Sound Quality (Cause its pygame :D)\n"
          "* Fixed Small Bugs\n"
          "* Added Exit Option for Play Song\n")
    input("\n"
          "Back")
    main()
    
main()
