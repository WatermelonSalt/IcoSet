import logging
from datetime import datetime


logger = logging.getLogger("IcoSet")


def toggle_logger(logger_state):

    if logger_state:

        logger.setLevel(logging.DEBUG)

        console_handle = logging.StreamHandler()
        file_handle = logging.FileHandler(
            f'IcoSet_{datetime.now().__str__().replace("-", "").replace(":", "").replace(" ", "").replace(".", "")}.log', mode="w+")

        console_handle.setLevel(logging.WARNING)
        file_handle.setLevel(logging.DEBUG)

        console_handle.setFormatter(logging.Formatter(
            "%(name)s > %(levelname)s > %(message)s"))
        file_handle.setFormatter(logging.Formatter(
            "%(process)d > %(asctime)s > %(name)s > %(levelname)s > %(message)s"))

        logger.addHandler(console_handle)
        logger.addHandler(file_handle)

    else:

        logger.setLevel(100)
