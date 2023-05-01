import logging


class LinuxColorFormatter(logging.Formatter):
    white = "\033[0;37m"
    gray = "\033[0;30m"
    yellow = "\033[33;20m"
    red = "\033[31;20m"
    bold_red = "\033[31;1m"
    reset = "\033[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: white + format + reset,
        logging.INFO: format,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class DiscordColorFormatter(logging.Formatter):
    white = "\033[0;37m"
    gray = "\033[0;30m"
    yellow = "\033[33;20m"
    red = "\033[31;20m"
    bold_red = "\033[31;1m"
    reset = "\033[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: gray + format + reset,
        logging.INFO: white + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
