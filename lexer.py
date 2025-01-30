import re

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def lex(input_string):
    tokens = []
    while input_string:
        match = None
        for token_type, regex in patterns.items():
            match = re.match(regex, input_string)
            if match:
                value = match.group(0)
                tokens.append(Token(token_type, value))
                input_string = input_string[len(value):]
                break

        if not match:
            raise ValueError(f"Invalid syntax: {input_string}")

    return tokens

patterns = {
    "NUMBER": r"\d+",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "PLUS": r"\+",
    "MINUS": r"-",
    "TIMES": r"\*",
    "DIVIDE": r"/",
    "LPAREN": r"\(",
    "RPAREN": r"\)",
    "WHITESPACE": r"\s+",
}
