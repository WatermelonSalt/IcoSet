import os
import sys
import tkinter as tk
from tkinter import filedialog

from colorama import Fore, init

init()
root = tk.Tk()
root.withdraw()


def checkSelectedFile():

    global choice
    global icon_path

    if icon_path.endswith(".ico") is False:

        if check == 0:

            print(f"{Fore.RED}Unable to get the resource")
            print(
                f"{Fore.RED}You selected the wrong file type again!\nThe program will now continue to the next try")

            return 0

        print(
            f"{Fore.RED}Seems like you selected a {Fore.CYAN}'{os.path.splitext(icon_path)[1]}'{Fore.RED} file instead of a {Fore.CYAN}'.ico'{Fore.RED} file")
        print(f"{Fore.GREEN}If you would like to try again enter {Fore.YELLOW}1{Fore.GREEN} in the following prompt and {Fore.YELLOW}0{Fore.GREEN} if you would like to quit")
        try:

            choice = int(input(
                f"{Fore.WHITE}Enter {Fore.YELLOW}1 {Fore.WHITE}or{Fore.YELLOW} 0 {Fore.WHITE}: "))

            analyseChoices()

        except Exception as ex:

            print(f"{Fore.RED}{ex} has occured!\nTry again!")
            try:

                choice = int(input(
                    f"{Fore.WHITE}Enter {Fore.YELLOW}1 {Fore.WHITE}or{Fore.YELLOW} 0 {Fore.WHITE}: "))

                analyseChoices()

            except Exception as ex:

                print(f"{Fore.RED}{ex} has occured\nThe program will now presume that you wanted to exit and do so\nPlease launch the program again to try again!")
                choice = 0

                analyseChoices()


def analyseChoices():

    global choice
    global check
    global icon_path
    global result

    if choice == 1:

        check = 0
        icon_path = filedialog.askopenfilename(
            initialdir="/", title="Select Icon file", filetypes=(("Icon Files", "*.ico"), ("All Files", "*.*")))

        result = checkSelectedFile()

    elif choice == 0:

        print(f"{Fore.RED}The program will exit now")
        sys.exit()

    else:

        print(
            f"{Fore.RED}Your choice is not in the provided choices\nThe program will exit now")
        sys.exit()


def setIcon(function):

    global folder_path

    def wrapper(*args, **kwargs):

        function(*args, **kwargs)

        os.system(f'''attrib +r "{folder_path}"''')
        os.system(f'''attrib +s +h "{folder_path}"/desktop.ini''')
        print(f"{Fore.GREEN}Icon set successfully")

    return wrapper


@setIcon
def generateDesktopini():

    global folder_path
    global icon_path

    with open(f"{folder_path}/desktop.txt", "w+") as inifile:

        contents = f"""[.ShellClassInfo]
IconFile = {icon_path}
IconIndex = 0
InfoTip = {ToolTip}
"""
        print(contents, file=inifile)

    inifile.close()

    try:

        os.rename(f"{folder_path}/desktop.txt", f"{folder_path}/desktop.ini")

    except FileExistsError:

        os.remove(f"{folder_path}/desktop.ini")
        os.rename(f"{folder_path}/desktop.txt", f"{folder_path}/desktop.ini")


def execute(repeat = 1):

    global folder_path
    global icon_path
    global ToolTip
    global choice
    global check
    global result

    result = 1

    for trynumber in range(0, repeat):

        print(f"{Fore.GREEN}Try number : {trynumber + 1}")

        print(f"{Fore.GREEN}Getting the folder to set the icon")

        folder_path = filedialog.askdirectory()

        print(f"{Fore.GREEN}Got the folder as {Fore.YELLOW}{folder_path} {Fore.GREEN}successfully")
        print(f"{Fore.GREEN}Trying to get the icon resource")

        icon_path = filedialog.askopenfilename(
            initialdir="/", title="Select Icon file", filetypes=(("Icon Files", "*.ico"), ("All Files", "*.*")))
        choice = 1
        check = 1

        checkSelectedFile()

        if result == 0:

            continue

        else:

            print(f"{Fore.GREEN}Got the resource as {Fore.YELLOW}{icon_path} {Fore.GREEN}successfully")

        print(f"{Fore.GREEN}Getting ToolTip string")

        ToolTip = input(
            f"{Fore.CYAN}Enter any information that you want to show as a tool tip when hovering above a folder : ")

        print(f"{Fore.GREEN}Got the ToolTip string successfully")

        print(f"{Fore.BLUE}Setting icon for {folder_path}")
        generateDesktopini()
