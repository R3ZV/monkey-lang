# Monkey Lang

This is my Python implementation of the book "Writing an interpreter in Go".

# The lang

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
		0
	} else {
		if (x == 1) {
			1
		} else {
        fibonacci(x - 1) + fibonacci(x - 2);
		}
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
