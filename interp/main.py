from argparse import ArgumentParser
from interp.lexer import Lexer


def main() -> int:
    parser = ArgumentParser()
    parser.add_argument("filename")

    args = parser.parse_args()
    if args.filename[-4:] != ".mky":
        print("Cannot interpret a non monkey file!")
        print("Monkey lang files end in '.mky'")
        return 1

    input: str

    try:
        with open(args.filename, "r") as f:
            input = f.read()
    except FileNotFoundError:
        print(f"{args.filename} not found!")
        return 1

    # interpretor = Interpretor(input)
    # interpretor.run()

    for token in Lexer(input).tokens():
        print(token)

    return 0


if __file__ == "__main__":
    raise SystemExit(main())
