from re import compile


_find_pascal = compile(r'((?<=[a-z0-9])[A-Z]|(?!^)[A-Z](?=[a-z]))')


def pascal_to_delimited (target, delim = '_'):
    return _find_pascal.sub(delim + r'\1', target).lower()
