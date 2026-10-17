# Implicit Type Coercion

JavaScript is a dynamically and loosely typed language. This means it automatically converts data types behind the scenes when operators or conditions expect a certain type. This is known as **type coercion**.

## Key Rules & Behaviors
- **The Plus Operator (`+`):** If either operand is a string, JavaScript converts the other operand to a string and concatenates them.
- **Other Arithmetic Operators (`-`, `*`, `/`, `%`):** These operators convert strings to numbers automatically (e.g., `"5" - 2` results in `3`).
- **Logical Contexts (`if`, `while`, `||`, `&&`):** Values are coerced to booleans. Falsy values include `0`, `""`, `null`, `undefined`, `NaN`, and `false`. Everything else is truthy.