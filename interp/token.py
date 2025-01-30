from enum import Enum


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers + literal
    IDENT = "IDENT"
    INT = "INT"

    # Operators
    ASSIGN = "="
    NOT = "!"
    EQL = "=="
    NOT_EQL = "!="
    PLUS = "+"
    MINUS = "-"
    MULT = "*"
    DIV = "/"
    GT = ">"
    LT = "<"

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"
    FALSE = "FALSE"
    TRUE = "TRUE"
    IF = "IF"
    ELSE = "ELSE"
    RETURN = "RETURN"


class Token:
    literal: str
    type: TokenType

    def __init__(
        self,
        type: TokenType,
        literal: str,
    ) -> None:
        self.literal = literal
        self.type = type

    def __repr__(self) -> str:
        return f"Litera = ({self.literal}) | Type = {self.type}"

    @staticmethod
    def look_identifier(ident: str) -> TokenType:
        identifiers = {
            "let": TokenType.LET,
            "fn": TokenType.FUNCTION,
            "false": TokenType.FALSE,
            "true": TokenType.TRUE,
            "if": TokenType.IF,
            "else": TokenType.ELSE,
            "return": TokenType.RETURN,
        }

        if ident in identifiers:
            return identifiers[ident]

        return TokenType.IDENT
