import tkinter as tk
from os import remove, rename, system
from os.path import basename
from tkinter import filedialog

import logger


class Interactor:

    root = tk.Tk()
    root.withdraw()

    def get_paths(self):

        logger.logger.debug("Getting directory path using interactive dialog")

        self.directory = filedialog.askdirectory()

        logger.logger.debug(
            "Successfully got directory path using interactive dialog")
        logger.logger.debug(
            f"Getting icon file path for {self.directory} using interactive dialog")

        self.icon = filedialog.askopenfilename(
            initialdir="/",
            title=f"Select icon file for {basename(self.directory)}",
            filetypes=(("Icons", "*.ico"), ("All files", "*.*")))

        logger.logger.debug(
            f"Successfully got icon file path for {self.directory} using interactive dialog")

    def set_icon(self):

        with open(f"{self.directory}/desktop.txt", "w+") as ini:

            ini.write(f"[.ShellClassInfo]\n" +
                      f"IconFile = {self.icon}\n" +
                      f"IconIndex = 0")

            logger.logger.debug(
                f"ini file proto text successfully written for {self.directory} in interactive mode")

        logger.logger.debug(
            f"Attempting to rename txt to ini for {self.directory} in interactive mode")

        try:

            rename(f"{self.directory}/desktop.txt",
                   f"{self.directory}/desktop.ini")

        except FileExistsError:

            remove(f"{self.directory}/desktop.ini")
            rename(f"{self.directory}/desktop.txt",
                   f"{self.directory}/desktop.ini")

        logger.logger.debug(
            f"ini file successfully written for {self.directory} in interactive mode")
        logger.logger.debug(
            f"Attempting to set perms for {self.directory} in interactive mode")

        system(f'attrib +r "{self.directory}"')
        system(f'attrib +s +h "{self.directory}"/desktop.ini')

        logger.logger.debug(
            f"Successfully set perms for {self.directory} in interactive mode")
