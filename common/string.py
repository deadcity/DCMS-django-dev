import re


def camel_to_underscore(str):
    str = re.sub(r'(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))', '_\\1', str)
    return str.lower()[1:] if str[1].isupper() else str.lower()
