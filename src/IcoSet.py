from sys import argv
from colorama import Fore, init, deinit
import argparse

if __name__ == "__main__":

    init()

    argument_processor = argparse.ArgumentParser(prog=f"{Fore.GREEN}icoset{Fore.RESET}", description=f"{Fore.CYAN}A to\
ol to set icons to directories with ease{Fore.RESET}")

    argument_processor.add_argument(
        "-c", "--config-path",
        action="store",
        type=str,
        nargs="?",
        const="./",
        default="none",
        metavar="PATH",
        help="Path to configuration file")

    argument_processor.add_argument(
        "-i", "--interactive",
        action="store_true",
        help="Operate the program in interactive mode"
    )

    processed_arguments = vars(argument_processor.parse_args(argv[1:]))
    print(processed_arguments)

    deinit()
