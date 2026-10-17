# JavaScript Data Types (Theory)

> Code for this lesson: `04_data_types.js` → run with `node 04_data_types.js`

## What is a data type?
A data type tells JavaScript **what kind of value** a variable holds.
JavaScript is *dynamically typed* – you don't write the type, JS finds it out.

```js
let x = 10;     // number
x = "hello";    // now a string (allowed)
```

## Two groups

| Primitive (simple values) | Non-primitive (reference) |
|---|---|
| `string`, `number`, `boolean`, `undefined`, `null`, `bigint`, `symbol` | `object`, `array`, `function` |
| Copied by **value** | Copied by **reference** (same box) |

```js
let a = 5;  let b = a;  b = 10;     // a is still 5
let o1 = { n: 1 };  let o2 = o1;  o2.n = 99;   // o1.n is also 99!
```

## Primitive types

| Type | Example | Note |
|---|---|---|
| string | `"Hello"` | text, use `'` `"` or `` ` `` |
| number | `42`, `3.14` | integers + decimals, also `NaN`, `Infinity` |
| boolean | `true` / `false` | yes / no |
| undefined | `let x;` | declared but no value |
| null | `null` | empty **on purpose** |
| bigint | `123n` | very big integers |
| symbol | `Symbol("id")` | always-unique value (advanced) |

## Non-primitive types
- **Object** – `{ key: value }` pairs → `{ name: "Ali", age: 20 }`
- **Array** – ordered list → `[1, 2, 3]`
- **Function** – reusable code, also a value

## `typeof` – check a type
```js
typeof "hi"      // "string"
typeof 42        // "number"
typeof null      // "object"  ⚠️ famous JS bug
typeof []        // "object"  ⚠️ use Array.isArray([])
```

## Truthy & Falsy
Only **8 falsy** values: `false`, `0`, `-0`, `0n`, `""`, `null`, `undefined`, `NaN`.
Everything else is truthy (even `"0"`, `[]`, `{}`).

## Type conversion
```js
Number("42")     // 42        (explicit)
String(123)      // "123"
"5" + 2          // "52"      (implicit: + joins text)
"5" - 2          // 3         (implicit: - makes numbers)
```

## `==` vs `===`
- `==` converts types first → `"5" == 5` is `true`
- `===` checks type too → `"5" === 5` is `false`
- ✅ **Always use `===`**

## Remember
1. 7 primitives, everything else is an object.
2. Primitives copy the value, objects share the reference.
3. `typeof null` → `"object"` and `typeof []` → `"object"` (quirks).
4. Use `===`, not `==`.

## Practice
1. What does `typeof NaN` return?
2. Difference between `null` and `undefined`?
3. Why is `0.1 + 0.2 === 0.3` false?
4. Why does changing `o2` also change `o1` in the example above?