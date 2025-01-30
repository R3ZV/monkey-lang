from argparse import ArgumentParser
from interp.lexer import Lexer


def main() -> int:
    parser = ArgumentParser(prog="monkey")
    parser.add_argument("filename", nargs="?")

    args = parser.parse_args()
    if args.filename != None:
        if args.filename[-4:] != ".mky":
            print("Cannot interpret a non monkey file!")
            print("Monkey lang files end in '.mky'")
            return 1

        file_content: str

        try:
            with open(args.filename, "r") as f:
                file_content = f.read()
        except FileNotFoundError:
            print(f"{args.filename} not found!")
            return 1

        for token in Lexer(file_content).tokens():
            print(token)
    else:
        content = ""
        while True:
            line = input(">> ")
            if line == "":
                for token in Lexer(content).tokens():
                    print(token)
            elif line == "q":
                break
            else:
                content += line

    return 0


if __file__ == "__main__":
    raise SystemExit(main())
