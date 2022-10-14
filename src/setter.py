from functools import wraps
from os import remove, rename, system
from os.path import basename

import logger


class Icon_Setter:

    def __init__(self, parser):

        self.parser = parser

    def icon_setter(self, func):

        @wraps(func)
        def actual_setter(*args, **kwargs):

            for directory in func(*args, **kwargs):

                with open(f"{directory}/desktop.txt", "w+") as ini:

                    try:

                        ini.write(f"[.ShellClassInfo]\n" +
                                  f"IconFile = {self.icon_sources[f'{basename(directory)}']}\n" +
                                  f"IconIndex = 0")

                        logger.logger.debug(
                            f"ini file successfully written for {directory}")

                    except KeyError as msg:

                        logger.logger.info(
                            f"Skipping {directory} as icon source for it doesn't exist")

                try:

                    rename(f"{directory}/desktop.txt",
                           f"{directory}/desktop.ini")

                except FileExistsError:

                    remove(f"{directory}/desktop.ini")
                    rename(f"{directory}/desktop.txt",
                           f"{directory}/desktop.ini")

                system(f'attrib +r "{directory}"')
                system(f'attrib +s +h "{directory}"/desktop.ini')

        return actual_setter

    def set_icons(self):

        logger.logger.debug("Gathering icon sources...")

        self.icon_sources = self.parser.icons_facilitator()

        logger.logger.debug("Icon sources gathered")
        logger.logger.debug(
            "Starting icon setting job for directories listed using option 'dir'")
        self.icon_setter(self.parser.dir_facilitator)()
        logger.logger.debug(
            "Icon setting job completed for directories listed using option 'dir'")
        logger.logger.debug(
            "Starting icon setting job for directories listed using option 'encapsulating'")
        self.icon_setter(self.parser.encapsulating_facilitator)()
        logger.logger.debug(
            "Icon setting job completed for directories listed using option 'encapsulating'")
        logger.logger.debug(
            "Starting icon setting job for directories listed using option 'recurse'")
        self.icon_setter(self.parser.recurse_facilitator)()
        logger.logger.debug(
            "Icon setting job completed for directories listed using option 'recurse'")
