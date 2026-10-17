# Advanced Objects & Modern JS Features

## 1. Methods and the `this` Keyword
A **method** is a function stored as a property inside an object. The `this` keyword refers to the current object executing the method.

```javascript
const account = {
    owner: "Ali",
    balance: 500,
    deposit(amount) {
        this.balance += amount;
    }
};
```

## 2. Built-in Object Methods

- ```Object.keys(obj)```: Returns an array of an object's keys.

- ```Object.values(obj)```: Returns an array of an object's values.

- ```Object.entries(obj)```: Returns an array of key-value pairs [key, value].

## 3. Destructuring & Spread Syntax

Destructuring: Extract properties into individual variables cleanly.

```javaScript
const { name, age } = user;
```
**Spread Operator (...)**: Copy or merge objects together.

```javaScript
const merged = { ...obj1, ...obj2 };
```