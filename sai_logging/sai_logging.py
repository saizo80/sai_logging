import logging
from io import StringIO
import os
from datetime import datetime
class Logger(object):
    def __init__(self, log_file_name: str = None, log_level: int = 20):
        """
        :param log_file_name: The name of the log file to write to
        :param log_level: The level of logging to use
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)
        self.level = log_level
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        if log_file_name:
            self.__compress_log_file(log_file_name)
            file_handler = logging.FileHandler(log_file_name)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(10)
            self.logger.addHandler(file_handler)
        self.stream = StringIO()
        stream_handler = logging.StreamHandler(self.stream)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    def info(self, msg: str):
        now = datetime.now()
        self.logger.info(msg)
        now = now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        if self.level <= 20:
            print(f'{now} - INFO - {msg}')

    def error(self, msg: str):
        now = datetime.now()
        self.logger.error(msg)
        now = now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        if self.level <= 40:
            print(f'{now} - ERROR - {msg}')

    def warning(self, msg: str):
        now = datetime.now()
        self.logger.warning(msg)
        now = now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        if self.level <= 30:
            print(f'{now} - WARNING - {msg}')

    def debug(self, msg: str):
        now = datetime.now()
        self.logger.debug(msg)
        now = now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        if self.level <= 10:
            print(f'{now} - DEBUG - {msg}')

    def critical(self, msg: str):
        now = datetime.now()
        self.logger.critical(msg)
        now = now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        if self.level <= 50:
            print(f'{now} - CRITICAL - {msg}')

    def fatal(self, msg: str):
        now = datetime.now()
        self.logger.fatal(msg)
        now = now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
        if self.level <= 50:
            print(f'{now} - FATAL - {msg}')

    def get_log(self) -> str:
        return self.stream.getvalue()

    def __compress_log_file(self, log_file_name: str):
        """
        Compresses the log file to gz if over 1MB
        """
        if os.path.exists(log_file_name):
            if os.path.getsize(log_file_name) > 1000000:
                import gzip, shutil

                with open(log_file_name, "rb") as f_in:
                    with gzip.open(log_file_name + ".gz", "ab") as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(log_file_name)
                open(log_file_name, "w+").close()
