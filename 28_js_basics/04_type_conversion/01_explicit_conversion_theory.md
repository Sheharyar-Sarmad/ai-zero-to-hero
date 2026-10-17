# Explicit Type Conversion (Type Casting)

Explicit conversion happens when you manually convert a value from one data type to another using built-in JavaScript functions or constructors.

## Common Methods
1. **To Number:**
   - `Number(value)`: Converts strings, booleans, or null/undefined into numbers.
   - `parseInt(string)`: Parses an integer from a string (ignores decimals/trailing text).
   - `parseFloat(string)`: Parses a floating-point number from a string.

2. **To String:**
   - `String(value)`: Converts any value into a string.
   - `value.toString()`: Method available on most primitives (except `null` and `undefined`).

3. **To Boolean:**
   - `Boolean(value)`: Converts any value into `true` or `false` based on its truthiness/falsiness.