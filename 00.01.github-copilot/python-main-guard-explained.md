# Python Main Guard Explained

This note explains the script ending pattern:

```python
if __name__ == '__main__':
  raise SystemExit(main())
```

## Purpose

This structure makes a Python file usable in two roles:

- As a command-line script (executed directly)
- As an importable module (used by other Python files)

## How it works

### 1) `__name__`

`__name__` is a special variable that Python sets automatically.

- If you run the file directly, `__name__` is set to `'__main__'`.
- If another file imports it, `__name__` is set to the module name.

So this condition:

```python
if __name__ == '__main__':
```

means: run the following code only when the file is executed directly.

### 2) `main()`

`main()` usually contains the command-line workflow and returns an exit status code:

- `0` for success
- non-zero (for example `1`) for errors

### 3) `raise SystemExit(main())`

`SystemExit` ends the program and passes the returned number to the operating system as the process exit code.

That is useful for shell scripting and automation, where exit codes are checked.

This is effectively equivalent to:

```python
import sys
sys.exit(main())
```

## Why this is recommended

- Keeps top-level code clean
- Prevents accidental execution when imported
- Improves reusability and testability
- Provides proper CLI exit behavior

## Template for a Python script

```Python
def classify_number(value: int) -> str:
  // function logic
  // …

def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: ….py <non-negative integer>', file=sys.stderr)
        return 1

    raw_value = sys.argv[1]

    try:
        number = int(raw_value)
    except ValueError:
        print('Error: the argument must be an integer.', file=sys.stderr)
        return 1

    if number < 0:
        print('Error: the argument must be a non-negative integer.', file=sys.stderr)
        return 1

    print(classify_number(number))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
```
