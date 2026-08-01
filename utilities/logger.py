import logging
import os


class LogGenerator:

    @staticmethod
    def loggen():

        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger()

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            "logs/aytomation.log",
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger