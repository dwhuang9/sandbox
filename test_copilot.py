import os  # unused import


def greet(name):
    # Missing type checks and inconsistent naming
    '''Return a greeting message for the given name.'''
    if name == None:
        return 'No name provided' # single quotes vs double
    message = "Hello, " + name  # string concatenation instead of f-string
    return message


def farewell(Name):
    # Function name capitalization inconsistent
    return f"Goodbye, {Name}!"  # no docstring


if __name__ == "__main__":
    # Simple test without assertions
    print(greet("World"))
    print(farewell(None))
    print(greet(123))  # passing wrong type
    # Missing main guard for environment variable
    print(os.getenv('UNSET_ENV'))

