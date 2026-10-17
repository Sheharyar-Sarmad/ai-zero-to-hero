# Arithmetic & Assignment Operators

## What is an operator?
An **operator** is a symbol that performs an action on values (called **operands**).

```js
let total = 5 + 3; // + is the operator, 5 and 3 are operands
```

## 1. Arithmetic Operators

| Operator | Name           | Example   | Result |
|----------|----------------|-----------|--------|
| `+`      | Addition       | `10 + 3`  | `13`   |
| `-`      | Subtraction    | `10 - 3`  | `7`    |
| `*`      | Multiplication | `10 * 3`  | `30`   |
| `/`      | Division       | `10 / 3`  | `3.333...` |
| `%`      | Remainder (modulo) | `10 % 3` | `1` |
| `**`     | Exponent       | `2 ** 3`  | `8`    |
| `++`     | Increment      | `x++`     | x + 1  |
| `--`     | Decrement      | `x--`     | x - 1  |

### Remainder (`%`) is very useful
- Even/odd check: `n % 2 === 0` means even
- Wrapping around: `index % array.length`

### Increment: prefix vs postfix
```js
let a = 5;
console.log(a++); // 5 (returns old value, THEN adds 1)
console.log(a);   // 6

let b = 5;
console.log(++b); // 6 (adds 1 FIRST, then returns)
```

### The `+` operator with strings
`+` adds numbers but **joins** strings:
```js
console.log(5 + 5);     // 10
console.log("5" + "5"); // "55"
console.log("5" + 5);   // "55"  (number becomes a string)
console.log("5" - 2);   // 3     (string becomes a number)
```

### Operator precedence
Multiplication, division and exponent run before addition and subtraction. Use parentheses to be clear.
```js
console.log(2 + 3 * 4);   // 14
console.log((2 + 3) * 4); // 20
```

## 2. Assignment Operators

| Operator | Meaning      | Same as      |
|----------|--------------|--------------|
| `=`      | Assign       | `x = 5`      |
| `+=`     | Add and assign | `x = x + 5`  |
| `-=`     | Subtract and assign | `x = x - 5` |
| `*=`     | Multiply and assign | `x = x * 5` |
| `/=`     | Divide and assign | `x = x / 5` |
| `%=`     | Remainder and assign | `x = x % 5` |
| `**=`    | Exponent and assign | `x = x ** 5` |

## Common Mistakes
1. **Floating point errors:** `0.1 + 0.2` gives `0.30000000000000004`. Use `.toFixed(2)` or work in whole units (e.g. cents).
2. **Dividing by zero:** `5 / 0` gives `Infinity`, not an error.
3. **Mixing strings and numbers with `+`:** convert first with `Number()`.
4. **Using `=` instead of `===`** in comparisons (covered in the next file).

## Key Takeaways
- Arithmetic operators do math; `+` also joins strings.
- `%` gives the remainder.
- `x++` and `++x` differ in what they return.
- Shorthand assignment (`+=`, `-=`) keeps code short.