#!/usr/bin/env python

import os, sys, subprocess
from os.path import exists
IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"
raw_input = input
def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
clear_screen()
print("File Manager (type make to make a file, 0 Exit)")
subprocess.call(("dir", "files"))
loc = raw_input("Aroba / > ")
print(loc)
def main():
    if loc == "0":
        sys.exit(5)
    if loc == "make":
        clear_screen()
        f = raw_input("File name > ")
        print(f)
        g = open("files/{}".format(f), "w+")
        d = raw_input("text > ")
        print(d)
        g.write(d)
        clear_screen()
        raw_input("File Created")
        subprocess.call((sys.executable, "files/manager.py"))
    else:
        clear_screen()
        try:
            loc_real = open("files/{}".format(loc))
        except:
            clear_screen()
            raw_input("File location isn't there!")
            subprocess.call((sys.executable, "files/manager.py"))
        input = raw_input("Remove/Write/Read/Quit:").lower()
        if input == "remove":
            clear_screen()
            os.remove("files/{}".format(loc))
            main()
        elif input == "write":
            clear_screen()
            loc_real.write(raw_input("Input what you want to write: "))
            main()
        elif input == "read":
            clear_screen()
            file_con = loc_real.read()
            print(file_con)
            raw_input("\nBack")
            main()
        elif input == "quit" or "q":
            subprocess.call((sys.executable, "files/manager.py"))
main()
