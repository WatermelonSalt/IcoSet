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
|    InfoTip=Some sensible information |
+--------------------------------------+
"""

import sys

from Modules import OptionHandler, ManualIconSet, BatchIconSet

if __name__ == "__main__":

    OptionHandler.handleOptions(sys.argv)

    if OptionHandler.manual is True:

        manualoption = OptionHandler.manualargument

        if manualoption == '':

            manualoption = 1

        ManualIconSet.execute(repeat = manualoption)

    if OptionHandler.batch is True:

        BatchIconSet.execute(OptionHandler.batchargument)
