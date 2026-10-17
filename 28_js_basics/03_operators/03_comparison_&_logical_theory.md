# Comparison, Logical & Other Operators

## 1. Comparison Operators
Comparison operators compare two values and always return a **boolean** (`true` or `false`).

| Operator | Meaning                  | Example      | Result  |
|----------|--------------------------|--------------|---------|
| `==`     | Equal (loose)            | `5 == "5"`   | `true`  |
| `===`    | Equal (strict)           | `5 === "5"`  | `false` |
| `!=`     | Not equal (loose)        | `5 != "5"`   | `false` |
| `!==`    | Not equal (strict)       | `5 !== "5"`  | `true`  |
| `>`      | Greater than             | `7 > 3`      | `true`  |
| `<`      | Less than                | `7 < 3`      | `false` |
| `>=`     | Greater than or equal    | `7 >= 7`     | `true`  |
| `<=`     | Less than or equal       | `3 <= 2`     | `false` |

### `==` vs `===` (very important)
- `==` converts types before comparing (**type coercion**), which causes surprises.
- `===` compares value **and** type, with no conversion.

**Rule: always use `===` and `!==`.**

### Special cases
```js
NaN === NaN;          // false (use Number.isNaN(x))
null == undefined;    // true
null === undefined;   // false
[] == false;          // true  (confusing!)
"b" > "a";            // true  (strings compare alphabetically)
```

## 2. Logical Operators

| Operator | Name | Meaning |
|----------|------|---------|
| `&&`     | AND  | `true` only if **both** sides are true |
| `\|\|`   | OR   | `true` if **at least one** side is true |
| `!`      | NOT  | flips `true` to `false` and vice versa |

### Truth table
| A     | B     | A && B | A \|\| B |
|-------|-------|--------|----------|
| true  | true  | true   | true     |
| true  | false | false  | true     |
| false | true  | false  | true     |
| false | false | false  | false    |

### Short-circuit evaluation
Logical operators actually return one of the **operand values**, and stop early:
- `a && b` returns `a` if `a` is falsy, otherwise `b`
- `a || b` returns `a` if `a` is truthy, otherwise `b`

```js
const name = userName || "Guest";     // default value
isLoggedIn && showDashboard();        // run only if true
```

## 3. Nullish Coalescing `??`
Returns the right side **only** if the left is `null` or `undefined`.

```js
0 || 10;   // 10  (0 is falsy)
0 ?? 10;   // 0   (0 is not null/undefined)
```
Use `??` when `0`, `""` or `false` are valid values.

## 4. Ternary Operator
A one-line `if/else`:
```js
condition ? valueIfTrue : valueIfFalse;

const status = age >= 18 ? "Adult" : "Minor";
```
Avoid nesting ternaries; it hurts readability.

## 5. Other Useful Operators

| Operator | Purpose | Example |
|----------|---------|---------|
| `typeof` | Gets the type of a value | `typeof 42` gives `"number"` |
| `?.`     | Optional chaining (safe property access) | `user?.address?.city` |
| `...`    | Spread (expands values) | `[...arr1, ...arr2]` |
| `in`     | Checks if a property exists | `"name" in person` |
| `instanceof` | Checks object type | `[] instanceof Array` |

## Operator Precedence (high to low, simplified)
1. `()` parentheses
2. `!`, `++`, `--`, `typeof`
3. `**`
4. `*`, `/`, `%`
5. `+`, `-`
6. `<`, `<=`, `>`, `>=`
7. `===`, `!==`, `==`, `!=`
8. `&&`
9. `||`, `??`
10. `?:` (ternary)
11. `=`, `+=`, `-=` ...

## Common Mistakes
1. Using `=` (assign) instead of `===` (compare) inside `if`.
2. Using `||` for defaults when `0` or `""` is valid. Use `??`.
3. Mixing `??` with `||` or `&&` without parentheses (a syntax error).
4. Comparing objects/arrays with `===`: `[1] === [1]` is `false` because they are different references.

## Key Takeaways
- Always prefer `===` over `==`.
- `&&` and `||` short-circuit and return values, not just booleans.
- `??` handles only `null`/`undefined`.
- Ternary is great for simple either/or choices.