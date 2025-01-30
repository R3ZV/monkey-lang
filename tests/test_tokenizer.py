from interp.token import Token, TokenType
from interp.lexer import Lexer


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
        Token(TokenType.EOF, "EOF"),
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
!-/*5;
5 < 10 > 5;
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
        Token(TokenType.NOT, "!"),
        Token(TokenType.MINUS, "-"),
        Token(TokenType.DIV, "/"),
        Token(TokenType.MULT, "*"),
        Token(TokenType.INT, "5"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.INT, "5"),
        Token(TokenType.LT, "<"),
        Token(TokenType.INT, "10"),
        Token(TokenType.GT, ">"),
        Token(TokenType.INT, "5"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.EOF, "EOF"),
    ]

    lexer = Lexer(input)
    for t in want:
        token = lexer.next_token()
        assert token.literal == t.literal
        assert token.type == t.type


def test_other_identifs():
    input = """
let add = fn(x, y) {
    x + y;
};

let result = add(five, ten);

if (5 < 10) {
    return true;
} else {
    return false;
}
"""

    want = [
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
        Token(TokenType.IF, "if"),
        Token(TokenType.LPAREN, "("),
        Token(TokenType.INT, "5"),
        Token(TokenType.LT, "<"),
        Token(TokenType.INT, "10"),
        Token(TokenType.RPAREN, ")"),
        Token(TokenType.LBRACE, "{"),
        Token(TokenType.RETURN, "return"),
        Token(TokenType.TRUE, "true"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.RBRACE, "}"),
        Token(TokenType.ELSE, "else"),
        Token(TokenType.LBRACE, "{"),
        Token(TokenType.RETURN, "return"),
        Token(TokenType.FALSE, "false"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.RBRACE, "}"),
        Token(TokenType.EOF, "EOF"),
    ]

    lexer = Lexer(input)
    for t in want:
        token = lexer.next_token()
        assert token.literal == t.literal
        assert token.type == t.type


def test_double_char_tokens():
    input = "5 != 4; 5 == 5;"

    want = [
        Token(TokenType.INT, "5"),
        Token(TokenType.NOT_EQL, "!="),
        Token(TokenType.INT, "4"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.INT, "5"),
        Token(TokenType.EQL, "=="),
        Token(TokenType.INT, "5"),
        Token(TokenType.SEMICOLON, ";"),
        Token(TokenType.EOF, "EOF"),
    ]

    lexer = Lexer(input)
    for t in want:
        token = lexer.next_token()
        assert token.literal == t.literal
        assert token.type == t.type
