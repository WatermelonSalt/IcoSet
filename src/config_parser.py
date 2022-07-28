from json import load

import logger


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
