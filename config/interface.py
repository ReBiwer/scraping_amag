from typing import TypedDict
from logging.handlers import Handler

class FormatFormatterLogger(TypedDict):
    format: str

class FormatterLogger(TypedDict):
    name_format: FormatFormatterLogger

class SettingsHandlerLogger(TypedDict):
    # class_handler:
    when: str | None
    interval: int | None
    backupCount: int | None
    level: None
    formatter: FormatterLogger
    # filename:
    encoding = 'utf-8'

class HandlerLogger(TypedDict):
    name_handler: str

class LoggerDictConfig(TypedDict):
    version: int
    disable_existing_loggers: bool
    formatters: FormatterLogger
    handlers: HandlerLogger
