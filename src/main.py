from argparse import ArgumentParser
from src.lexer import Lexer


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("filename")

    args = parser.parse_args()
    if args.filename[-4:] != ".mky":
        print("Cannot interpret a non monkey file!")
        return 1

    input: str

    try:
        with open(args.filename, "r") as f:
            input = f.read()
    except FileNotFoundError:
        print(f"{args.filename} not found!")
        return 1

    for token in Lexer(input).tokens():
        print(token)
    return 0


if __file__ == "__main__":
    raise SystemExit(main())
