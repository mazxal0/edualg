from datetime import datetime
import logging
import time
from enum import Enum


class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    SUCCESS = 5


class Ploggy:
    COLORS = {
        LogLevel.DEBUG: "\033[97m",  # зелёный
        LogLevel.INFO: "\033[94m",  # синий
        LogLevel.WARNING: "\033[93m",  # жёлтый
        LogLevel.ERROR: "\033[91m",  # красный
        LogLevel.SUCCESS: "\033[92m",
        "END": "\033[0m"
    }

    def __init__(self, prefix="Ploggy"):
        self.prefix = prefix

    def log(self, message, level: LogLevel=LogLevel.INFO):
        color = self.COLORS[level]
        end = self.COLORS["END"]
        t = datetime.now().strftime("%H:%M:%S")
        print(f'{color}[{self.prefix}] [{level.name}] {message} [{t}] {end}')

    @staticmethod
    def slog(message, level: LogLevel=LogLevel.INFO):
        color = Ploggy.COLORS[level]
        end = Ploggy.COLORS["END"]
        t = datetime.now().strftime("%H:%M:%S")
        print(f'{color}[PLOGGY] [{level.name}] {message} [{t}] {end}')

    def debug(self, message):
        self.log(message, level=LogLevel.DEBUG)

    def info(self, message):
        self.log(message, level=LogLevel.INFO)

    def warning(self, message):
        self.log(message, level=LogLevel.WARNING)

    def error(self, message):
        self.log(message, level=LogLevel.ERROR)

    def success(self, message):
        self.log(message, level=LogLevel.SUCCESS)

    def log_function(self, level: LogLevel=LogLevel.DEBUG):
        def decorator(func):
            def wrapper(*args, **kwargs):
                self.log(f'Enter {func.__name__}(){' with ' if args or kwargs else ""}{'args=' if args else ""}{args}{' and ' if args and kwargs else ""}{'kwargs=' if kwargs else ""}{kwargs if kwargs else ""}', level=level)
                try:
                    result = func(*args, **kwargs)
                    self.success(f'Exit {func.__name__}() -> {result}')
                    return result
                except Exception as e:
                    self.error(f'Exception in {func.__name__}(): {e}')
                    raise
            return wrapper
        return decorator

