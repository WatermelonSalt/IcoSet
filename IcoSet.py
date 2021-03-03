#! Python3.9.1

"""
* This script sets the icons to the folder automatically if executed
* Do it once and keep it for ever
* Uses a json file to read configs from
? To make life easier for people
? This script modifies the desktop.ini file for each folder to acheive this

 Structure of a normal desktop.ini
=== === === === === === === === ===
+--------------------------------------+
|    [.ShellClassInfo]                 |
|    ConfirmFileOp=0                   |
|    NoSharing=1                       |
|    IconFile=Folder.ico               |
|    IconIndex=0                       |
|    InfoTip=Some sensible information.|
+--------------------------------------+
"""

import os
import sys
import getopt
import json


def givehelp():

    helptext = """
IconSetter Help
---------------

Usage: IcoSet [Options]

Order of options does matter

Options:

Short       Long        Action
-----       ----        ------

-c          --config    This option takes in a config file which must be provided to make this program work
                        Provide the path to the config file as an argument

-h          --help      This option shows this help message
"""

    print(helptext)


def setIcons(function):

    def wrapper(*args, **kwargs):

        function(*args, **kwargs)

        if function.__name__.endswith('CommonFolders'):

            for folder in args[0].FolderPaths_Common:

                path = args[0].CommonFoldersPath + folder

                os.system(f'''attrib +r "{path}"''')
                os.system(f'''attrib +s +h "{path}"/desktop.ini''')

        if function.__name__.endswith('NonCommonFolders'):

            for folder in args[0].FolderPaths_NonCommon:

                os.system(f'''attrib +r "{folder}"''')
                os.system(f'''attrib +s +h "{folder}/desktop.ini"''')

    return wrapper


class IcoSet:

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


if __name__ == "__main__":

    Setter = IcoSet()

    opts, args = getopt.getopt(
        sys.argv[1:], shortopts="c:h", longopts=["config=", "help"])

    if opts == []:

        print("Your usage might not be correct, check out this help")
        givehelp()
        sys.exit()

    for option, argument in opts:

        if option in ("--help", "-h"):

            givehelp()
            sys.exit()

        elif option in ("-c", "--config"):

            Setter.getConfigJson(argument)
            Setter.generateDesktopiniforCommonFolders()
            Setter.generateDesktopiniforNonCommonFolders()
