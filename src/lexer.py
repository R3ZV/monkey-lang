from src.token import Token, TokenType
from typing import List


class Lexer:
    input: str
    pos: int
    read_pos: int
    char: str

    def __init__(self, input: str) -> None:
        self.input = input
        self.pos = 0
        self.read_pos = 0
        self.char = ""

        self.read_char()

    def tokens(self) -> List[Token]:
        tokens = []
        while True:
            token = self.next_token()
            tokens.append(token)

            if token.type == TokenType.EOF:
                break

        return tokens

    def next_token(self) -> Token:
        self.skip_whitespace()

        token: Token = Token(TokenType.ILLEGAL, "")
        match self.char:
            case "+":
                token = Token(TokenType.PLUS, self.char)
            case "=":
                token = Token(TokenType.ASSIGN, self.char)
            case "(":
                token = Token(TokenType.LPAREN, self.char)
            case ")":
                token = Token(TokenType.RPAREN, self.char)
            case "{":
                token = Token(TokenType.LBRACE, self.char)
            case "}":
                token = Token(TokenType.RBRACE, self.char)
            case ",":
                token = Token(TokenType.COMMA, self.char)
            case ";":
                token = Token(TokenType.SEMICOLON, self.char)
            case "":
                token = Token(TokenType.EOF, "")
            case _:
                # Early return because we self.read_char() at the end
                # and we have already called self.read_char() in
                # self.read_identifier()
                #
                # E.g. let x=5; in this case it would skip the "=".
                if self.is_letter(self.char):
                    ident = self.read_identifier()
                    type = Token.look_identifier(ident)

                    return Token(type, ident)
                elif self.is_number(self.char):
                    literal = self.read_number()
                    return Token(TokenType.INT, literal)
                else:
                    token = Token(TokenType.ILLEGAL, self.char)

        self.read_char()
        return token

    def skip_whitespace(self) -> None:
        while self.char in ["\n", " ", "\r", "\t"]:
            self.read_char()

    def read_char(self) -> None:
        if self.read_pos >= len(self.input):
            self.char = ""
        else:
            self.char = self.input[self.read_pos]

        self.pos = self.read_pos
        self.read_pos += 1

    def read_identifier(self) -> str:
        start = self.pos
        while self.is_letter(self.char):
            self.read_char()

        end = self.pos

        return self.input[start:end]

    def read_number(self) -> str:
        start = self.pos
        while self.is_number(self.char):
            self.read_char()

        end = self.pos

        return self.input[start:end]

    def is_letter(self, char: str) -> bool:
        return char.isalpha() or char == "_"

    def is_number(self, char: str) -> bool:
        return char.isnumeric()
