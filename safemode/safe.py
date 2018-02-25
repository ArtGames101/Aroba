# ArtSystem (c) ArtGames101 2018
import sys, os, random, subprocess, time, psutil

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def start():
    clear_screen()
    print("ArtSystem Safe Mode")
    subprocess.call((sys.executable, "su.py"))
    main()
def main():
    clear_screen()
    print("Administrator     | SafeMode\n"
          "================================")
    print("\n"
          "c. Command Prompt\n"
          "\n"
          "s. Security Options\n")
    choice = user_choice()
    if choice == "c":
        admin()
    if choice == "s":
        security()
    else:
        main()

def admin():
    clear_screen()
    print("Administrative Console\n"
          "========================\n"
          "Type 'help' for help, Type 'exit' to Exit")
    choice = user_choice()
    if choice == "help":
        clear_screen()
        print("Administrative Console\n"
              "========================\n")
        print("\n"
              "***Commands***\n"
              "\n"
              "help   (Shows Help)\n"
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
        input("WIP")
        admin()
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
        subprocess.call((sys.executable, "safe.py"))
    if choice == "stop":
        clear_screen()
        print("Stopped all scripts")
        sys.exit()
    if choice == "exit":
        main()
    else:
        input("[ARTSYS] {}: command not found".format(choice))
        admin()

def security():
    clear_screen()
    print("System Status : Safe\n"
          "\n"
          "Enter")
    input(".")
    main()

start()
