import re

# Token patterns including tabs, colons, newlines, and strings
patterns = {
    "NUMBER": r"\d+",
    "IDENTIFIER": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "IF": r"\bif\b",
    "ELSE": r"\belse\b",
    "WHILE": r"\bwhile\b",
    "PRINT": r"\bprint\b",  # Added support for print function
    "ASSIGN": r"=",
    "PLUS": r"\+",
    "MINUS": r"-",
    "TIMES": r"\*",
    "DIVIDE": r"/",
    "LPAREN": r"\(",
    "RPAREN": r"\)",
    "LCURLYBRACE": r"\{",
    "RCURLYBRACE": r"\}",
    "SEMICOLON": r";",
    "COLON": r":",
    "NEWLINE": r"\n+",
    "WHITESPACE": r"[ ]+",  # Matches spaces but NOT tabs or newlines
    "TAB": r"\t+",
    "STRING": r'"[^"]*"',  # Matches anything inside double quotes
}

# Create a single regex pattern
token_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in patterns.items())

# Read file
with open("EZScript.ez", "r") as file:
    eztxt = file.read()

# Tokenize input
token_list = []
for match in re.finditer(token_regex, eztxt):
    token_type = match.lastgroup
    token_value = match.group()
    if token_type not in ["WHITESPACE"]:  # Ignore spaces, but keep other tokens
        token_list.append((token_type, token_value))

# Print tokens
for token in token_list:
    print(token)
