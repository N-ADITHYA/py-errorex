patterns = [
    {
        "type": "TypeError",
        "match": "NoneType",
        "explanation": "You are using something that is None",
        "why": "The variable was never initialized or became None",
        "fixes": [
            "Initialize the variable before using it",
            "Check if value is None",
            "Use condition: if data is not None"
        ]
    },
    {
        "type": "IndexError",
        "match": "out of range",
        "explanation": "You are accessing an index that doesn't exist",
        "why": "The index is greater than the list size",
        "fixes": [
            "Check list length using len(list)",
            "Ensure index is within bounds",
            "Use safe loops like: for item in list"
        ]
    },
    {
        "type": "ZeroDivisionError",
        "match": "division by zero",
        "explanation": "You are dividing a number by zero",
        "why": "Division by zero is mathematically undefined",
        "fixes": [
            "Check denominator before division",
            "Add condition: if x != 0"
        ]
    },
    {
        "type": "KeyError",
        "match": "KeyError",
        "explanation": "You are accessing a key that doesn't exist in dictionary",
        "why": "The key is missing in the dictionary",
        "fixes": [
            "Check if key exists using 'in'",
            "Use dict.get() instead of direct access"
        ]
    },
    {
        "type": "AttributeError",
        "match": "AttributeError",
        "explanation": "You are accessing an attribute or method that doesn't exist",
        "why": "The object doesn't have that property or method",
        "fixes": [
            "Check object type using type()",
            "Verify method name spelling"
        ]
    },
    {
        "type": "TypeError",
        "match": "unsupported operand",
        "explanation": "You are trying to perform an operation on incompatible types",
        "why": "For example, adding string and integer",
        "fixes": [
            "Convert values to same type",
            "Check types before operation"
        ]
    },
    {
        "type": "FileNotFoundError",
        "match": "FileNotFoundError",
        "explanation": "The file you are trying to open does not exist",
        "why": "Incorrect file path or file missing",
        "fixes": [
            "Check file path",
            "Ensure file exists",
            "Use absolute path if needed"
        ]
    },
    {
        "type": "ValueError",
        "match": "ValueError",
        "explanation": "You passed an invalid value to a function",
        "why": "The value format or range is incorrect",
        "fixes": [
            "Read full traceback",
            "Check variable values",
            "Print debug values"
        ]
    }
]