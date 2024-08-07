from typing import TypedDict, List
from enum import Enum
from logging import Handler
from os.path import Path


class LevelLoggers(Enum):
    DEBUG = 'DEBUG'
    INFO = 'INFO'
    WARNING = 'WARNING'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'


class FormatFormatterLogger(TypedDict):
    format: str

class FormatterLogger(TypedDict):
    name_format: FormatFormatterLogger

class SettingsHandlerLogger(TypedDict):
    class_handler: Handler
    when: str | None
    interval: int | None
    backupCount: int | None
    level: LevelLoggers
    formatter: FormatterLogger
    filename: str
    encoding = 'utf-8'

class HandlerLogger(TypedDict):
    name_handler: SettingsHandlerLogger

class SettighsLoger(TypedDict):
    level:LevelLoggers
    handlers: List[HandlerLogger, ...]

class LoggerConfig(TypedDict):
    name_logger: SettighsLoger

class LoggerDictConfig(TypedDict):
    version: int
    disable_existing_loggers: bool
    formatters: FormatterLogger
    handlers: HandlerLogger
    loggers: LoggerConfig
