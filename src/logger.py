import inspect
import logging


class LoggerProxy:
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self._logger.addHandler(ch)

    def __getattr__(self, item):
        attr = self._logger.__getattribute__(item)
        if hasattr(attr, '__call__'):
            def wrapper(msg, *args, **kwargs):
                frame = inspect.currentframe().f_back
                filename = inspect.getframeinfo(frame).filename.split('/')[-1]
                func = inspect.getframeinfo(frame).function
                formatted_msg = f'<{filename}::{func}>'
                return attr(formatted_msg + ' ' + msg, *args, **kwargs)
            return wrapper
        return attr


logger = LoggerProxy()