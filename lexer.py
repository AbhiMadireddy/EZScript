import re

TOKEN_RULES = [
    (r'\d+', "NUMBER"),
    (r'[a-zA-Z_]\w*', "IDENTIFIER"),
    (r'\+', "PLUS"),
    (r'=', "EQUAL"),
    (r'\s+', None),  # Ignore whitespace
]

def lexer(code):
    tokens = []
    while code:
        for pattern, token_type in TOKEN_RULES:
            match = re.match(pattern, code)
            if match:
                if token_type:
                    tokens.append((token_type, match.group(0)))
                code = code[match.end():]
                break
        else:
            raise SyntaxError(f"Unexpected character: {code[0]}")
    return tokens

print(lexer("x = 42 + 5"))
