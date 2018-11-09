import logging
from logging.handlers import RotatingFileHandler


class BitLog:
    def __init__(self):
        self.log_formatter = logging.Formatter(
            '%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

        self.logFile = 'log.txt'

        self.my_handler = RotatingFileHandler(self.logFile, mode='a', maxBytes=1*1024*1024,
                                              backupCount=2, encoding=None, delay=0)
        self.my_handler.setFormatter(self.log_formatter)
        self.my_handler.setLevel(logging.INFO)

        self.app_log = logging.getLogger('root')
        self.app_log.setLevel(logging.INFO)

        self.app_log.addHandler(self.my_handler)

    def log(self, message):
        self.app_log.info(message)
