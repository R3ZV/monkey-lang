from interp.lexer import Lexer
from interp.token import Token
from ast.ast import Program


class Parser:
    lexer: Lexer
    curr_token: Token
    peek_token: Token

    def __init__(self, lexer: Lexer) -> None:
        self.lexer = lexer
        self.next_token()
        self.next_token()

    def next_token(self):
        self.curr_token = self.peek_token
        self.peek_token = self.lexer.next_token()

    # TODO: return a Program
    def parse(self):
        pass
