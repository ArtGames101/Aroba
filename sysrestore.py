import sys, os, random, time, subprocess

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
    print("(A≈) System Restore\n"
          "=======================\n")
    print("\n"
          "Would You Like to Reset ArtSystem\n"
          "\n"
          "1. Yes\n"
          "\n"
          "2. No\n")
    choice = user_choice()
    if choice == "1":
        restore()
    if choice == "2":
        sys.exit(1)

def restore():
    clear_screen()
    print("1 Restore Launcher  2 Reset Users  3 Check Restore\n"
          "------------------")
    print("\n"
          "Restoring Launcher...")
    run = open("run.py", "w")
    backup = open("data/restore/launcher.py", "r")
    run.write("{}".format(restore))
    run.close()
    clear_screen()
    print("✓ Restore Launcher  2 Reset Users  3 Check Restore\n"
          "---------------------------------")
    print("\n"
          "Reseting Users...")
    user = open("user/logindata.py", "w")
    passw = open("user/loginpass.py", "w")
    user.write("USERNAME = 'Unknown'")
    passw.write("PASSWORD = 'Unknown'")
    user.close()
    passw.close()
    clear_screen()
    print("✓ Restore Launcher  ✓ Reset Users  3 Check Restore\n"
          "---------------------------------------------------")
    print("\n"
          "Checking Restore...")
    time.sleep(5)
    clear_screen()
    print("✓ Restore Launcher  ✓ Reset Users  ✓ Check Restore\n"
          "---------------------------------------------------")
    print("\n"
          "What was the Reason of you Restoring ArtSystem?\n"
          "\n"
          "1. Virus\n"
          "\n"
          "2. Modified Code\n"
          "\n"
          "3. Other\n")
    choice = user_choice()
    if choice == "1":
        virus()
    if choice == "2":
        mod()
    if choice == "3":
        other()

def virus():
    clear_screen()
    print("(A≈) Virus\n"
          "==============")
    print("\n"
          "We care about your Privacy!\n"
          "\n"
          "Some Viruses that have been created for ArtSystem can\n"
          "Destroy ArtSystem Completely or just steal Document data!\n"
          "\n"
          "Please report them on the ArtSystem Github Page!\n"
          "https://github.com/ArtGames101/Aroba\n"
          "\n"
          "If you did encounter one we will patch it! (Make Sure to Specify What it did!)\n")
    input("\n"
          "Enter")
    done()

def mod():
    clear_screen()
    print("(A≈) Modified Code/Software\n"
          "===============================")
    print("\n"
          "We At ArtSystem dont mind if you Modify Code as long as\n"
          "\n"
          "* You know what you are doing\n"
          "* You dont cause damage to your ArtSystem\n"
          "\n"
          "*** If A Module says dont Tamper With dont Modify it! ***\n")
    input("\n"
          "Enter")
    done()

def other():
    clear_screen()
    print("(A≈) Other Restore Reason\n"
          "=============================")
    print("\n"
          "We Like to hear your Feedback/Suggestions!\n"
          "\n"
          "Please State the Reason you Restored ArtSystem!")
    choice = user_choice()
    clear_screen()
    print("(A≈) Other Restore Reason\n"
          "=============================")
    print("\n"
          "{}\n"
          "Make sure if this is a problem/error to report it!\n".format(choice))
    input("\n"
          "Enter")
    done()

def done():
    clear_screen()
    print("(A≈) Thanks!\n"
          "=============================")
    print("\n"
          "Your ArtSystem has been restored!\n"
          "If Restore does not work copy 'data/restore/launcher.py'\n"
          "And replace run with it!\n")
    print("\n"
          "1. Restore Again\n"
          "\n"
          "2. Continue to ArtSystem\n"
          "\n"
          "0. Exit")
    choice = user_choice()
    if choice == "1":
        main()
    if choice == "2":
        subprocess.call((sys.executable, "run.py"))
    if choice == "0":
        sys.exit()

main()
