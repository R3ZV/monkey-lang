from src.token import Token, TokenType
from src.lexer import Lexer


def test_basic_next_token():
    input = "=+(){},;"

    want = [
        Token(TokenType.ASSIGN, "="),
        Token(TokenType.PLUS, "+"),
        Token(TokenType.LPAREN, "("),
        Token(TokenType.RPAREN, ")"),
        Token(TokenType.LBRACE, "{"),
        Token(TokenType.RBRACE, "}"),
        Token(TokenType.COMMA, ","),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.EOF, ""),
    ]

    lexer = Lexer(input)
    for t in want:
        token = lexer.next_token()
        assert token.literal == t.literal
        assert token.type == t.type


def test_core_next_token():
    input = """let five = 5;
let ten = 10;
let add = fn(x, y) {
x + y;
};
let result = add(five, ten);
    """

    want = [
        Token(TokenType.LET, "let"),
        Token(TokenType.IDENT, "five"),
        Token(TokenType.ASSIGN, "="),
        Token(TokenType.INT, "5"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.LET, "let"),
        Token(TokenType.IDENT, "ten"),
        Token(TokenType.ASSIGN, "="),
        Token(TokenType.INT, "10"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.LET, "let"),
        Token(TokenType.IDENT, "add"),
        Token(TokenType.ASSIGN, "="),
        Token(TokenType.FUNCTION, "fn"),
        Token(TokenType.LPAREN, "("),
        Token(TokenType.IDENT, "x"),
        Token(TokenType.COMMA, ","),
        Token(TokenType.IDENT, "y"),
        Token(TokenType.RPAREN, ")"),
        Token(TokenType.LBRACE, "{"),
        Token(TokenType.IDENT, "x"),
        Token(TokenType.PLUS, "+"),
        Token(TokenType.IDENT, "y"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.RBRACE, "}"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.LET, "let"),
        Token(TokenType.IDENT, "result"),
        Token(TokenType.ASSIGN, "="),
        Token(TokenType.IDENT, "add"),
        Token(TokenType.LPAREN, "("),
        Token(TokenType.IDENT, "five"),
        Token(TokenType.COMMA, ","),
        Token(TokenType.IDENT, "ten"),
        Token(TokenType.RPAREN, ")"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.EOF, ""),
    ]

    lexer = Lexer(input)
    for t in want:
        token = lexer.next_token()
        assert token.literal == t.literal
        assert token.type == t.type
