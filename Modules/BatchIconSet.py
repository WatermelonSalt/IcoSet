import getopt
import json
import os

from colorama import init, Fore

init()


def setIcons(function):

    def wrapper(*args, **kwargs):

        function(*args, **kwargs)

        if function.__name__.endswith('CommonFolders'):

            for folder in args[0].FolderPaths_Common:

                path = args[0].CommonFoldersPath + folder

                os.system(f'''attrib +r "{path}"''')
                os.system(f'''attrib +s +h "{path}"/desktop.ini''')
                print(f"{Fore.GREEN}Icon set successfully for {Fore.YELLOW}{path}")

        if function.__name__.endswith('NonCommonFolders'):

            for folder in args[0].FolderPaths_NonCommon:

                os.system(f'''attrib +r "{folder}"''')
                os.system(f'''attrib +s +h "{folder}/desktop.ini"''')
                print(f"{Fore.GREEN}Icon set successfully for {Fore.YELLOW}{folder}")

    return wrapper


class SetIconsFromConfig:

    def getConfigJson(self, argument):

        config = open(argument, 'r').read()
        config = json.loads(config)
        self.CommonFoldersPath = config['CommonFoldersPath']
        self.FolderPaths_Common = config['FolderPaths_Common']
        self.IconPaths_Common = config['IconPaths_Common']
        self.CommonIconsPath = config['CommonIconsPath']
        self.FolderPaths_NonCommon = config['FolderPaths_Non-Common']
        self.IconPaths_NonCommon = config['IconPaths_Non-Common']
        self.ToolTips_Common = config['ToolTips_Common']
        self.ToolTips_NonCommon = config['ToolTips_Non-Common']

    @setIcons
    def generateDesktopiniforCommonFolders(self):

        for index, folder in enumerate(self.FolderPaths_Common):

            path = self.CommonFoldersPath + folder

            print(f"{Fore.YELLOW}{path} {Fore.GREEN}added to queue")

            with open(f"{path}/desktop.txt", "w+") as inifile:

                contents = f"""[.ShellClassInfo]
IconFile = {self.CommonIconsPath}/{self.IconPaths_Common[index]}
IconIndex = 0
InfoTip = {self.ToolTips_Common[index]}
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

        for index, folder in enumerate(self.FolderPaths_NonCommon):

            print(f"{Fore.YELLOW}{folder} {Fore.GREEN}added to queue")

            with open(f"{folder}/desktop.txt", "w+") as inifile:

                contents = f"""[.ShellClassInfo]
IconFile = {self.IconPaths_NonCommon[index]}
IconIndex = 0
InfoTip = {self.ToolTips_NonCommon[index]}
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
    Setter.generateDesktopiniforCommonFolders()
    Setter.generateDesktopiniforNonCommonFolders()
    print(f"{Fore.MAGENTA}Icons set successfully")
