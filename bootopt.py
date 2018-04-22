import sys, os, subprocess, time
os.system("setterm -background blue -foreground white")
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
    print("(A≈) Boot Options\n"
          "=====================")
    print("\n"
          "1. Run ArtSystem\n"
          "2. Run Safe Mode\n"
          "3. Run Safe Mode (With Networking)\n"
          "4. Run Restore Module\n"
          "5. Run Upgrade Module\n"
          "6. Run Linux Launcher\n"
          "\n"
          "0. Exit")
    choice = user_choice()
    if choice == "1":
        subprocess.call((sys.executable, "run.py"))
    if choice == "2":
        subprocess.call((sys.executable, "safemode/safe.py"))
    if choice == "3":
        subprocess.call((sys.executable, "safemode/safen.py"))
    if choice == "4":
        subprocess.call((sys.executable, "sysrestore.py"))
    if choice == "5":
        subprocess.call((sys.executable, "upgrade.py"))
    if choice == "6":
        try:
            subprocess.call(("./run.sh"))
        except:
            os.system("run.sh")
    if choice == "0":
        sys.exit()

main()
