import sys, os, subprocess, time

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")
        
def main():
    clear_screen()
    print("Upgrading Packages...")
    try:
        subprocess.call(("git", "pull", "https://github.com/ArtGames101/Aroba.git"))
        time.sleep(4)
        clear_screen()
        input("Updated!")
    except:
        clear_screen()
        print("Unable to Update Packages!")
        input(".")
        sys.exit()
    sys.exit()

main()
