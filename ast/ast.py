from abc import ABC, abstractmethod
from typing import List, NoReturn
from interp.token import Token


class Node(ABC):
    @abstractmethod
    def token_literal(self) -> str:
        pass


class Statement(Node):
    @abstractmethod
    def statement_node(self) -> None:
        pass


class Expression(Node):
    @abstractmethod
    def expression_node(self) -> None:
        pass


class Identifier(Expression):
    token: Token
    value: str

    def __init__(self, token: Token, value: str) -> None:
        self.token = token
        self.value = value

    def token_literal(self) -> str:
        return self.token.literal

    def expression_node(self):
        pass


class LetStatement(Statement):
    token: Token
    value: Expression
    name: Identifier

    def __init__(
        self, token: Token, value: Expression, name: Identifier
    ) -> None:
        self.token = token
        self.value = value
        self.name = name

    def token_literal(self) -> str:
        return self.token.literal

    def statement_node(self):
        pass


class Program:
    statements: List[Statement]

    def __init__(self):
        self.statements = []

    def token_literal(self) -> str:
        if len(self.statements) > 0:
            return self.statements[0].token_literal()
        return ""
