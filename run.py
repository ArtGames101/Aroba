# -*- coding: utf-8 -*-
# ArtSystem (c) ArtGames101 2017 - 2018
# Lobit ҉ (c) MrBackPack 2018 (Designed by MrBackPack, Programmed by ArtGames101)

# (A≈) ArtSystem Aroba

import sys, os, random, time, subprocess, webbrowser
import urllib
import config as c
try:
    from data import gold as g
    from data import alphapps as alpha
except:
    pass
from data import anew
try:
    from log import notification
except:
    pass
from data import upgradestay as upg
try:
    from user.user1 import logindata as logind
    from user.user1 import loginpass as loginp
    from user.user1 import parental as parent
    from user.user1 import reminder as remind
    from user.user1 import img
except:
    pass

# Lobit Imports
try:
    from data.lobit import restricted as lrist
except:
    input("( ҉ ) Lobit ERROR: Could not import data.lobit.restricted")
    pass
# Version
vr = "1.0"
version = "v{}-Alpha".format(vr)
# Next Version
nextup = "2.0"
try:
    error = open("log/lasterror.txt", "w")
    start = open("log/startlog.txt", "w")
except:
    pass
try:
    webb = open("web/name.py", "w")
    webb.write("name = '{}'".format(logind.USERNAME))
except:
    try:
        webb = open("Aroba/web/name.py", "w")
        webb.write("name = '{}'".format(logind.USERNAME))
    except:
        pass
    
webb.close()
santa = False
games = ["snake", "BattleSim", "squirrel", "Santa", "Tetris", "GunRush", "DocCreator", "VF"]
apps = ["DocCreator", "VF", "WebBrowser"]
gm = 6
ap = 3
pa = 2
ad = ["Go Gold and get ALPHA games that are comming soon!", "Get Alphapps to install the newest apps!", "Squirrel (GO GOLD!) (Eat other squirrels to become the OMEGA SQUIRREL)", "Snake (a game where you have to eat apples!)", "BattleSim (The best battle simulator for python!)", "Tetris  (A Game where you have to stack blocks!)"]
try:
    import snake
except Exception as e:
    try:
        exc = '{}: {}'.format(type(e).__name__, e)
        error.write(exc)
    except:
        pass

try:
    import tetris
except Exception as e:
    try:
        exc = '{}: {}'.format(type(e).__name__, e)
        error.write(exc)
    except:
        pass
try:
    from BattleSim import run as battle
except Exception as e:
    try:
        exc = '{}: {}'.format(type(e).__name__, e)
        error.write(exc)
    except:
        pass

try:
    import squirrel
except Exception as e:
    try:
        exc = '{}: {}'.format(type(e).__name__, e)
        error.write(exc)
    except:
        pass

try:
    import santa
except Exception as e:
    try:
        exc = '{}: {}'.format(type(e).__name__, e)
        error.write(exc)
    except:
        pass


IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def adconsole():
    return input("\n#ROOT:Aroba:~ $ ").lower().strip()

def new():
    clear_screen()
    try:
       subprocess.call(('notify-send', 'ArtSystem Verification', 'Please enter your 6 digit code!'))
    except:
        pass
    print("(A≈) ArtSystem Aroba {}\n"
          "===========================".format(vr))
    print("\n"
          "Please enter your 6 digit verification code\n"
          "to continue!")
    print("\n"
          "?: Get it from the Aroba Github")
    choice = user_choice()
    if choice == "aroba1":
        confirm = open("data/anew.py", "w")
        confirm.write("new = False")
        input("Verification code accepted!")
        confirm.close()
        neww()
    else:
        input("Invalid Verification Code!")
        new()

def neww():
    clear_screen()
    print("(A≈) ArtSystem Aroba {}\n"
          "==========================".format(vr))
    print("\n"
          "Welcome to ArtSystem!\n"
          "\n"
          "Here is what you can do with your new ArtSystem!\n"
          "\n"
          "* Play Games\n"
          "* Manage Accounts\n"
          "* Browse the web\n"
          "* Create & Run Applications\n"
          "* Browse Updates & Events\n"
          " And More!")
    input("\n"
          "Enter")
    lobitintro()
def lobitintro():
    clear_screen()
    print("Lobit  ҉  \n"
          "==============")
    print("\n"
          "Hello i am Lobit  ҉  your ArtSystem Personal Assistant!\n"
          "\n"
          "My job is to help you when you need to find something or just need someone to talk to!\n"
          "\n"
          "1. Take a Tour\n"
          "\n"
          "2. Next")
    choice = user_choice()
    if choice == "1":
        lobittour()
    if choice == "2":
        newww()
    else:
        lobitintro()

def lobittour():
    clear_screen()
    print("Lobit  ҉\n"
          "============")
    print("\n"
          "Options:\n"
          "\n"
          "1. What is Lobit?\n"
          "2. Where are the Lobit Files Located?\n"
          "3. What does lobit do?\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("A note from the developers\n"
              "==============================\n"
              "Lobit   ҉ is a Personal Assistant Designed by MrBackPack\n"
              "and programmed by ArtGames101")
        print("\n"
              "Information about Lobit\n"
              "===========================\n"
              "Lobit is a Personal Assistant that is designed to\n"
              "help you find files/applications or just to talk to!\n")
        input("\n"
              "Back")
        lobittour()
    if choice == "2":
        clear_screen()
        print("Lobit Files\n"
              "===============\n"
              "Most of Lobit's Code is intergrated into ArtSystem but...\n"
              "if you go to '/data/lobit' or '\data\lobit' you can find a file called restricted.py\n"
              "which contains phrases that Lobit Either Disagrees with or phrases that make lobit says something funny")
        input("\n"
              "Back")
        lobittour()
    if choice == "3":
        clear_screen()
        print("What can lobit do\n"
              "=====================\n"
              "lobit can:\n"
              "\n"
              "* Help you find things\n"
              "* Can talk to you\n"
              "* Can tell jokes\n"
              "* Can Search for things\n"
              "And more!\n")
        input("\n"
              "Back")
        lobittour()
    if choice == "0":
        lobitintro()
    else:
        lobittour()

def newww():
    clear_screen()
    print("(A≈) ArtSystem Aroba {}\n"
          "==========================".format(vr))
    print("\n"
          "Your ArtSystem Comes with Restore Options and Web Protection!\n"
          "\n"
          "Info : This is the last version of Vortex but there will be software updates!\n"
          "\n"
          "Push Enter to Register\n")
    input(".")
    register()

def fchangelog():
    # After update changelog
    clear_screen()
    print("(A≈) ArtSystem Aroba {}\n"
          "===========================".format(vr))
    print("Changelog:\n"
          "* First Version")
    input("\n"
          "Enter")
    sys.exit(1)

def warn():
    try:
        subprocess.call(('notify-send', 'ArtSystem Startup', 'Please Make ArtSystem Fullscreen!'))
    except:
        pass
    clear_screen()
    print("(A≈) ArtSystem Aroba\n"
          "==========================")
    print("\n"
          "INFO : Please Put ArtSystem in Full Screen!"
          "\n"
          "Redirecting in 3...")
    time.sleep(1)
    clear_screen()
    print("(A≈) ArtSystem Aroba\n"
          "==========================")
    print("\n"
          "INFO : Please Put ArtSystem in Full Screen!"
          "\n"
          "Redirecting in 2...")
    time.sleep(1)
    clear_screen()
    print("(A≈) ArtSystem Aroba\n"
          "==========================")
    print("\n"
          "INFO : Please Put ArtSystem in Full Screen!"
          "\n"
          "Redirecting in 1...")
    time.sleep(1)
    loading()

def loading():
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ____+___  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | +_______  \n"
      "  |__________________|         |__________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |                  |         |_+________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   __+_____  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |__+_______\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |                  |         |_____+____\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            /")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ______+_  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |_____+____\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |                  |         |_+________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   __+_____  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |_+________\n"
      "  |                  |   \n"
      "  |                  | _+______  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ________  \n"
      "   /                \          |_+________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |__+_______\n"
      "  |                  |   \n"
      "  |                  | _+______  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ________  \n"
      "   /                \          |________+_\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |_+________\n"
      "  |                  |   \n"
      "  |                  | _+______  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            \ ")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   +_______  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | _____+__  \n"
      "  |__________________|         |__________\n"
      "  |                  |   \n"
      "  |                  | __+_____  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ________  \n"
      "   /                \          |______+___\n"
      "  |                  |   \n"
      "  |                  | ____+___  \n"
      "  |__________________|         |__________\n"
      "  |                  |   \n"
      "  |                  | +_______  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ________  \n"
      "   /                \          |_______+__\n"
      "  |                  |   \n"
      "  |                  | __+_____  \n"
      "  |__________________|         |__________\n"
      "  |                  |   \n"
      "  |                  | +_______  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            /")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   +_______  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |__+_______\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |                  |         |___+______\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ________  \n"
      "   /                \          |_______+__\n"
      "  |                  |   \n"
      "  |                  | ___+____  \n"
      "  |__________________|         |__________\n"
      "  |                  |   \n"
      "  |                  | _____+__  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            |")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   ____+___  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |__+_______\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |                  |         |______+___\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            -")
    time.sleep(1)
    clear_screen()
    print("\n"
      "     / -----------\      \n"
      "    /              \   _____+__  \n"
      "   /                \          |__________\n"
      "  |                  |   \n"
      "  |                  | ________  \n"
      "  |__________________|         |___+______\n"
      "  |                  |   \n"
      "  |                  | ______+_  \n"
      "  |                  |         |__________\n"
      "                         \n"
      "        ArtSystem        \n")
    print("            \ ")
    time.sleep(1)
    welcome()

    
    
def welcome():
    clear_screen()
    try:
        from user.user1 import logindata
        from user.user1 import img
        from user.user1 import loginpass
        print(logindata.USERNAME)
        print(img.usrimg)
        print(loginpass.PASSWORD)
        clear_screen()
    except:
        clear_screen()
        print("============\n"
              " File Error \n"
              "============\n")
        print(":( An Error has been Encountered!\n"
              "Options to Fix Problem")
        print("\n"
              "1. Register (Will Write Fresh data)\n"
              "2. Guest Account  (Use Guest account for now!)\n"
              "3. Restore  (Restore 'LAST' Save data)\n"
              "4. Guide    (See the ArtSystem Guide)\n")
        subprocess.call((sys.executable, "sounds/error.py"))
        choice = user_choice()
        if choice == "1":
            register()
        if choice == "2":
            guestmain()
        if choice == "3":
            restore()
        if choice == "4":
            try:
                webbrowser.open("guide/help.html")
            except:
                try:
                    webbrowser.open("guide\help.html")
                except:
                    input("Unable to Open 'guide.html'")
                    welcome()
            welcome()
    try:
        subprocess.call(('notify-send', 'ArtSystem Startup', 'ArtSystem has sucessfuly Loaded!'))
    except:
        try:
            subprocess.call(('zenity', '--info', '--text="ArtSystem Aroba has sucessfuly Loaded!"', '--timeout=5 2'))
            clear_screen()
        except:
            pass
        if img.usrimg == "None":
            print("                    | Welcome to Aroba |\n"
                  "                    |------------------|\n"
                  "\n"
                  "1. [?] {}\n"
                  "\n"
                  "2. [G] Guest\n"
                  "\n"
                  "\n"
                  "r. Register\n"
                  "0. More Options                                       w. Warnings\n".format(logind.USERNAME))
            choice = user_choice()
            if choice == "1":
                login()
            if choice == "2":
                guesta()
            if choice == "r":
                regwarn()
            if choice == "admin":
                adlogin()
            if choice == "w":
                warnings()
            if choice == "0":
                try:
                    mainmore()
                except:
                    pass
            else:
                welcome()
        else:
            print("                    | Welcome to Aroba |\n"
                  "                    |------------------|\n"
                  "\n"
                  "1. [{}] {}\n"
                  "\n"
                  "2. [G] Guest\n"
                  "\n"
                  "\n"
                  "r. Register\n"
                  "0. More Options                                       w. Warnings\n".format(img.usrimg, logind.USERNAME))
            choice = user_choice()
            if choice == "1":
                login()
            if choice == "2":
                guesta()
            if choice == "r":
                regwarn()
            if choice == "admin":
                adlogin()
            if choice == "w":
                warnings()
            if choice == "0":
                try:
                    mainmore()
                except:
                    pass
            else:
                welcome()

def warnings():
    clear_screen()
    print("Warning!\n"
          "============")
    print("\n"
          "1. Please make sure to logout properly\n"
          "2. Please Report All bugs you find otherwise it could destroy your ArtSystem!\n")
    input(".")
    welcome()
def mainmore():
    clear_screen()
    print("==============\n"
          " More Options \n"
          "==============\n")
    print("\n"
          "1. Refer\n"
          "2. Restore\n"
          "3. Shutdown Options\n"
          "\n"
           "0. Back")
    choice = user_choice()
    if choice == "1":
        refer()
    if choice == "2":
        restore()
    if choice == "3":
        wshutdown()
    if choice == "0":
        welcome()


def refer():
    clear_screen()
    print("=================\n"
          " Refer ArtSystem \n"
          "=================\n")
    print("\n"
          "Github : https://github.com/ArtGames101/Aroba\n"
          "\n"
          "Install cmd : git clone https://github.com/ArtGames101/Aroba.git")
    input("\n"
          "Back")
    mainmore()

def restore():
    clear_screen()
    try:
        from data.restore import name, passw
    except:
        input("No Data to restore!")
        mainmore()
    print("=========\n"
          " Restore \n"
          "=========\n")
    print("ArtSystem is restoring your old data!")
    try:
        usr = open("user/user1/logindata.py", "w")
        usr.write("USERNAME = '{}'".format(name.old))
        pa = open("user/user1/loginpass.py", "w")
        pa.write("PASSWORD = '{}'".format(passw.old))
        time.sleep(5)
        input("ArtSystem Restored!")
        usr.close()
        pa.close()
        subprocess.call((sys.executable, "run.py"))
    except:
        usr = open("Aroba/user/user1/logindata.py", "w")
        usr.write("USERNAME = '{}'".format(name.old))
        pa = open("Aroba/user/user1/loginpass.py", "w")
        pa.write("PASSWORD = '{}'".format(passw.old))
        time.sleep(5)
        input("ArtSystem Restored!")
        usr.close()
        pa.close()
        subprocess.call((sys.executable, "run.py"))
    
def wshutdown():
    clear_screen()
    print("==========\n"
          " Shutdown \n"
          "==========\n")
    print("1. Shutdown")
    print("2. Restart")
    print("\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("\n"
              "     / -----------\      \n"
              "    /              \   ________  \n"
              "   /                \          |__________\n"
              "  |                  |   \n"
              "  |                  | ________  \n"
              "  |__________________|         |__________\n"
              "  |                  |   \n"
              "  |                  | ________  \n"
              "  |                  |         |__________\n"
              "                         \n"
              "        ArtSystem        \n")
        print("Shutdown!")
        clear_screen()
    if choice == "2":
        subprocess.call((sys.executable, "run.py"))
    if choice == "0":
        welcome()

def guesta():
    clear_screen()
    print("===============\n"
          " Guest Account \n"
          "===============\n")
    print("\n"
          "Are you sure you want to login as a guest?\n"
          "\n"
          "You wont be able to: Surf the net, Shop or Change Settings!")
    print("1. Yes    | 2. No")
    choice = user_choice()
    if choice == "1":
        guestmain()
    if choice == "2":
        welcome()

def adlogin():
    clear_screen()
    print("=========\n"
          " Welcome \n"
          "=========\n")
    print("Administrator")
    print("\n"
          "Password\n"
          "\n"
          "_____________\n"
          "\n"
          "[0. Switch User]")
    choice = user_choice()
    if choice == "0":
        welcome()
    if choice == "aroba1":
        admin()
    else:
        adloginf()
def adloginf():
    clear_screen()
    print("=========\n"
          " Welcome \n"
          "=========\n")
    print("Administrator")
    print("\n"
          "Password\n"
          "\n"
          "_____________\n"
          "\n"
          "[0. Switch User]")
    print("\n"
          "Incorrect Password!")
    subprocess.call((sys.executable, "sounds/error.py"))
    choice = user_choice()
    if choice == "0":
        welcome()
    if choice == "aroba1":
        admin()
    else:
        adloginf()
def login():
    clear_screen()
    print("=========\n"
          " Welcome \n"
          "=========\n")
    try:
        print("{}".format(logind.USERNAME))
    except:
        input("No User found!")
        register()
    print("\n"
          "Password\n"
          "\n"
          "_____________\n"
          "\n"
          "[0. Switch User]")
    choice = user_choice()
    if choice == "0":
        welcome()
    if choice == loginp.PASSWORD:
        startsound()
    else:
        loginf()

def loginf():
    clear_screen()
    print("=========\n"
          " Welcome \n"
          "=========\n")
    try:
        print("{}".format(logind.USERNAME))
    except:
        input("No User found!")
        register()
    try:
        if remind.rem == "None":
            print("\n"
                  "Password\n"
                  "\n"
                  "_____________\n"
                  "\n"
                  "[0. Switch User]")
            print("\n"
                  "Incorrect Password!")
        else:
            print("\n"
                  "Password\n"
                  "\n"
                  "_____________\n"
                  "\n"
                  "Reminder : {}\n"
                  "[0. Switch User]".format(remind.rem))
            print("\n"
                  "Incorrect Password!")
    except:
        print("\n"
              "Password\n"
              "\n"
              "_____________\n"
              "\n"
              "[0. Switch User]")
        print("\n"
              "Incorrect Password!")
    subprocess.call((sys.executable, "sounds/error.py"))
    choice = user_choice()
    if choice == "0":
        welcome()
    if choice == loginp.PASSWORD:
        startsound()
    else:
        loginf()

def startsound():
    clear_screen()
    print("\n"
          "     / -----------\      \n"
          "    /              \   ________  \n"
          "   /                \          |__________\n"
          "  |                  |   \n"
          "  |                  | ________  \n"
          "  |__________________|         |__________\n"
          "  |                  |   \n"
          "  |                  | ________  \n"
          "  |                  |         |__________\n"
          "                         \n"
          "        Welcome        \n")
    subprocess.call((sys.executable, "su.py"))
    main()

def regwarn():
    clear_screen()
    print("Warning!\n"
          "============")
    print("\n"
          "Do not exit during Registration!\n"
          "It will break your login files!\n")
    print("\n"
          "1. Continue  | 2. Back")
    choice = user_choice()
    if choice == "1":
        register()
    if choice == "2":
        welcome()
    else:
        regwarn()
def register():
    try:
        subprocess.call(('notify-send', 'Registration', 'Please do not exit until registration is over!'))
    except:
        pass
    clear_screen()
    print("Create Account\n"
          "===============\n")
    print("1 Username  2 Password 3 Reminder 4 Avatar\n"
          "----------")
    try:
        loginw = open("user/logindata.py", "w")
    except:
        loginw = open("Aroba/user/logindata.py", "w")
    print("Name Yourself")
    choice = user_choice()
    loginw.write("USERNAME = '{}'".format(choice))
    loginw.close()
    registerp()

def registerp():
    clear_screen()
    print("Create Account\n"
          "===============\n")
    print("✓ Username  2 Password 3 Reminder 4 Avatar\n"
          "----------------------")
    try:
        loginpw = open("user/loginpass.py", "w")
    except:
        loginpw = open("Aroba/user/loginpass.py", "w")
    print("Choose a Password")
    choice = user_choice()
    if choice == "":
        input("That Password is restricted")
        registerp()
    else:
        loginpw.write("PASSWORD = '{}'".format(choice))
        loginpw.close()
        registerl()

def registerl():
    clear_screen()
    print("Create Account\n"
          "===============\n")
    print("✓ Username  ✓ Password 3 Reminder 4 Avatar\n"
          "---------------------------------")
    print("\n"
          "Would you like a password reminder msg?")
    print("\n"
          "1. Yes  | 2. No")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        try:
            rem = open("user/reminder.py", "w")
        except:
            rem = open("Aroba/user/reminder.py", "w")
        print("Create Account\n"
              "===============\n")
        print("✓ Username  ✓ Password 3 Reminder 4 Avatar\n"
              "---------------------------------")
        print("Type Reminder message")
        choice = user_choice()
        rem.write("rem = '{}'".format(choice))
        rem.close()
        registeri()
    if choice == "2":
        try:
            rem = open("user/reminder.py", "w")
        except:
            rem = open("Aroba/user/reminder.py", "w")
        rem.write("rem = 'None'")
        rem.close()
        registeri()

def registeri():
    try:
        img = open("user/img.py", "w")
    except:
        img = open("Aroba/user/img.py", "w")
    clear_screen()
    print("Create Account\n"
          "===============\n")
    print("✓ Username  ✓ Password ✓ Reminder 4 Avatar\n"
          "------------------------------------------")
    print("\n"
          "Pick an avatar!")
    print("\n"
          "1. :D\n"
          "2. ^.^\n"
          "3. ?!\n"
          "4. :)\n"
          "5. :4)\n"
          "n. None\n"
          "c. Custom")
    choice = user_choice()
    try:
        usr = open("data/restore/name.py", "w")
        usr.write("old = '{}'".format(logind.USERNAME))
        pas = open("data/restore/passw.py", "w")
        pas.write("old = '{}'".format(loginp.PASSWORD))
        usr.close()
        pas.close()
    except:
        try:
            usr = open("Aroba/data/restore/name.py", "w")
            usr.write("old = '{}'".format(logind.USERNAME))
            pas = open("Aroba/data/restore/passw.py", "w")
            pas.write("old = '{}'".format(loginp.PASSWORD))
            usr.close()
            pas.close()
        except:
            print("ERR : Backup Failed")
    if choice == "1":
        img.write("usrimg = ':D'")
        clear_screen()
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        img.write("usrimg = '^.^'")
        clear_screen()
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "3":
        img.write("usrimg = '?!'")
        clear_screen()
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "4":
        img.write("usrimg = ':)'")
        clear_screen()
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "5":
        img.write("usrimg = ':4)'")
        clear_screen()
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "n":
        img.write("usrimg = 'None'")
        clear_screen()
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))
    if choice == "c":
        clear_screen()
        print("Write an Avatar\n"
              "Recomended : Use 3 characters at most!")
        choice = user_choice()
        img.write("usrimg = '{}'".format(choice))
        clear_screen()
        input("Registration Complete!\n"
              "\n"
              "Enter")
        img.close()
        subprocess.call((sys.executable, "run.py"))

def admin():
    clear_screen()
    print("Administrative Console\n"
          "========================\n"
          "Type 'help' for help, Type 'exit' to Exit")
    choice = adconsole()
    if choice == "help":
        clear_screen()
        print("Administrative Console\n"
              "========================\n")
        print("\n"
              "***Commands***\n"
              "\n"
              "help   (Shows Help)\n"
              "uname  (Set Username)\n"
              "upass  (Set Password)\n"
              "stop   (Runs Stop Command)\n"
              "exit   (Exits Console)\n"
              "restrt (Restart ArtSystem)\n"
              "sysin  (See the System Info)\n")
        input("\n"
              "Enter")
        admin()
    if choice == "sysin":
        clear_screen()
        # Ping (str(round((t2-t1)*1000)
        try:
            import psutil
            if IS_WINDOWS:
                operate = "Win"
            if IS_MAC:
                operate = "MAC"
            else:
                operate = "GNU/Linux"
            t1 = time.perf_counter()
            time.sleep(0.678)
            t2 = time.perf_counter()
            size = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
            print("(A≈) System Information")
            print("\n"
                  "Version {}, {}\n"
                  "\n"
                  "ArtSystem Size : {}\n"
                  "Ping Time : {}\n"
                  "Running on : {}\n"
                  "\n"
                  "(c) ArtGames101".format(vr, version, size, (str(round((t2-t1)*1000))), operate))
            input("\n"
                  "Back")
            admin()
        except:
            if IS_WINDOWS:
                operate = "Win"
            if IS_MAC:
                operate = "MAC"
            else:
                operate = "GNU/Linux"
            t1 = time.perf_counter()
            time.sleep(0.678)
            t2 = time.perf_counter()
            print("(A≈) System Information")
            print("\n"
                  "Version {}, {}\n"
                  "\n"
                  "ArtSystem Size : Unknown\n"
                  "Ping Time : {}ms\n"
                  "Running on : {}\n"
                  "\n"
                  "(c) ArtGames101".format(vr, version, (str(round((t2-t1)*1000))), operate))
            input("\n"
                  "Back")
            admin()
    if choice == "restrt":
        subprocess.call((sys.executable, "run.py"))
    if choice == "uname":
        clear_screen()
        print("Administrative Console\n"
              "========================\n")
        print("Choose new name for Default User")
        choice = user_choice()
        n = open("user/logindata.py", "w")
        n.write("USERNAME = '{}'".format(choice))
        input("Set Username to {}".format(choice))
        n.close()
        admin()
    if choice == "stop":
        clear_screen()
        print("Stopped all scripts")
        sys.exit()
    if choice == "upass":
        clear_screen()
        print("Administrative Console\n"
              "========================\n")
        print("Choose a new Password for Default User")
        choice = user_choice()
        u = open("user/loginpass.py", "w")
        u.write("PASSWORD = '{}'".format(choice))
        input("Set Password to {}".format(choice))
        u.close()
        admin()
    if choice == "exit":
        welcome()
    else:
        input("[ARTSYS] {}: command not found".format(choice))
        admin()

def main():
    if c.currentgame == "snake":
        game = "snake"
    if c.currentgame == "Tetris":
        game = "Tetris"
    elif c.currentgame == "BattleSim":
        game = "BattleSim"
    elif c.currentgame == "Santa":
        game = "Santa"
    elif c.currentgame == "squirrel":
        game = "squirrel"
    elif c.currentgame == "GunRush":
        game = "GunRush"
    elif c.currentgame == "DocCreator":
        game = "DocCreator"
    elif c.currentgame == "VF":
        game = "VF"
    else:
        game = "None"
    clear_screen()
    print("========================================================\n"
          " {}        |  {}     \n"
          "========================================================\n".format(c.NAMETAG, time.ctime()))

    if game in games:
        print("(o). Disc Game ({})".format(game))
    else:
        print("(o). Disc Game (Choose)")
    print("e. ArtSystem Aroba Events/help/Changelog")
    print("s. Store")
    print("w. Quantum WebBrowser")
    print("set. Settings")
    if santa == True:
        print("sa. Santa's Gift!")
    else:
        pass
    print("n. Notifications")
    print("\n{}".format(random.choice(ad)))
    print("\n\n\n"
          " ____________________________________________________________________________________\n"
          "|a. (A≈). Start | u. Upgrade Packages | l. Load App | o. Office  | t. Tools          |\n"
          "|_______________|_____________________|_____________|____________|___________________|")
    choice = user_choice()
    if choice == "(o)":
        gm()
    if choice == "s":
        if parent.PAPASS == None:
            store()
        else:
            clear_screen()
            print("Enter Parental Control Password")
            choice = user_choice()
            if choice == parent.PAPASS:
                store()
            else:
                main()
    if choice == "e":
        events()
    if choice == "set":
        if parent.PAPASS == None:
            settings()
        else:
            clear_screen()
            print("Enter Parental Control Password")
            choice = user_choice()
            if choice == parent.PAPASS:
                settings()
            else:
                main()
    if choice == "sa":
        if santa == True:
            santagift()
        else:
            main()
    if choice == "n":
        notification()
    if choice == "l":
        loadapp()
    if choice == "o":
        office()
    if choice == "w":
        subprocess.call((sys.executable, "web/web.py"))
    if choice == "(A≈)":
        menu()
    if choice == "A":
        menu()
    if choice == "a":
        menu()
    if choice == "u":
        subprocess.call((sys.executable, "packup.py"))
    if choice == "t":
        tools()
    else:
        main()

def tools():
    clear_screen()
    print("(A≈) ArtSystem Tools\n"
          "========================")
    print("\n"
          "a. ArtSystem Antivirus\n"
          "\n"
          "s. Support\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "a":
        antivirus()
    if choice == "s":
        support()
    if choice == "0":
        main()

def support():
    clear_screen()
    print("(A≈) ArtSystem Support\n"
          "==========================")
    print("Which type of Support would you like?\n"
          "\n"
          "1. Virtual Support\n"
          "\n"
          "2. Live Support\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        vagent()
    if choice == "2":
        lagent()
    if choice == "0":
        tools()

def vagent():
    search()


def antivirus():
    clear_screen()
    print("(A≈) ArtSystem Antivirus\n"
          "      Keeping you safe!\n"
          "============================")
    print("\n"
          "Status : Protected\n"
          "\n"
          "1. Scan Now\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        antiviruscan()
    if choice == "0":
        main()

def antiviruscan():
    clear_screen()
    print("(A≈) Antivirus Scaning...\n"
          "=============================")
    print("\n"
          "Scaning Aroba Folder...")
    try:
        import Destroyer
        print("Found Destroyer! '/ '")
    except:
        pass
    try:
        import ArtUnreal
        print("Found ArtUnreal! '/ '")
    except:
        pass
    time.sleep(3)
    clear_screen()
    print("(A≈) Antivirus Scaning...\n"
          "=============================")
    print("\n"
          "Scaning Restore Folder...")
    try:
        from data.restore import Destroyer
        print("Found Destroyer! '/data/restore '")
    except:
        pass
    try:
        from data.restore import ArtUnreal
        print("Found ArtUnreal! '/data/restore '")
    except:
        pass
    time.sleep(3)
    clear_screen()
    print("(A≈) Antivirus Scaning...\n"
          "=============================")
    print("\n"
          "Scaning Web Folder...")
    try:
        from web import Destroyer
        print("Found Destroyer! '/web '")
    except:
        pass
    try:
        from web import ArtUnreal
        print("Found ArtUnreal! '/web '")
    except:
        pass
    time.sleep(3)
    clear_screen()
    print("(A≈) Antivirus Scaning...\n"
          "=============================")
    print("\n"
          "Scaning user Folder...")
    try:
        from user import Destroyer
        print("Found Destroyer! '/user '")
    except:
        pass
    try:
        from user import ArtUnreal
        print("Found ArtUnreal! '/user '")
    except:
        pass
    time.sleep(3)
    clear_screen()
    print("(A≈) Antivirus Scaning...\n"
          "=============================")
    print("\n"
          "Scaning Applications Folder...")
    try:
        from applications import Destroyer
        print("Found Destroyer! '/applications '")
    except:
        pass
    try:
        from applications import ArtUnreal
        print("Found ArtUnreal! '/applications '")
    except:
        pass
    antivirusre()

def antivirusre():
    clear_screen()
    print("(A≈) Antivirus Results\n"
          "==========================")
    print("\n"
          "Viruses Found:\n")
    try:
        import Destroyer
        print("Found Destroyer! '/ '")
    except:
        pass
    try:
        import ArtUnreal
        print("Found ArtUnreal! '/ '")
    except:
        pass
    try:
        from data.restore import Destroyer
        print("Found Destroyer! '/data/restore '")
    except:
        pass
    try:
        from data.restore import ArtUnreal
        print("Found ArtUnreal! '/data/restore '")
    except:
        pass
    try:
        from web import Destroyer
        print("Found Destroyer! '/web '")
    except:
        pass
    try:
        from web import ArtUnreal
        print("Found ArtUnreal! '/web '")
    except:
        pass
    try:
        from user import Destroyer
        print("Found Destroyer! '/user '")
    except:
        pass
    try:
        from user import ArtUnreal
        print("Found ArtUnreal! '/user '")
    except:
        pass
    try:
        from applications import Destroyer
        print("Found Destroyer! '/applications '")
    except:
        pass
    try:
        from applications import ArtUnreal
        print("Found ArtUnreal! '/applications '")
    except:
        pass
    print("\n"
          "1. Remove Viruses (RECOMMENDED)\n"
          "\n"
          "2. Ignore?")
    choice = user_choice()
    if choice == "1":
        try:
            try:
                de = open("Destroyer.py", "w")
                de.write("# Virus Removed!")
                de.close()
            except:
                pass
            try:
                au = open("ArtUnreal.py", "w")
                au.write("# Virus Removed!")
                au.close()
            except:
                pass
            try:
                aur = open("data/restore/ArtUnreal.py", "w")
                aur.write("# Virus Removed!")
                aur.close()
            except:
                pass
            try:
                der = open("data/restore/Destroyer.py", "w")
                der.write("# Virus Removed!")
                der.close()
            except:
                pass
            try:
                auw = open("web/ArtUnreal.py", "w")
                auw.write("# Virus Removed!")
                auw.close()
            except:
                pass
            try:
                dew = open("web/Destroyer.py", "w")
                dww.write("# Virus Removed!")
                dew.close()
            except:
                pass
            try:
                auu = open("user/ArtUnreal.py", "w")
                auu.write("# Virus Removed!")
                auu.close()
            except:
                pass
            try:
                deu = open("user/Destroyer.py", "w")
                deu.write("# Virus Removed!")
                deu.close()
            except:
                pass
            try:
                aua = open("applications/ArtUnreal.py", "w")
                aua.write("# Virus Removed!")
                aua.close()
            except:
                pass
            try:
                dea = open("applications/Destroyer.py", "w")
                dea.write("# Virus Removed!")
                dea.close()
            except:
                pass
            input("Removed all Possible Viruses!")
            main()
        except:
            input("Removed all Possible Viruses!")
            main()
    if choice == "2":
        main()
def office():
    clear_screen()
    print("(A≈) ArtSystem Office\n"
          "=========================\n")
    print("\n"
          "1. Text Editor (ALPHA)\n"
          "2. Calculator  (ALPHA)\n"
          "3. Paint       (Stable)\n"
          "4. PiePlayer   (BETA)\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        subprocess.call((sys.executable, "applications/aroba_apps/texteditor.py"))
    if choice == "2":
        subprocess.call((sys.executable, "applications/aroba_apps/calculator.py"))
    if choice == "3":
        subprocess.call((sys.executable, "applications/aroba_apps/brush.py"))
    if choice == "4":
        subprocess.call((sys.executable, "applications/aroba_apps/musicplayer/run.py"))
    if choice == "0":
        main()
    else:
        office()
def loadapp():
    clear_screen()
    print("(A≈) Load Application\n"
          "=========================\n\n"
          "Choose an App to run!\n"
          "(Make sure its in Python 3)\n")
    print("office {}".format(subprocess.call(("dir", "applications"))))
    print("\n"
          "0. Exit")
    choice = user_choice()
    if choice == "office":
        office()
    if choice == "0":
        main()
    else:
        try:
            subprocess.call((sys.executable, "applications/{}".format(choice)))
        except:
            try:
                print("Make Sure when doing folders to do 'folder/file'!")
                subprocess.call(("dir", "applications/{}".format(choice)))
            except:
                input("[Error] App Can not be loaded!")
                loadapp()
def gm():
    if c.currentgame == "snake":
        game = "snake"
    if c.currentgame == "Tetris":
        game = "Tetris"
    elif c.currentgame == "BattleSim":
        game = "BattleSim"
    elif c.currentgame == "Santa":
        game = "Santa"
    elif c.currentgame == "squirrel":
        game = "squirrel"
    elif c.currentgame == "GunRush":
        game = "GunRush"
    elif c.currentgame == "DocCreator":
        game = "DocCreator"
    elif c.currentgame == "VF":
        game = "VF"
    else:
        game = "None"
    clear_screen()
    print("Game Options\n"
          "================")
    print("\n"
          "1. Play | 2. Select Different Game\n"
          "          0. Back")
    print("\n"
          "If this does not work run the game through terminal!")
    choice = user_choice()
    if choice == "1":
        if game == "DocCreator":
            subprocess.call((sys.executable, "DocCreator/run.py"))
        elif game == "VF":
            subprocess.call((sys.executable, "VirtualFriend-VF/run.py"))
        elif game == "snake":
            subprocess.call(("python", "snake.py"))
        elif game == "Tetris":
            subprocess.call(("python", "tetris.py"))
        elif game == "squirrel":
            subprocess.call(("python", "squirrel.py"))
        elif game == "BattleSim":
            subprocess.call((sys.executable, "BattleSim/run.py"))
        elif game == "Santa":
            subprocess.call((sys.executable, "SantasLittleHelper/santa.py"))
        elif game == "GunRush":
            subprocess.call((sys.executable, "GunRush/run.py"))
    if choice == "2":
        gms()
    if choice == "0":
        main()

def gms():
    clear_screen()
    print("Select a Game\n"
          "================")
    print("Warning : Choose a game you own!")
    print("\n"
          "1. Snake\n"
          "2. BattleSim\n"
          "3. Squirrel\n"
          "4. Santa's Little Helper (CHRISTMAS ONLY!)\n"
          "5. Tetris\n"
          "6. Virtual Friend VF\n"
          "7. GunRush\n"
          "8. DocCreator")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        g = open("config.py", "w")
        g.write("try:\n"
                "    from user import logindata as l\n"
                "except:\n"
                "    pass\n"
                "try:\n"
                "    NAMETAG = l.USERNAME\n"
                "except:\n"
                "    NAMETAG = None\n"
                "currentgame = 'snake'\n")
        input("Push Enter!")
        g.close()
        subprocess.call((sys.executable, "data/game.py"))
    if choice == "2":
        clear_screen()
        g = open("config.py", "w")
        g.write("try:\n"
                "    from user import logindata as l\n"
                "except:\n"
                "    pass\n"
                "try:\n"
                "    NAMETAG = l.USERNAME\n"
                "except:\n"
                "    NAMETAG = None\n"
                "currentgame = 'BattleSim'\n")
        input("Push Enter!")
        g.close()
        subprocess.call((sys.executable, "data/game.py"))
    if choice == "3":
        clear_screen()
        g = open("config.py", "w")
        g.write("try:\n"
                "    from user import logindata as l\n"
                "except:\n"
                "    pass\n"
                "try:\n"
                "    NAMETAG = l.USERNAME\n"
                "except:\n"
                "    NAMETAG = None\n"
                "currentgame = 'squirrel'\n")
        input("Push Enter!")
        g.close()
        subprocess.call((sys.executable, "data/game.py"))
    if choice == "4":
        clear_screen()
        g = open("config.py", "w")
        g.write("try:\n"
                "    from user import logindata as l\n"
                "except:\n"
                "    pass\n"
                "try:\n"
                "    NAMETAG = l.USERNAME\n"
                "except:\n"
                "    NAMETAG = None\n"
                "currentgame = 'Santa'\n")
        input("Push Enter!")
        g.close()
        subprocess.call((sys.executable, "data/game.py"))
    if choice == "5":
        clear_screen()
        g = open("config.py", "w")
        g.write("try:\n"
                "    from user import logindata as l\n"
                "except:\n"
                "    pass\n"
                "try:\n"
                "    NAMETAG = l.USERNAME\n"
                "except:\n"
                "    NAMETAG = None\n"
                "currentgame = 'Tetris'\n")
        input("Push Enter!")
        g.close()
        subprocess.call((sys.executable, "data/game.py"))
    if choice == "6":
        clear_screen()
        g = open("config.py", "w")
        g.write("try:\n"
                "    from user import logindata as l\n"
                "except:\n"
                "    pass\n"
                "try:\n"
                "    NAMETAG = l.USERNAME\n"
                "except:\n"
                "    NAMETAG = None\n"
                "currentgame = 'VF'\n")
        input("Push Enter!")
        g.close()
        subprocess.call((sys.executable, "data/game.py"))
    if choice == "7":
        clear_screen()
        g = open("config.py", "w")
        g.write("try:\n"
                "    from user import logindata as l\n"
                "except:\n"
                "    pass\n"
                "try:\n"
                "    NAMETAG = l.USERNAME\n"
                "except:\n"
                "    NAMETAG = None\n"
                "currentgame = 'DocCreator'\n")
        input("Push Enter!")
        g.close()
        subprocess.call((sys.executable, "data/game.py"))
                    

def guestmain():
    if c.currentgame == "snake":
        game = "snake"
    if c.currentgame == "Tetris":
        game = "Tetris"
    elif c.currentgame == "BattleSim":
        game = "BattleSim"
    elif c.currentgame == "Santa":
        game = "Santa"
    elif c.currentgame == "squirrel":
        game = "squirrel"
    elif c.currentgame == "GunRush":
        game = "GunRush"
    elif c.currentgame == "DocCreator":
        game = "DocCreator"
    elif c.currentgame == "VF":
        game = "VF"
    else:
        game = "None"
    clear_screen()
    print("========================================================\n"
          "=. Guest        |  {}     \n"
          "========================================================\n".format(time.ctime()))

    if game in games:
        print("(o). Disc Game ({})".format(game))
    else:
        print("\a")
    print("c. Changelog")
    print("s. Store")
    print("w. Quantum WebBrowser")
    print("set. Settings")
    if santa == True:
        print("sa. Santa's Gift!")
    else:
        pass
    print("n. Notifications")
    print("\n{}".format(random.choice(ad)))
    print("\n0. Logout")
    subprocess.call((sys.executable, "su.py"))
    choice = user_choice()
    if choice == "(o)":
        if game == "DocCreator":
            subprocess.call((sys.executable, "DocCreator/run.py"))
        if game == "VF":
            subprocess.call((sys.executable, "VirtualFriend-VF/run.py"))
        if game == "snake":
            subprocess.call(("python", "snake.py"))
        if game == "Tetris":
            subprocess.call(("python", "tetris.py"))
        if game == "squirrel":
            subprocess.call(("python", "squirrel.py"))
        if game == "BattleSim":
            subprocess.call((sys.executable, "BattleSim/run.py"))
        if game == "Santa":
            subprocess.call((sys.executable, "SantasLittleHelper/santa.py"))
        if game == "GunRush":
            subprocess.call((sys.executable, "GunRush/run.py"))
    if choice == "s":
        input("Guests Can't do that!")
        guestmain()
    if choice == "c":
        changelog()
    if choice == "set":
        input("Guests Can't do that!")
        guestmain()
    if choice == "sa":
        if santa == True:
            santagift()
        else:
            guestmain()
    if choice == "n":
        notification()
    if choice == "w":
        input("Guests Can't do that!")
        guestmain()
    if choice == "=":
        guestmenu()
    if choice == "0":
        guestlogout()
    else:
        guestmain()


def notification():
    clear_screen()
    print("=====================\n"
          " Newest Notification \n"
          "=====================\n")
    try:
        print(notification.NOT)
    except:
        print("No New Notifications")
    print("\n"
          "1. Clear  | 0. Back")
    choice = user_choice()
    if choice == "1":
        rewrite = open("log/notification.py", "w")
        rewrite.write("NOT = 'None'")
    if choice == "0":
        print(".")
    else:
        notification()
def settings():
    if logind.USERNAME == "Guest":
        input("Guests cant do that!")
        guestmain()
    else:
        clear_screen()
        print("============\n"
              "  Settings  \n"
              "============\n")
        print("Change Settings here!")
        print("\a")
        print("s. System Info")
        print("u. Username")
        print("pass. Password")
        print("p. Parental Control")
        print("\n"
              "a. Advanced Settings\n"
              "r. Restart (Saves Settings)")
        print("0. Back")
        choice = user_choice()
        if choice == "s":
            sysinfo()
        if choice == "u":
            usernamec()
        if choice == "pass":
            passchange()
        if choice == "p":
            if parent.PAPASS == None:
                parentalcontrol()
            else:
                parentalsettings()
        if choice == "a":
            advancedsettings()
        if choice == "r":
            subprocess.call((sys.executable, "run.py"))
        if choice == "0":
            main()
        else:
            settings()

def advancedsettings():
    clear_screen()
    print("============\n"
          "  Advanced  \n"
          "  Settings  \n"
          "============\n")
    print("n. Change Recent Notification")
    print("u. Update Packages")
    print("l. Lobit Settings")
    print("\n"
          "Danger Zone!!!:\n"
          "\n")
    print("d. ****Delete Accoount****  (Deletes Current Account!)")
    print("\n"
          "r. Restart (Saves Settings)\n"
          "0. Back")
    choice = user_choice()
    if choice == "n":
        notifichange()
    if choice == "u":
        subprocess.call((sys.executable, "packup.py"))
    if choice == "l":
        lobitsettings()
    if choice == "d":
        deleteacc()
    if choice == "r": 
        subprocess.call((sys.executable, "run.py"))
    if choice == "0":
        settings()
    else:
        advancedsettings()

def lobitsettings():
    clear_screen()
    print("Lobit  ҉  Settings\n"
          "======================")
    try:
        from data.lobit.settings import active
    except:
        print("ed. Enable/Disable Lobit (Status : Unknown)")
    try:
        if active.active == True:
            print("ed. Enable/Disable Lobit (Status : Enabled)")
        else:
            print("ed. Enable/Disable Lobit (Status : Disabled)")
    except:
        pass
    choice = user_choice()
    if choice == "ed":
        try:
            if active.active == True:
                a = open("data/lobit/settings/active.py", "w")
                a.write("active = False")
                a.close()
                input("Lobit Disabled!")
                subprocess.call((sys.executable, "run.py"))
            if active.active == False:
                a = open("data/lobit/settings/active.py", "w")
                a.write("active = True")
                a.close()
                input("Lobit Enabled!")
                subprocess.call((sys.executable, "run.py"))
            else:
                a = open("data/lobit/settings/active.py", "w")
                a.write("active = True")
                a.close()
                input("Lobit Enabled!")
                subprocess.call((sys.executable, "run.py"))
        except:
            a = open("data/lobit/settings/active.py", "w")
            a.write("active = False")
            a.close()
            input("Lobit Disabled!")
            subprocess.call((sys.executable, "run.py"))
def sysinfo():
    clear_screen()
    # Ping (str(round((t2-t1)*1000)
    try:
        import psutil
        if IS_WINDOWS:
            operate = "Win"
        if IS_MAC:
            operate = "MAC"
        else:
            operate = "GNU/Linux"
        t1 = time.perf_counter()
        time.sleep(0.678)
        t2 = time.perf_counter()
        size = '{:.2f} MiB'.format(__import__('psutil').Process().memory_full_info().uss / 1024 ** 2)
        print("(A≈) System Information")
        print("\n"
              "Version {}, {}\n"
              "\n"
              "ArtSystem Size : {}\n"
              "Ping Time : {}\n"
              "Running on : {}\n"
              "\n"
              "(c) ArtGames101".format(vr, version, size, (str(round((t2-t1)*1000))), operate))
        input("\n"
              "Back")
        settings()
    except:
        if IS_WINDOWS:
            operate = "Win"
        if IS_MAC:
            operate = "MAC"
        else:
            operate = "GNU/Linux"
        t1 = time.perf_counter()
        time.sleep(0.678)
        t2 = time.perf_counter()
        print("(A≈) System Information")
        print("\n"
              "Version {}, {}\n"
              "\n"
              "ArtSystem Size : Unknown\n"
              "Ping Time : {}ms\n"
              "Running on : {}\n"
              "\n"
              "(c) ArtGames101".format(vr, version, (str(round((t2-t1)*1000))), operate))
        input("\n"
              "Back")
        settings()

def deleteacc():
    clear_screen()
    print("=================\n"
          " Delete Account? \n"
          "=================\n")
    print("Are You Sure you want to delete your account?")
    print("\n"
          "y. Yes  | n. No")
    choice = user_choice()
    if choice == "y":
        loginw = open("user/logindata.py", "w")
        loginpw = open("user/loginpass.py", "w")
        loginw.write("USERNAME = ")
        loginpw.write("PASSWORD = ")
        input("Enter to continue")
        loginw.close()
        loginpw.close()
        subprocess.call((sys.executable, "run.py"))
def override():
    if parent.PAPASS == None:
        clear_screen()
        print("====================\n"
              " **** Overwrite **** \n"
              "====================\n")
        print("\n"
              "Are you sure you want to Override ArtSystem this can not be undone?")
        print("\n"
              "y. Yes   | n. No")
        choice = user_choice()
        if choice == "y":
            over = open("run.py", "w")
            over.write("# You Have overwrited ArtSystem\n"
                       "print('Opps! This wont work!')")
            over.close()
            subprocess.call((sys.executable, "run.py"))
        if choice == "n":
            main()
        else:
            override()
    else:
        main()
def parentalsettings():
    clear_screen()
    print("==================\n"
          " Parental Control \n"
          "==================\n")
    print("Parental Control Settings:")
    print("\n"
          "p. Change Parental Password\n"
          "c. Clear Parental Password")
    choice = user_choice()
    if choice == "p":
        parentalcontrol()

    if choice == "c":
        par = open("user/parental.py", "w")
        par.write("PAPASS = None")
        clear_screen()
        input("Restarting...")
        par.close()
        subprocess.call((sys.executable, "run.py"))
def parentalcontrol():
    clear_screen()
    print("==================\n"
          " Parental Control \n"
          "==================\n")
    print("Enter your Account Password!")
    choice = user_choice()
    if choice == loginp.PASSWORD:
        input("Accepted!")
        parentalac()
    else:
        input("Incorrect Password!")
        settings()

def parentalac():
    clear_screen()
    print("==================\n"
          " Parental Control \n"
          "==================\n")
    print("Choose Your parental control password!")
    choice = user_choice()
    if choice == loginp.PASSWORD:
        input("You can not use your account password!")
        settings()
    else:
        par = open("user/parental.py", "w")
        par.write("PAPASS = '{}'".format(choice))
        clear_screen()
        input("Restarting...")
        par.close()
        subprocess.call((sys.executable, "run.py"))
def usernamec():
    clear_screen()
    print("============\n"
          "  Username  \n"
          "============\n")
    loginw = open("user/logindata.py", "w")
    print("\n"
          "New Username :")
    choice = user_choice()
    loginw.write("USERNAME = '{}'".format(choice))
    input("Done!")
    loginw.close()
    settings()

def passchange():
    clear_screen()
    print("============\n"
          "  Password  \n"
          "============\n")
    print("\n"
          "New Password :")
    loginpw = open("user/loginpass.py", "w")
    choice = user_choice()
    loginpw.write("USERNAME = '{}'".format(choice))
    input("Done!")
    loginpw.close()
    settings()


def santagift():
    clear_screen()
    print("You will need internet for this if you have no internet push enter!")
    print("\n"
          "Merry Christmas!")
    print("\nc. Collect")
    choice = user_choice()
    if choice == "c":
        subprocess.call(("git", "clone", "https://github.com/artsystem101/SantasLittleHelper.git"))
        subprocess.call(("git", "clone", "https://github.com/artsystem101/squirrel.git"))
        subprocess.call(("git", "clone", "https://github.com/artsystem101/snake.git"))
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/BattleSim.git"))
        gold.write("gold = True")
        input("All ArtSystem Games have been installed and also you have recieved Gold!")
        input("Unpack snake and squirrel from their folders!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Collected Santa's Gift!')")
        main()
    else:
        main()
        
        
def menu():
    clear_screen()
    print("=======\n"
          " Start \n"
          "=======\n")
    print("1. Office\n"
          "2. ArtSystem Store\n"
          "3. Settings\n"
          "  _____________________\n"
          "s.|Search              | 0. Shutdown Options\n"
          "  |____________________|\n"
          "\n"
          "e. Back")
    choice = user_choice()
    if choice == "1":
        office()
    if choice == "2":
        store()
    if choice == "3":
        settings()
    if choice == "0":
        logout()
    if choice == "s":
        search()
    if choice == "e":
        main()
    else:
        main()

def search():
    from data.lobit.settings import active
    if active.active == True:
        clear_screen()
        print("( ҉ ) Hello i am Lobit Your Personal Assistant!\n"
              "     What are you looking for?\n"
              "\n"
              "Type what you want me to search for\n"
              "\n"
              "e. Back")
        choice = user_choice()
        if choice in lrist.phra:
            if choice == lrist.sd:
                clear_screen()
                print("( ҉ ) 3...")
                time.sleep(2)
                clear_screen()
                print("( ҉ ) 2...")
                time.sleep(2)
                clear_screen()
                print("( ҉ ) 2...")
                time.sleep(2)
                clear_screen()
                print("( ҉ ) I cant self destruct but... I shutdown ArtSystem for you!")
                sys.exit(50)
            if choice == lrist.t:
                clear_screen()
                input("( ҉ ) Trojans : Little Computer Bugs things that kill EVERYTHING!")
                search()
            if choice == lrist.i:
                clear_screen()
                input("( ҉ ) Sorry but i dont feel the same. I am just a computer program")
                search()
            if choice == lrist.w:
                clear_screen()
                print("( ҉ ) ...")
                input("\n"
                      "( ҉ ) Sorry i could not respond to 'marry'")
                search()
            if choice == lrist.ww:
                clear_screen()
                print("( ҉ ) ............")
                input("\n"
                      "( ҉ ) Nope.")
                search()
        if choice == "help":
            clear_screen()
            input("( ҉ ) Exactly what im doing!")
            search()
        if choice == "store":
            clear_screen()
            print("( ҉ ) Here are two Results i found!:\n"
                  "\n"
                  "1. ArtSystem Store\n"
                  "2. Snake\n"
                  "\n"
                  "0. Search again")
            choice = user_choice()
            if choice == "1":
                store()
            if choice == "2":
                storesnake()
            if choice == "0":
                search()
        if choice == "web":
            clear_screen()
            print("( ҉ ) Here are two Results i found!:\n"
                  "\n"
                  "1. Office\n"
                  "2. Quantum WebBrowser\n"
                  "\n"
                  "0. Search again")
            choice = user_choice()
            if choice == "1":
                office()
            if choice == "2":
                subprocess.call((sys.executable, "web/web.py"))
            if choice == "0":
                search()
        if choice == "settings":
            clear_screen()
            print("( ҉ ) Here are two Results i found!:\n"
                  "\n"
                  "1. Settings\n"
                  "2. Quantum WebBrowser\n"
                  "\n"
                  "0. Search again")
            choice = user_choice()
            if choice == "1":
                settings()
            if choice == "2":
                subprocess.call((sys.executable, "web/web.py"))
            if choice == "0":
                search()
        if choice == "e":
            main()
        else:
            try:
                subprocess.call((sys.executable, "data/lobit/sai.py"))
            except:
                clear_screen()
                print("( ҉ ) I Did not understand what you searched for '{}':\n"
                      "Did you mean?:\n"
                      "\n"
                      "1. Settings\n"
                      "2. Quantum WebBrowser\n"
                      "3. System Info\n"
                      "4. How do i find the Admin Console\n"
                      "5. Tell A Joke\n"
                      "6. Who are you\n"
                      "7. Other\n"
                      "\n"
                      "0. Search again".format(choice))
                choice = user_choice()
                if choice == "1":
                    settings()
                if choice == "2":
                    subprocess.call((sys.executable, "web/web.py"))
                if choice == "3":
                    sysinfo()
                if choice == "4":
                    clear_screen()
                    input("You can Access The Admin Console when at the login page by typing 'admin'!")
                    search()
                if choice == "5":
                    joke()
                if choice == "6":
                    clear_screen()
                    print("My name is Lobit ҉  and i am Your Personal Assistant for ArtSystem!\n"
                          "I can help you find Applications that you are looking for, Tell Jokes,\n"
                          "And Help you find information about ArtSystem!\n"
                          "\n"
                          "I cant Wait to help you!")
                    input("\n"
                          "Back")
                    search()
                if choice == "0":
                    search()
    if active.active == False:
        clear_screen()
        print("( ҉ ) Opps! Looks like i have been disabled!")
        input(".")
        main()
    else:
        main()

def joke():
    clear_screen()
    jokes = ["How do all the oceans say hello to each other?\n\nThey Wave", "What do you call a bear with no teeth?\n\nA Gummy bear", "What did one wall say to the other wall?\n\nMeet you at the corner", "What do you call cheese that isn't yours?\n\nNacho Cheese", "Where do cows go for entertainment?\n\nThe Moo-vies", "What do you call a pig that knows Karate?\n\nA Pork Chop!", "Why did the fish jump out of the water?\n\nBecause the sea-weed", "Why are Ghosts bad liars?\n\nBecaue you can see right through them"]
    input("( ҉ ) Here you Go!\n"
          "\n"
          "{}".format(random.choice(jokes)))
    search()
def loop():
    r = ["Ha", "LOOOOOOOOOOOOOOOOOLP", "Restart to exit!", "lololodloefokog", "fuywefuwegfuyehf", "My name is Jeff", "idk"]
    input("{} | Push Enter".format(random.choice(r)))
    loop()
def logout():
    clear_screen()
    print("==========\n"
          "  Logout  \n"
          "==========\n")
    print("1. Restart")
    print("2. Shutdown")
    print("3. Wait")
    print("4. Logout")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        clear_screen()
        print("\n"
              "     /------------\      \n"
              "    /              \     \n"
              "   /                \    \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |__________________|   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "\n"
              "        ArtSystem        \n")
        print("Shutdown!")
        sys.exit(1)
    if choice == "3":
        wait()
    if choice == "4":
        welcome()
    if choice == "0":
        main()
    else:
        logout()

def guestlogout():
    clear_screen()
    print("==========\n"
          "  Logout  \n"
          "==========\n")
    print("1. Restart")
    print("2. Shutdown")
    print("3. Logout")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        clear_screen()
        print("\n"
              "     /------------\      \n"
              "    /              \     \n"
              "   /                \    \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |__________________|   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "  |                  |   \n"
              "\n"
              "        ArtSystem        \n")
        print("Shutdown!")
        sys.exit(1)
    if choice == "3":
        welcome()
    if choice == "0":
        guestmain()
    else:
        guestlogout()

        
def wait():
    clear_screen()
    print("========\n"
          "  Wait  \n"
          "========\n")
    print("10. 10 Secs")
    print("20. 20 Secs")
    print("30. 30 Secs")
    print("40. 40 Secs")
    print("50. 50 Secs")
    print("60. 1 Min")
    print("70. 1 Min 10 Secs")
    print("80. 1 Min 20 Secs")
    choice = user_choice()
    if choice == "10":
        time.sleep(10)
        main()
    if choice == "20":
        time.sleep(20)
        main()
    if choice == "30":
        time.sleep(30)
        main()
    if choice == "40":
        time.sleep(40)
        main()
    if choice == "50":
        time.sleep(50)
        main()
    if choice == "60":
        time.sleep(60)
        main()
    if choice == "70":
        time.sleep(70)
        main()
    if choice == "80":
        time.sleep(80)
        main()


def events():
    clear_screen()
    print("(A≈) ArtSystem\n"
          "==================")
    print("\n"
          "c. Changelog\n"
          "\n"
          "e. Events\n"
          "\n"
          "h. Help\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "c":
        changelog()
    if choice == "e":
        eevents()
    if choice == "h":
        try:
            subprocess.call(("guide/help.html"))
        except:
            try:
                subprocess.call(("guide\help.html"))
            except:
                events()
    if choice == "0":
        main()

def eevents():
    clear_screen()
    print("(A≈) ArtSystem Events\n"
          "=========================")
    print("\n"
          "Events:\n"
          "\n"
          "1. Started Support\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        print("(A≈) Started ArtSystem Support\n"
              "==================================")
        print("\n"
              "ArtSystem Has Started Support!\n"
              "\n"
              "Aroba Has now got Live/Virtual Support\n"
              "\n"
              "Live Support:\n"
              "The ArtGames team are not always online\n"
              "but if we are online we can help you straight away!\n"
              "\n"
              "Virtual Help:\n"
              "Virtual help is always online and is intergrated into\n"
              "your ArtSystem!\n"
              "The Virtual Assistant cant help with everything!")
        input("\n"
              "Back")
        eevents()
    if choice == "0":
        events()
    
def changelog():
    clear_screen()
    print("=================\n"
          "    Changelog    \n"
          "=================\n")
    print("Whats New in {}?".format(version))
    print("\n"
          "* Added Lobit (Personal Assistant)\n"
          "* Added Load Application page\n"
          "* Updated Start Menu\n"
          "* Added Built-in apps\n"
          "* Added System Info\n"
          "* Added Better Password Protection\n"
          "* Added More Console Commands\n"
          "* Added Full System Restore\n"
          "* Changed Menu\n"
          "* Changed Login Screen\n"
          "* Added Events Page\n"
          "\n"
          " Too Much to Actualy add in changelog")
    print("\n"
          "<. Last Update   | 0. Back")
    choice = user_choice()
    if choice == "<":
        lastupdate()
    if choice == "0":
        events()

def lastupdate():
    clear_screen()
    print("=================\n"
          "    Changelog    \n"
          "=================\n")
    print("Whats Was in the last update?!?!")
    print("\n"
          "* Nothing...")
    input("\nBack")
    changelog()
    
def store():
    if logind.USERNAME == "Guest":
        input("Guests Cant do that!")
        main()
    else:
        clear_screen()
        print("=================\n"
              " ArtSystem Store \n"
              "=================\n")
        print("Categories:")
        print("1. Featured")
        print("2. Games")
        print("3. Apps")
        print("4. Lobit Upgrades")
        print("4. Passes")
        print("0. Back")
        choice = user_choice()
        if choice == "1":
            featured()
        if choice == "2":
            storegames()
        if choice == "3":
            apps()
        if choice == "4":
            lobitup()
        if choice == "5":
            passes()
        if choice == "0":
            main()

def lobitup():
    clear_screen()
    print("================\n"
          " Lobit Upgrades \n"
          "================\n")
    print("\n"
          "1. Talk to Lobit (AI) (ArtSystem)\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        storelobitsai()
    if choice == "0":
        store()

def featured():
    clear_screen()
    print("================\n"
          "    Featured    \n"
          "================\n")
    print("The top 3 games and apps are here!\n\n")
    print("1. BattleSim (ArtGames101)")
    print("2. Snake (Pygame)")
    print("3. GunRush (MrBackPack)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storebattlesim()
    if choice == "2":
        storesnake()
    if choice == "3":
        storegunrush()
    if choice == "0":
        store()

def passes():
    clear_screen()
    print("=================\n"
          "     Passes      \n"
          "=================\n")
    print("1. Gold  (ArtSystem)")
    print("2. Alphapps  (ArtSystem)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        gogold()
    if choice == "2":
        goalphapps
    if choice == "0":
        store()

def apps():
    clear_screen()
    print("=================\n"
          "      Apps       \n"
          "=================\n")
    print("1. Py Web Browser   (ArtGames101)")
    print("2. Document Creator (ArtGames101)")
    print("3. VirtualFriend VF (ArtGames101)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storeweb()
    if choice == "2":
        storedoc()
    if choice == "3":
        storevf()
    if choice == "0":
        store()

def storelobitsai():
    clear_screen()
    print("Talk to Lobit (AI)\n"
          "\n"
          "Description:\n"
          "You can talk to lobit\n"
          "\n"
          "Publisher:\n"
          "MrBackPack & ArtSystem\n")
    try:
        from data.lobit import tai
        print("Installed")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        clear_screen()
        print("Creating AI file...")
        ai = open("data/lobit/tai.py", "w")
        ai.write("# -*- coding: utf-8 -*-\n"
                 "# Lobit (c) MrBackPack 2018\n"
                 "import sys, os, random, lobsp\n"
                 "\n"
                 "def main():\n"
                 "    print('( ҉ )'.format(random.choice(lobsp.s)))\n")
        ai.close()
        time.sleep(3)
        clear_screen()
        print("Creating Text files...")
        txt = open("data/lobit/lobsp.py", "w")
        txt.write("# Lobit (c) MrBackPack 2018\n"
                  "import random\n"
                  "\n"
                  "s = ['Ok', 'hello', 'yes', 'im not sure', 'no', 'how are you', 'good']")
        txt.close()
        time.sleep(2)
        clear_screen()
        input("Done!")
        storelobitsai()
        
def storeweb():
    clear_screen()
    print("Py Web Browser\n"
          "\n"
          "Description:\n"
          "Search the web!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    print("Installed!")
    print("0. Back")
    choice = user_choice()
    if choice == "0":
        storegames()

def storevf():
    clear_screen()
    print("VirtualFriend VF\n"
          "\n"
          "Description:\n"
          "Have Fun with your own Virtual Friend\n"
          "That has lots of features!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/VirtualFriend-VF.git"))
        input("Installed!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (GunRush)')")
        storetetris()
    if choice == "0":
        storegames()
        
def storedoc():
    clear_screen()
    print("Document Creator\n"
          "\n"
          "Description:\n"
          "Create Documents!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    if alpha.A == True:
        try:
            import DocCreator
            print("Installed!")
        except:
            print("i. Install  (With Alphapps Pass!)")
    else:
        print("Get Alphapps to install!")
    choice = user_choice()
    if choice == "i":
        if alpha.A == True:
            subprocess.call(("git", "clone", "https://github.com/artsystem101/DocCreator.git"))
            input("Installed!")
            notifi = open("log/notification.py", "w")
            notifi.write("import time\n"
                         "NOT = '{} |  {}'.format(time.ctime(), 'Installed App (Document Creator)')")
            storedoc()
        else:
            input("Install Alphapps Pass to Get this!")
            storedoc()
    if choice == "0":
        apps()
def storegames():
    clear_screen()
    print("=================\n"
          "      Games      \n"
          "=================\n")
    print("1. Snake  (Pygame)")
    print("2. Battle Sim  (ArtGames101)")
    print("3. Squirrel (Pygame)  (GOLD!)")
    print("4. Santas Little Helper (ArtGames101)  (Christmas Gift!)")
    print("5. Tetris  (ArtGames101)")
    print("6. GunRush (MrBackPack)")
    print("0. Back")
    choice = user_choice()
    if choice == "1":
        storesnake()
    if choice == "2":
        storebattlesim()
    if choice == "3":
        storesquirrel()
    if choice == "4":
        slh()
    if choice == "5":
        storetetris()
    if choice == "6":
        storegunrush()
    if choice == "0":
        store()

def storegunrush():
    clear_screen()
    print("GunRush\n"
          "\n"
          "Description:\n"
          "None\n"
          "\n"
          "Publisher:\n"
          "MrBackPack\n")
    try:
        from GunRush import run
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/GunRush.git"))
        input("Installed!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (GunRush)')")
        storetetris()
    if choice == "0":
        storegames()
def storetetris():
    clear_screen()
    print("Tetris\n"
          "\n"
          "Description:\n"
          "Stack Blocks and get as many rows as you can!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    try:
        import tetris
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/artsystem101/tetris.git"))
        input("Installed!")
        input("To Unpack tetris game move tetris.py & the mid files from the tetris folder!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (Tetris)')")
        storetetris()
    if choice == "0":
        storegames()

def slh():
    clear_screen()
    print("Santa's Little Helper\n"
          "\n"
          "Description:\n"
          "Help Santa Deliver Presents to Children\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    if santa == True:
        try:
            import SantasLittleHelper
            print("Installed!")
        except:
            print("i. Install  (For Christmas)")
    else:
        print("Install on Christmas Updates!")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        if santa == True:
            subprocess.call(("git", "clone", "https://github.com/artsystem101/SantasLittleHelper.git"))
            input("Installed!")
            input("Merry Christmas (Your game does not need unpacking!)")
            notifi = open("log/notification.py", "w")
            notifi.write("import time\n"
                         "NOT = '{} |  {}'.format(time.ctime(), 'Installed Exclusive Game (Santas little helper!)')")
            slh()
        else:
            slh()
    if choice == "0":
        storegames()

def storesquirrel():
    clear_screen()
    print("Squirrel\n"
          "\n"
          "Description:\n"
          "Kill Smaller Squirrels to become the OMEGA SQUIRREL\n"
          "\n"
          "Publisher:\n"
          "Pygame\n")
    if g.gold == True:
        try:
            import squirrel
            print("Installed!")
        except:
            print("i. Install  (With Gold Pass!)")
    else:
        print("Go Gold to install!")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        if g.gold == True:
            subprocess.call(("git", "clone", "https://github.com/artsystem101/squirrel.git"))
            input("Installed!")
            input("To Unpack squirrel game move squirrel.py and squirrel.png from the squirrel folder!")
            notifi = open("log/notification.py", "w")
            notifi.write("import time\n"
                         "NOT = '{} |  {}'.format(time.ctime(), 'Installed Gold Game (Squirrel)')")
            storesquirrel()
        else:
            storesquirrel()
    if choice == "0":
        storegames()

def storesnake():
    clear_screen()
    print("Snake\n"
          "\n"
          "Description:\n"
          "Eat as many apples as you can without loosing!\n"
          "\n"
          "Publisher:\n"
          "Pygame\n")
    try:
        import snake
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/artsystem101/snake.git"))
        input("Installed!")
        input("To Unpack snake game move snake.py from the snake folder!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (Snake)')")
        storesnake()
    if choice == "0":
        storegames()

def storebattlesim():
    clear_screen()
    print("Battle Sim\n"
          "\n"
          "Description:\n"
          "Battle Enemies & unlock characters!\n"
          "\n"
          "Publisher:\n"
          "ArtGames101\n")
    try:
        from BattleSim import run
        print("\nInstalled!")
    except:
        print("i. Install")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        subprocess.call(("git", "clone", "https://github.com/ArtGames101/BattleSim.git"))
        input("Installed!")
        input("Your Game Doesnt Need unpacking!")
        notifi = open("log/notification.py", "w")
        notifi.write("import time\n"
                     "NOT = '{} |  {}'.format(time.ctime(), 'Installed Game (Battle Sim)')")
        storebattlesim()
    if choice == "0":
        storegames()


def gogold():
    clear_screen()
    print("*Gold Game Pass*\n"
          "\n"
          "Description:\n"
          "Get Special Access to store games that have not been released!\n"
          "\n"
          "Publisher:\n"
          "ArtSystem\n")
    if g.gold == True:
        print("\nActive!")
    else:
        print("\ni. Go Gold!")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        gold.write("gold = True")
        input("Gold Pass Updated!")
        gogold
    if choice == "0":
        passes()

def goalphapps():
    clear_screen()
    print("*Alphapps*\n"
          "\n"
          "Description:\n"
          "Get Special Access to Apps!!!!\n"
          "\n"
          "Publisher:\n"
          "ArtSystem\n")
    if alpha.A == True:
        print("\nActive!")
    else:
        print("\ni. Get Alphapps")
    print("0. Back")
    choice = user_choice()
    if choice == "i":
        gold.write("A = True")
        input("Alphapps Pass Updated!")
        goalphapps
    if choice == "0":
        passes()


if upg.stay == True:
    if anew.new == True:
        new()
    else:
        warn()
else:
    subprocess.call((sys.executable, "ArtSystem/run.py"))
