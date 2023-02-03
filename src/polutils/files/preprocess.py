import re

def to_snake_case(text: list[str]) -> list[str]:
    return [re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', char).lower() for char in text]