import sys, os, subprocess, time
from doc import doco, doct, docth
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
    try:
        print("(A≈) ArtSystem Text Editor\n"
              "==============================\n")
        print("\n"
              "1. {}\n"
              "\n"
              "2. {}\n"
              "\n"
              "3. {}\n"
              "\n"
              "0. Back".format(doco.title, doct.title, docth.title))
        choice = user_choice()
        if choice == "1":
            doc1()
        if choice == "2":
            doc2()
        if choice == "3":
            doc3()
        if choice == "0":
            print("Txt Exit")
    except:
        print("\n"
              ":( ArtSystem Text Editor has encounted an error!")
        print("\n"
              "Options:\n"
              "\n"
              "1. Reset Document one\n"
              "\n"
              "2. Reset Document two\n"
              "\n"
              "3. Reset Document three\n"
              "\n"
              "4. Reset All Documents\n"
              "\n"
              "0. Exit (This may be a glitch!)")
        choice = user_choice()
        if choice == "1":
            one = open("doc/doco.py", "w")
            one.write("title = 'Untitled'\n"
                      "\n"
                      "text = 'None'")
            one.close()
            subprocess.call((sys.executable, "texteditor.py"))
        if choice == "2":
            two = open("doc/doct.py", "w")
            two.write("title = 'Untitled'\n"
                      "\n"
                      "text = 'None'")
            two.close()
            subprocess.call((sys.executable, "texteditor.py"))
        if choice == "3":
            thr = open("doc/docth.py", "w")
            thr.write("title = 'Untitled'\n"
                      "\n"
                      "text = 'None'")
            thr.close()
            subprocess.call((sys.executable, "texteditor.py"))
        if choice == "4":
            one = open("doc/doco.py", "w")
            one.write("title = 'Untitled'\n"
                      "\n"
                      "text = 'None'")
            one.close()
            two = open("doc/doct.py", "w")
            two.write("title = 'Untitled'\n"
                      "\n"
                      "text = 'None'")
            two.close()
            thr = open("doc/docth.py", "w")
            thr.write("title = 'Untitled'\n"
                      "\n"
                      "text = 'None'")
            thr.close()
            subprocess.call((sys.executable, "texteditor.py"))
        if choice == "0":
            main()
            

def doc1():
    clear_screen()
    print("{}\n"
          "======================\n".format(doco.title))
    print("\n"
          "1. Edit\n"
          "\n"
          "2. View\n"
          "\n"
          "0. Back\n")
    choice = user_choice()
    if choice == "1":
        doce1()
    if choice == "2":
        docv1()
    if choice == "0":
        main()

def doce1():
    clear_screen()
    print("Enter A New Doc Title\n"
          "=========================")
    choice1 = user_choice()
    clear_screen()
    print("Enter Document Text\n"
          "=======================")
    print("Note : type \n for new paragraph")
    choice2 = user_choice()
    clear_screen()
    docu1 = open("doc/doco.py", "w")
    docu1.write("title = '{}'\n"
                "\n"
                "text = '{}'".format(choice1, choice2))
    docu1.close()
    input("Document Created!")
    subprocess.call(sys.executable, "texteditor.py")

def docv1():
    clear_screen()
    print("{}\n"
          "=======================\n"
          "\n"
          "{}".format(doco.title, doco.text))
    input("\n"
          "Back")
    doc1()
    
def doc2():
    clear_screen()
    print("{}\n"
          "======================\n".format(doct.title))
    print("\n"
          "1. Edit\n"
          "\n"
          "2. View\n"
          "\n"
          "0. Back\n")
    choice = user_choice()
    if choice == "1":
        doce2()
    if choice == "2":
        docv2()
    if choice == "0":
        main()

def doce2():
    clear_screen()
    print("Enter A New Doc Title\n"
          "=========================")
    choice1 = user_choice()
    clear_screen()
    print("Enter Document Text\n"
          "=======================")
    print("Note : type 'backslash n' for new paragraph")
    choice2 = user_choice()
    clear_screen()
    docu2 = open("doc/doct.py", "w")
    docu2.write("title = '{}'\n"
                "\n"
                "text = '{}'".format(choice1, choice2))
    docu2.close()
    input("Document Created!")
    subprocess.call(sys.executable, "texteditor.py")

def docv2():
    clear_screen()
    print("{}\n"
          "=======================\n"
          "\n"
          "{}".format(doct.title, doct.text))
    input("\n"
          "Back")
    doc2()

def doc3():
    clear_screen()
    print("{}\n"
          "======================\n".format(docth.title))
    print("\n"
          "1. Edit\n"
          "\n"
          "2. View\n"
          "\n"
          "0. Back\n")
    choice = user_choice()
    if choice == "1":
        doce3()
    if choice == "2":
        docv3()
    if choice == "0":
        main()

def doce3():
    clear_screen()
    print("Enter A New Doc Title\n"
          "=========================")
    choice1 = user_choice()
    clear_screen()
    print("Enter Document Text\n"
          "=======================")
    print("Note : type \n for new paragraph")
    choice2 = user_choice()
    clear_screen()
    docu3 = open("doc/docth.py", "w")
    docu3.write("title = '{}'\n"
                "\n"
                "text = '{}'".format(choice1, choice2))
    docu3.close()
    input("Document Created!")
    subprocess.call(sys.executable, "texteditor.py")

def docv3():
    clear_screen()
    print("{}\n"
          "=======================\n"
          "\n"
          "{}".format(docth.title, docth.text))
    input("\n"
          "Back")
    doc1()
main()
