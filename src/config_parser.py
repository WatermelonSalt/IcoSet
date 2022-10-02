from json import load
from os import listdir
from os.path import isdir, splitext, basename

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

            if isdir(dir):

                yield dir

                logger.logger.debug(f"Facilitated path to {dir} in mode 'dir'")

            else:

                logger.logger.debug(
                    f"{dir} is not a directory, did not facilitate path")

    def encapsulating_facilitator(self, dir_file=True, src=None):

        for path in (self.paths["encapsulating"] if not src else (src if type(src) is list else [src])):

            if isdir(path):

                if dir_file:

                    yield path

                for dir in listdir(path):

                    if isdir(f"{path}/{dir}") == dir_file:

                        yield f"{path}/{dir}"

                        logger.logger.debug(
                            f"Facilitated path to {path}/{dir} in mode 'encapsulating'")

                    else:

                        logger.logger.debug(
                            f"{path}/{dir} is not a {'directory' if dir_file else 'file'}, did not facilitate path")

            else:

                logger.logger.debug(
                    f"Skipping {path} as it is not a {'directory' if dir_file else 'file'}"
                )

    def recurse_facilitator(self):

        dirs_to_recurse = []

        for path in self.paths["recurse"]:

            if isdir(path):

                dirs_to_recurse.append(path)

                logger.logger.debug(
                    f"Added {path} to the list of directories to be recursed"
                )

            else:

                logger.logger.debug(
                    f"Skipping {path} as it is not a directory"
                )

        while dirs_to_recurse:

            yield dirs_to_recurse[0]

            logger.logger.debug(
                f"Facilitated path to {dirs_to_recurse[0]} in mode 'recurse'"
            )

            for dir in listdir(dirs_to_recurse[0]):

                if isdir(f"{dirs_to_recurse[0]}/{dir}"):

                    dirs_to_recurse.append(f"{dirs_to_recurse[0]}/{dir}")

                    logger.logger.debug(
                        f"Added {dirs_to_recurse[0]}/{dir} to the list of directories to be recursed"
                    )

                else:

                    logger.logger.debug(
                        f"Skipping {dirs_to_recurse[0]}/{dir} as it is not a directory"
                    )

            dirs_to_recurse.pop(0)

    def icons_facilitator(self):

        icons = dict()

        for path in self.paths["icon_sources"]:

            if (isdir(path) == 0 and (splitext(path)[1] == ".ico")):

                icons[splitext(basename(path))[0]] = path

                logger.logger.debug(
                    f"Added {path} to the list of icon sources under the alias '{splitext(basename(path))[0]}'")

            else:

                logger.logger.debug(
                    f"{path} is a directory, icons will be sourced with 'encapsulated' mode")

                for file_path in self.encapsulating_facilitator(dir_file=False, src=path):

                    if splitext(file_path)[1] == ".ico":

                        icons[splitext(basename(file_path))[0]] = file_path

                        logger.logger.debug(
                            f"Added {file_path} to the list of icon sources under the alias '{splitext(basename(file_path))[0]}'")
