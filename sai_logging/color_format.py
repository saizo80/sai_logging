import logging


class ColorFormatter(logging.Formatter):
    pink = "\033[0;35m"
    gray = "\033[38;20m"
    yellow = "\033[33;20m"
    red = "\033[31;20m"
    bold_red = "\033[31;1m"
    reset = "\033[0m"
    format = "%(asctime)s - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: gray + format + reset,
        logging.INFO: pink + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
