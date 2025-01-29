# Monkey Lang

This is my Python implementation of the book "Writing an interpreter in Go".
This is not a serious language, it's only for educational purposes.

# Run locally

You will need "uv" package manager installed and python 3.13.

```
git clone git@github.com:R3ZV/monkey-lang
cd monkey-lang

uv sync

uv run -m interp <file>

# Run an example
uv run -m interp examples/factorial.mky

# Play with it using REPL
uv run -m interp
```

# The lang

Monkey language files end in `.mky`.

### Limitations

- It only supports integers
- Doesn't have a `for / while` loop (but you can use reccursion)

### Syntax

```rust
let age = 1;
let name = "Monkey";
let result = 10 * (20 / 2);

let myArray = [1, 2, 3, 4, 5];
let thorsten = {"name": "Thorsten", "age": 28};

let add = fn(a, b) { return a + b; };
let add = fn(a, b) { a + b; };

let fibonacci = fn(x) {
	if (x == 0) {
		return 0;
	}

	if (x == 1) {
		return 1;
	} else {
		fibonacci(x - 1) + fibonacci(x - 2);
	}
};

let twice = fn(f, x) {
	return f(f(x));
};

let addTwo = fn(x) {
	return x + 2;
};

twice(addTwo, 2); // => 6
```
