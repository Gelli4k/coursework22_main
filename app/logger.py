import logging


def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    file_handler = logging.FileHandler("basic.txt")
    logger.addHandler(file_handler)

    formatter = logging.Formatter("%(asc_time)s [%(level_name)s] %(message)s")
    file_handler.setFormatter(formatter)

    return logger
