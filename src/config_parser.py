from json import load

import logger


class Configurator:

    def __init__(self, config_file_path):

        self.config_file_path = config_file_path

    def get_paths(self):

        with open(self.config_file_path) as config:

            self.paths = load(config)

        logger.logger.debug(self.paths)
