from py_errorex import *
from .patterns import patterns
def translate_error(error_message):
    error_message = error_message.lower()
    error_type = error_message.split(":")[0]

    # 1️⃣ match by MESSAGE first (specific)
    for pattern in patterns:
        if pattern["match"].lower() in error_message:
            return pattern

    # 2️⃣ fallback to TYPE
    for pattern in patterns:
        if pattern.get("type", "").lower() == error_type:
            return pattern

    return {
        "explanation": f"Unknown error: {error_message}",
        "why": "This error is not yet supported",
        "fixes": ["Check the full traceback"]
    }