
import sys, os, subprocess, time

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
    print("(A≈) Calculator\n"
          "===================\n")
    print("\n"
          "Choose Your First Number\n"
          "\n"
          "e. Exit")
    nu = user_choice()
    if nu == "e":
        print("Cal Exit")
    else:
        nu1 = nu
        clear_screen()
        print("(A≈) Calculator\n"
              "===================\n")
        print("\n"
              "Choose your Second Number\n"
              "\n"
              "e. Exit")
        n = user_choice()
        if n == "e":
            print("Cal Exit")
        else:
            nu2 = n
            a = nu1 + nu2
            clear_screen()
            print("(A≈) Calculator\n"
                  "===================\n")
            print("\n"
                  "{}\n"
                  "\n"
                  "1. Calculate Another\n"
                  "0. Exit".format(a))
            choice = user_choice()
            if choice == "1":
                main()
            if choice == "0":
                print("Cal Exit")

main()
