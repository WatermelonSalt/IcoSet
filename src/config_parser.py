from json import load

import logger
from os import listdir
from os.path import isdir


class Configurator:

    def __init__(self, config_file_path):

        self.config_file_path = config_file_path
        self.get_paths()

    def get_paths(self):

        with open(self.config_file_path) as config:

            self.paths = load(config)

        logger.logger.debug(self.paths)

    def dir_facilitator(self):

        for dir in self.paths["dir"]:

            yield dir

            logger.logger.debug(f"Facilitated path to {dir} in mode 'dir'")

    def encapsulating_facilitator(self):

        for path in self.paths["encapsulating"]:

            for dir in listdir(path):

                if isdir(f"{path}/{dir}"):

                    yield dir

                    logger.logger.debug(
                        f"Facilitated path to {dir} in mode 'encapsulating'")

                else:

                    logger.logger.debug(
                        f"{dir} is not a directory, did not facilitate path")
