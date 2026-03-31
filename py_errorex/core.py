import sys
import traceback
from .translator import translate_error
from .formatter import format_output

def handle_exception(exc_type, exc_value, exc_traceback):
    tb = traceback.extract_tb(exc_traceback)
    last_error = tb[-1]

    error_info = {
        "message": f"{exc_type.__name__}: {exc_value}",
        "file": last_error.filename,
        "line": last_error.lineno,
        "code": last_error.line
    }

    result = translate_error(error_info["message"])
    format_output(result, error_info)


def enable():
    sys.excepthook = handle_exception