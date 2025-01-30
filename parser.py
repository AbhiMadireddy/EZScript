class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse_expression(self):
        left = self.parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in "+-":
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.parse_term()
            left = (op, left, right)  # Represent as a tree
        return left

    def parse_term(self):
        if self.tokens[self.pos].isdigit():
            val = int(self.tokens[self.pos])
            self.pos += 1
            return val
        return None  # Error handling
