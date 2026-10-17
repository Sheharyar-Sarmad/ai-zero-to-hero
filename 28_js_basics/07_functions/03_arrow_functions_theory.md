# Arrow Functions

Introduced in ES6, arrow functions provide a concise syntax for writing function expressions. They are widely used for short callbacks and modern JavaScript applications.

## Syntax Comparison

**Traditional Expression:**
```javascript
const square = function(x) {
    return x * x;
};
```

## Arrow Function (Standard):

```javaScript
const square = (x) => {
    return x * x;
};
```

## Arrow Function (Concise Body):

If the function contains only a single expression, you can omit the curly braces {} and the return keyword (implicit return).

```javaScript
const square = x => x * x;
```

## Key Characteristics

Shorter and cleaner syntax.

Do not have their own this keyword binding (inherits this from the enclosing lexical scope).