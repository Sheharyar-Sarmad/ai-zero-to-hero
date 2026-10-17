# Loops in JavaScript

Loops are programming constructs used to repeat a block of code multiple times until a specified condition evaluates to false.

## 1. The `for` Loop
Best used when the exact number of iterations is known in advance.

```javascript
for (let i = 0; i < 5; i++) {
    console.log(i);
}
```

## 2. The `while` Loop
Best used when the number of iterations is not known beforehand, and execution depends on a boolean condition.

```javascript
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
```

## 3. The `do...while` Loop
Similar to a `while` loop, but the code block executes at least once before the condition is tested.

```javascript
let i = 0;
do {
    console.log(i);
    i++;
} while (i < 5);
```