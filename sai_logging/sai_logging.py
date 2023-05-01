import gzip
import logging
import os
import shutil
import sys
from io import StringIO

from .color_format import LinuxColorFormatter, DiscordColorFormatter


class Logger(object):
    def __init__(
        self,
        log_file: str = None,
        color: bool = True,
        stream_level: int = 20,
        file_level: int = 10,
        log_stdout: bool = True,
        stdout_level: int = 20,
    ):
        """
        :param log_file: The name of the log file to write to (default: None)
        :param color: Whether or not to use color in the console (default: True)
        :param stream_level: The level of the stream handler (default: INFO)
        :param file_level: The level of the file handler (default: DEBUG)
        :param log_stdout: Whether or not to log to stdout (default: True)
        :param stdout_level: The level of the stdout handler (default: INFO)
        """
        # make the logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(10)

        # add logger formatting
        if color:
            formatter = LinuxColorFormatter()
            discord_formatter = DiscordColorFormatter()
        else:
            formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        # add the file handler if a log file is specified
        if log_file:
            self._compress_log_file(log_file)
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            file_handler.setLevel(file_level)
            self.logger.addHandler(file_handler)

        # add the stream handler
        self.stream = StringIO()
        stream_handler = logging.StreamHandler(self.stream)
        stream_handler.setFormatter(discord_formatter)
        stream_handler.setLevel(stream_level)
        self.logger.addHandler(stream_handler)

        # add stdout handler
        if log_stdout:
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setFormatter(formatter)
            stdout_handler.setLevel(stdout_level)
            self.logger.addHandler(stdout_handler)

    def info(self, msg: str):
        """log `msg` with severity 'INFO'"""
        self.logger.info(msg)

    def error(self, msg: str):
        """log `msg` with severity 'ERROR'"""
        self.logger.error(msg)

    def warning(self, msg: str):
        """log `msg` with severity 'WARNING'"""
        self.logger.warning(msg)

    def debug(self, msg: str):
        """log `msg` with severity 'DEBUG'"""
        self.logger.debug(msg)

    def critical(self, msg: str):
        """log `msg` with severity 'CRITICAL'"""
        self.logger.critical(msg)

    def fatal(self, msg: str):
        """log `msg` with severity 'CRITICAL'"""
        self.logger.fatal(msg)

    def get_log(self) -> str:
        """return the full log as a string"""
        return self.stream.getvalue()

    def _compress_log_file(self, log_file_name: str):
        """
        Compresses the log file to gz if over 1MB
        """
        if os.path.exists(log_file_name):
            if os.path.getsize(log_file_name) > 1000000:
                with open(log_file_name, "rb") as f_in:
                    with gzip.open(log_file_name + ".gz", "ab") as f_out:
                        shutil.copyfileobj(f_in, f_out)
                os.remove(log_file_name)
