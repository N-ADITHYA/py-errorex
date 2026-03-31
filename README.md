#  py-errorex

**Beginner-friendly Python error explainer**

`py-errorex` enhances Python error messages by providing **clear explanations, reasons, and actionable fixes** — helping beginners debug faster and understand their mistakes.

---

##  Features

*  Explains Python errors in simple language
*  Shows *why* the error happened
* ️ Suggests practical fixes
*  Works instantly with any Python script
*  Focused on common beginner mistakes

---

##  Installation

Install from PyPI:

```bash
pip install py-errorex
```

Or install locally:

```bash
pip install .
```

---

## Usage

Just enable ErrorX at the top of your script:

```python
import errorex

errorex.enable()

data = None
print(len(data))
```

---

##  Default Python Error

```text
TypeError: object of type 'NoneType' has no len()
```

---

##  With py-errorex

```text
❌ TypeError: object of type 'NoneType' has no len()
👉 You are using something that is None

📍 File: app.py
🔢 Line: 4
👉 Code: print(len(data))

💡 Why:
The variable was never initialized or became None

👉 Fixes:
 - Initialize the variable before using it
 - Check if value is None
 - Use condition: if data is not None
```

---

## Supported Errors

Currently supports:

* TypeError (NoneType, incompatible types)
* IndexError
* KeyError
* ZeroDivisionError
* AttributeError
* ValueError
* FileNotFoundError

> More patterns coming soon 

---

##  How It Works

`py-errorex` hooks into Python’s global exception system:

```python
sys.excepthook
```

When an error occurs:

1. Captures traceback
2. Identifies error type
3. Matches known patterns
4. Generates explanation + fixes
5. Displays beginner-friendly output

---

## Example

```python
import errorex

errorex.enable()

arr = [1, 2, 3]
print(arr[5])
```

### Output

```text
❌ IndexError: list index out of range
👉 You are accessing an index that doesn't exist

💡 Why:
The index is greater than the list size

👉 Fixes:
 - Check list length using len(list)
 - Ensure index is within bounds
 - Use safe loops like: for item in list
```

---

##  Future Improvements

*  Colored terminal output
*  Smarter context-aware explanations
*  IDE / VS Code extension
*  More error patterns

---

##  Contributing

Contributions are welcome!

You can:

* Add new error patterns
* Improve explanations
* Enhance formatting

---

##  License

MIT License

---

##  Support

If you found this useful, consider giving it a ⭐ on GitHub!

---

**Made for learners, by a learner**
