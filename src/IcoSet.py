import argparse
from sys import argv

from colorama import Fore, deinit, init

import logger
from config_parser import Configurator

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

    argument_processor.add_argument(
        "-l", "--log",
        action="store_true",
        help="Enable / Disable logging"
    )

    processed_arguments = vars(argument_processor.parse_args(argv[1:]))

    logger.toggle_logger(processed_arguments["log"])

    logger.logger.info(f"Parsed Arguments : {processed_arguments}")

    config_parser = Configurator(processed_arguments["config_path"])

    deinit()
