import json
import logging


class JsonFormatter(logging.Formatter):
  def format(self, record):
    log_record = {
      "message": record.getMessage(),
      "severity": record.levelname,
      "logger": record.name,
      "timestamp": self.formatTime(record, self.datefmt)
    }

    for key, value in record.__dict__.items():
      if key not in ('args', 'asctime', 'created', 'exc_info', 'exc_text', 'filename',
                     'funcName', 'id', 'levelname', 'levelno', 'lineno', 'module',
                     'msecs', 'message', 'msg', 'name', 'pathname', 'process',
                     'processName', 'relativeCreated', 'stack_info', 'thread', 'threadName'):
        log_record[key] = value

    if record.exc_info:
      log_record["exception"] = self.formatException(record.exc_info)

    return json.dumps(log_record)
