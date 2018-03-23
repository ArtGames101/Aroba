import subprocess, sys, os, time, webbrowser
import name

# Extention Load
try:
    from snowtheme import snowtheme as st
    snow = open(".extdata/snowtheme.txt", "w")
    snow.write("# SnowTheme by MrBackPack\n"
               "\n"
               "__Publisher__ : {}\n"
               "__version__ : {}\n"
               "\n"
               "[{}]".format(st.publisher, st.v, time.ctime()))
    print("snowtheme loaded")
    snow.close()
except:
    pass

# Website open : webbrowser.open(URL)

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
    print("Welcome!")
    try:
        if st.st == True:
            print("+   +   +   +   +   +   +   +   +\n"
                  "+1. Search +| 2. Suggested Sites+\n")
            print("  +   + 0. Exit +  +   +   +   + ")
        else:
            print("\n"
                  "1. Search | 2. Suggested Sites\n")
            print("     0. Exit")
    except:
        print("\n"
              "1. Search | 2. Suggested Sites\n")
        print("     0. Exit")
    choice = user_choice()
    if choice == "1":
        search()
    if choice == "2":
        suggested()
    if choice == "3":
        extentions()
    if choice == "4":
        hhelp()
    if choice == "0":
        sys.exit(1)

def extentions():
    clear_screen()
    print("Quantum Extentions\n"
          "======================")
    print("\n"
          "1. Browse Extentions\n"
          "2. Manage Extentions\n"
          "\n"
          "0. Back")
    choice = user_choice()
    if choice == "1":
        shopext()
    if choice == "2":
        manext()
    if choice == "0":
        main()

def shopext():
    clear_screen()
    print("\n"
          "Quantum Extentions\n"
          "======================")
    print("\n"
          "1. The Only Extention\n"
          "\n"
          "0. Back")
    clear_screen()
    choice = user_choice()
    if choice == "1":
        snowthemeext()
    if choice == "0":
        extentions()

def manext():
    clear_screen()
    print("\n"
          "Quantum Extentions\n"
          "======================")
    try:
        from snowtheme import snowtheme
        print("st. Snowtheme")
    except:
        pass
    print("\n"
          "0. Back")
    choice = user_choice()
    if choice == "st":
        try:
            from snowtheme import snowtheme
            snowthemedata()
        except:
            input("Error: Have you got this extention?")
            manext()
    if choice == "0":
        extentions()

def snowthemedata():
    clear_screen()
    print("SnowTheme   | Theme")
    print("\n"
          "Data:\n"
          "\n"
          "__Publisher__: {}\n"
          "\n"
          "__Version__: {}\n".format(st.publisher, st.v))
    
def search():
    clear_screen()
    print("Welcome {}".format(name.name))
    try:
        if st.st == True:
            print("+   +   +   +   +\n"
                  "+Enter URL Below+")
        else:
            print("\n"
                  "Enter URL Below")
    except:
        print("\n"
              "Enter URL Below")
    choice = user_choice()
    webbrowser.open(choice)
    main()

def suggested():
    clear_screen()
    print("Welcome {}".format(name.name))
    try:
        if st.st == True:
            print("+   +   +   +   +   +   +   +   +   +   +   +\n"
                  "+Suggested Sites:+\n"
                  "  +   +   +   +   +   +   +   +   +   +   +\n"
                  "1. +https://google.com.au+\n"
                  "2. +https://youtube.com+\n"
                  "3. +https://github.com+\n"
                  "4. +https://github.com/ArtSystemStudios/Vortex+\n"
                  "5. +https://github.com/ArtGames101+\n"
                  "\n"
                  "0. +Back+")
        else:
            print("\n"
                  "Suggested Sites:\n"
                  "\n"
                  "1. https://google.com.au\n"
                  "2. https://youtube.com\n"
                  "3. https://github.com\n"
                  "4. https://github.com/ArtSystemStudios/Vortex\n"
                  "5. https://github.com/ArtGames101\n"
                  "\n"
                  "0. Back")
    except:
        print("\n"
              "Suggested Sites:\n"
              "\n"
              "1. https://google.com.au\n"
              "2. https://youtube.com\n"
              "3. https://github.com\n"
              "4. https://github.com/ArtSystemStudios/Vortex\n"
              "5. https://github.com/ArtGames101\n"
              "\n"
              "0. Back")
    choice = user_choice()
    if choice == "1":
        webbrowser.open("https://google.com.au")
    if choice == "2":
        webbrowser.open("https://youtube.com")
    if choice == "3":
        webbrowser.open("https://github.com")
    if choice == "4":
        webbrowser.open("https://github.com/ArtSystem/Vortex")
    if choice == "5":
        webbrowser.open("https://github.com/ArtGames101")
    if choice == "0":
        main()
    else:
        main()
main()
