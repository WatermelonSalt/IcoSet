import getopt
import json
import os

from colorama import init, Fore

init()


def setIcons(function):

    def wrapper(*args, **kwargs):

        function(*args, **kwargs)

        if function.__name__.endswith('CommonFoldersOnly'):

            for folder in args[0].PathFromCommonFolders:

                path = args[0].CommonFolders + folder

                os.system(f'''attrib +r "{path}"''')
                os.system(f'''attrib +s +h "{path}"/desktop.ini''')
                print(f"{Fore.GREEN}Icon set successfully for {Fore.YELLOW}{path}")

        if function.__name__.endswith('NonCommonFolders'):

            for folder in args[0].NonCommonFolderPaths:

                os.system(f'''attrib +r "{folder}"''')
                os.system(f'''attrib +s +h "{folder}/desktop.ini"''')
                print(f"{Fore.GREEN}Icon set successfully for {Fore.YELLOW}{folder}")

    return wrapper


class SetIconsFromConfig:

    def getConfigJson(self, argument):

        config = open(argument, 'r').read()
        config = json.loads(config)
        self.CommonFolders = config['CommonFolders']
        self.PathFromCommonFolders = config['PathFromCommonFolders']
        self.CommonIconsFolder = config['CommonIconsFolder']
        self.PathFromCommonIconsFolder = config['PathFromCommonIconsFolder']
        self.NonCommonFolderPaths = config['Non-CommonFolderPaths']
        self.NonCommonIconPaths = config['Non-CommonIconPaths']
        self.CommonToolTips = config['CommonToolTips']
        self.NonCommonToolTips = config['Non-CommonToolTips']

    @setIcons
    def generateDesktopiniforCommonFoldersOnly(self):

        for index, folder in enumerate(self.PathFromCommonFolders):

            path = self.CommonFolders + folder

            print(f"{Fore.YELLOW}{path} {Fore.GREEN}added to queue")

            with open(f"{path}/desktop.txt", "w+") as inifile:

                contents = f"""[.ShellClassInfo]
IconFile = {self.CommonIconsFolder}/{self.PathFromCommonIconsFolder[index]}
IconIndex = 0
InfoTip = {self.CommonToolTips[index]}
"""
                print(contents, file=inifile)

            inifile.close()

            try:

                os.rename(f"{path}/desktop.txt", f"{path}/desktop.ini")

            except FileExistsError:

                os.remove(f"{path}/desktop.ini")
                os.rename(f"{path}/desktop.txt", f"{path}/desktop.ini")

    @setIcons
    def generateDesktopiniforNonCommonFolders(self):

        for index, folder in enumerate(self.NonCommonFolderPaths):

            print(f"{Fore.YELLOW}{folder} {Fore.GREEN}added to queue")

            with open(f"{folder}/desktop.txt", "w+") as inifile:

                contents = f"""[.ShellClassInfo]
IconFile = {self.NonCommonIconPaths[index]}
IconIndex = 0
InfoTip = {self.NonCommonToolTips[index]}
"""
                print(contents, file=inifile)

            inifile.close()

            try:

                os.rename(f"{folder}/desktop.txt", f"{folder}/desktop.ini")

            except FileExistsError:

                os.remove(f"{folder}/desktop.ini")
                os.rename(f"{folder}/desktop.txt", f"{folder}/desktop.ini")


def execute(argument):

    Setter = SetIconsFromConfig()

    print(f"{Fore.GREEN}Getting the config file...")
    Setter.getConfigJson(argument)
    print(f"{Fore.MAGENTA}Got the config file from {Fore.YELLOW}{argument} {Fore.GREEN}successfully")
    print(f"{Fore.WHITE}Trying to set icons...")
    Setter.generateDesktopiniforCommonFoldersOnly()
    Setter.generateDesktopiniforNonCommonFolders()
    print(f"{Fore.MAGENTA}Icons set successfully")
