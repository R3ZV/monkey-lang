from enum import Enum


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers + literal
    IDENT = "IDENT"
    INT = "INT"

    # Operators
    ASSIGN = "="
    PLUS = "+"

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
        }

        if ident in identifiers:
            return identifiers[ident]

        return TokenType.IDENT
