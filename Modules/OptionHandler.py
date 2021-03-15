import getopt
import sys
from collections import Counter

from colorama import Fore, init

init()


def giveHelp():

    helptext = f"""
{Fore.MAGENTA}IconSetter Help
{Fore.YELLOW}---------------

{Fore.GREEN}Usage: IcoSet [Options]

{Fore.RED}Order of options does not matter

{Fore.GREEN}Options:


{Fore.MAGENTA}Short        Long        Action
{Fore.YELLOW}-----        ----        ------

{Fore.CYAN}-m           --manual    This option makes the program work in manual mode

{Fore.CYAN}-c           --config    This option takes in a config file which must be provided to make this program work in batch mode
{Fore.CYAN}                         Provide the path to the config file as an argument

{Fore.CYAN}-h           --help      This option shows this help message

{Fore.MAGENTA}Arguments
{Fore.YELLOW}---------

{Fore.CYAN}-m repeat=<number>   {Fore.RED}Default is 1

{Fore.CYAN}-c <path/to/your/config.json>    {Fore.RED}Must include the extension

{Fore.CYAN}-h {Fore.RED}No Arguments
"""

    print(helptext)


def splitOptsVar(opts_var):

    options = []
    arguments = []

    for option, argument in opts_var:

        options.append(option)
        arguments.append(argument)

    return options, arguments


def manualModeParsing(optionlist, argumentlist):

    global manual
    global manualargument

    for index, option in enumerate(optionlist):

        if option in ("-m", "--manual"):

            manual = True
            manualargument = argumentlist[index]

            break

        else:

            manual = False


def batchModeParsing(optionlist, argumentlist):

    global batch
    global batchargument

    for index, option in enumerate(optionlist):

        if option in ("-c", "--config"):

            batch = True
            batchargument = argumentlist[index]

            break

        else:

            batch = False


def checkMultipleSameOptions(optionlist):

    status = True

    allelementscount = Counter(optionlist)

    for elementcount in allelementscount.values():

        if elementcount > 1:

            status = False

            break

    return status


def filterOnlyHelp(optionlist):

    global nohelp

    nohelp = False

    status = True

    if optionlist.count("-h") or optionlist.count("--help") is True:

        for index, option in enumerate(optionlist):

            if index == 0 and option in ("-h", "--help"):

                try:

                    status = False
                    optionlist[index + 1]

                except:

                    status = True

                    break

            if index != 0 and index == len(optionlist) - 1 and option in ("-h", "--help"):

                status = False

                break

            if index != 0 and index != len(optionlist) - 1 and option in ("-h", "--help"):

                status = False

                break

    else:

        status = False
        nohelp = True

    return status


def checkUnallowedCombos(optionlist):

    allelementscount = Counter(optionlist)

    if((allelementscount["-m"] == 1 or allelementscount["--manual"] == 1) and (allelementscount["-c"] == 1 or allelementscount["--config"] == 1)):

        print(f"{Fore.RED}You cannot use {Fore.YELLOW}'-m'/'--manual' {Fore.RED}and {Fore.YELLOW}'-c'/'--config' {Fore.RED}at the same time\nThe Program will exit now")
        sys.exit()


def handleOptions(argv):

    try:

        opts, errs = getopt.getopt(
            argv[1:], shortopts="c:hm", longopts=["config=", "help", "manual"])

    except Exception as exp:

        print(f"{Fore.RED}{exp}\n\n{Fore.BLUE}The program will exit now")
        sys.exit()

    options, arguments = splitOptsVar(opts)

    if errs != []:

        print(f"{Fore.RED}Options were not passed correctly!")
        print(f"{Fore.GREEN}Please try again with proper options")
        sys.exit()

    if opts == []:

        print(
            f"{Fore.BLUE}Hmm, seems like you don't know how to use me\nWell, here is some help")
        giveHelp()
        sys.exit()

    if checkMultipleSameOptions(options) is True:

        pass

    else:

        print(f"{Fore.RED}You seem to use an option more than once which is not allowed.\nThe program will now exit")
        sys.exit()

    if filterOnlyHelp(options) is True:

        giveHelp()

    elif nohelp == True:

        pass

    else:

        print(f"{Fore.RED}You seem to use other options along with the 'help' option which should not be done.\nThe program will now exit")
        sys.exit()

    checkUnallowedCombos(options)
    manualModeParsing(options, arguments)
    batchModeParsing(options, arguments)
