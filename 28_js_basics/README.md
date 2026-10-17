# 28 · JavaScript Basics: Zero to Hero

> Part of the **ai-zero-to-hero** repository.

A hands-on, beginner-friendly JavaScript curriculum. It starts with "what is JavaScript?" and ends with a working, browser-based capstone app. Each module pairs short theory notes with runnable code and practice exercises, so you learn by reading, running, and building.

---

## Table of Contents

- [What You Will Learn](#what-you-will-learn)
- [Prerequisites](#prerequisites)
- [Curriculum Structure](#curriculum-structure)
- [Learning Path](#learning-path)
- [Capstone Project: FocusBoard](#capstone-project-focusboard)
- [How to Use This Repository](#how-to-use-this-repository)
- [Suggested Study Plan](#suggested-study-plan)
- [Tips for Learning Effectively](#tips-for-learning-effectively)
- [Resources](#resources)

---

## What You Will Learn

By the end of this module you will be able to:

- Write and run JavaScript in the browser and with Node.js
- Work with variables, data types, operators, and type conversion
- Control program flow with conditionals and loops
- Organize code with functions, arrays, and objects
- Manipulate strings, numbers, and the `Math` object
- Build interactive pages using the DOM and event listeners
- Validate user input in forms
- Schedule work with timers and intervals
- Persist data with `localStorage` and JSON
- Fetch data from APIs using `fetch` and `async/await`
- Handle errors and debug code with confidence
- Combine all of the above in a complete mini application

## Prerequisites

| Requirement | Notes |
|---|---|
| Basic HTML and CSS | Helpful for modules 11 to 17 and the capstone |
| A code editor | [VS Code](https://code.visualstudio.com/) is recommended |
| A modern browser | Chrome, Edge, Firefox, or Safari |
| Node.js (optional but recommended) | Lets you run `.js` files from the terminal. Get it from [nodejs.org](https://nodejs.org/) |

No prior programming experience is required.

---

## Curriculum Structure

```
28_js_basics/
├── 01_foundation/
├── 02_variables_&_data_types/
├── 03_operators/
├── 04_type_conversion/
├── 05_conditionals/
├── 06_loops/
├── 07_functions/
├── 08_arrays/
├── 09_objects/
├── 10_strings_numbers_math/
├── 11_dom_manipulation/
├── 12_events_listeners/
├── 13_forms_validation/
├── 14_timers_intervals/
├── 15_localstorage_json/
├── 16_fetch_api/
├── 17_error_handling_debugging/
├── project/
└── README.md
```

### Part 1: Core Language

| # | Module | What it covers |
|---|---|---|
| 01 | [`01_foundation`](./01_foundation) | What JavaScript is, where it runs, `console.log`, comments, linking a script to HTML, and running code in the browser and Node.js |
| 02 | [`02_variables_&_data_types`](./02_variables_&_data_types) | `var`, `let`, `const`, naming rules, primitives (string, number, boolean, `null`, `undefined`, symbol, bigint), and `typeof` |
| 03 | [`03_operators`](./03_operators) | Arithmetic, assignment, comparison (`==` vs `===`), logical operators, and the ternary operator |
| 04 | [`04_type_conversion`](./04_type_conversion) | Implicit coercion, explicit conversion with `Number()`, `String()`, and `Boolean()`, truthy and falsy values |
| 05 | [`05_conditionals`](./05_conditionals) | `if / else if / else`, `switch`, and short-circuit evaluation |
| 06 | [`06_loops`](./06_loops) | `for`, `while`, `do...while`, `for...of`, `for...in`, `break`, and `continue` |
| 07 | [`07_functions`](./07_functions) | Declarations, expressions, arrow functions, parameters, return values, scope, closures, and callbacks |

### Part 2: Working with Data

| # | Module | What it covers |
|---|---|---|
| 08 | [`08_arrays`](./08_arrays) | Creating and modifying arrays, `push`, `pop`, `slice`, `splice`, `map`, `filter`, `reduce`, `find`, and `sort` |
| 09 | [`09_objects`](./09_objects) | Object literals, properties and methods, `this`, destructuring, spread and rest, and `Object.keys/values/entries` |
| 10 | [`10_strings_numbers_math`](./10_strings_numbers_math) | String methods, template literals, number formatting, and the `Math` object |

### Part 3: JavaScript in the Browser

| # | Module | What it covers |
|---|---|---|
| 11 | [`11_dom_manipulation`](./11_dom_manipulation) | Selecting elements, changing text, attributes, and styles, and creating and removing nodes |
| 12 | [`12_events_listeners`](./12_events_listeners) | `addEventListener`, the event object, bubbling, and event delegation |
| 13 | [`13_forms_validation`](./13_forms_validation) | Reading form values, `preventDefault`, custom validation rules, and inline error messages |
| 14 | [`14_timers_intervals`](./14_timers_intervals) | `setTimeout`, `setInterval`, `clearInterval`, and building clocks and countdowns |

### Part 4: Data, APIs, and Reliability

| # | Module | What it covers |
|---|---|---|
| 15 | [`15_localstorage_json`](./15_localstorage_json) | `localStorage` basics, `JSON.stringify` and `JSON.parse`, and persisting app state |
| 16 | [`16_fetch_api`](./16_fetch_api) | Promises, `fetch`, `async/await`, handling responses, and working with real APIs |
| 17 | [`17_error_handling_debugging`](./17_error_handling_debugging) | `try / catch / finally`, throwing errors, common error types, DevTools, breakpoints, and debugging strategies |

### Capstone

| Folder | What it contains |
|---|---|
| [`project`](./project) | **FocusBoard**, a task manager with a focus timer that uses concepts from the whole module |

---

## Learning Path

```
Core Language ──► Working with Data ──► Browser & DOM ──► Data, APIs & Reliability ──► Capstone
  (01 – 07)           (08 – 10)           (11 – 14)             (15 – 17)             (project)
```

Work through the modules **in order**. Each one builds on the previous ones, and modules 11 to 17 assume you are comfortable with functions, arrays, and objects.

---

## Capstone Project: FocusBoard

The [`project/`](./project) folder contains **FocusBoard**, a task manager with a built-in focus timer, built with vanilla HTML, CSS, and JavaScript and no frameworks or libraries.

### Purpose

Reading about concepts is not the same as using them together. The capstone shows how the individual skills from modules 01 to 17 combine in one real application, and gives you a codebase to read, run, break, and extend.

### Scope

| Feature | Description |
|---|---|
| Task management | Add, complete, delete, and filter tasks by status |
| Priorities and due dates | Each task has a priority and an optional due date, with overdue tasks highlighted |
| Form validation | Inline error messages for invalid titles and past dates |
| Focus timer | A configurable countdown (1 to 120 minutes) with a completed-sessions counter |
| Live clock | Updates every second |
| Quote of the moment | Fetched from a public API, with a fallback if the request fails |
| Persistence | Tasks and sessions survive a page refresh |

### How It Ties the Modules Together

| Concept | Modules | Where it appears in the project |
|---|---|---|
| Variables, operators, conditionals | 02, 03, 05 | State, comparisons, and branching logic throughout |
| Type conversion | 04 | Converting input values with `Number()` |
| Loops and arrays | 06, 08 | Rendering lists, `filter`, `find`, and `forEach` |
| Functions | 07 | Small, single-purpose helpers (`renderTasks`, `validateForm`, `formatTime`) |
| Objects | 09 | Each task is an object with `id`, `title`, `priority`, `due`, `done` |
| Strings and numbers | 10 | `padStart` for timer formatting, trimming and length checks |
| DOM manipulation | 11 | Building the task list with `createElement` and `textContent` |
| Events | 12 | Form submit, filter buttons, and delegated clicks on the list |
| Forms and validation | 13 | Validating the add-task form before saving |
| Timers and intervals | 14 | The live clock and the focus timer |
| localStorage and JSON | 15 | Saving and loading tasks and session counts |
| Fetch API | 16 | Loading a random quote with `async/await` |
| Error handling | 17 | `try/catch` around storage and network calls, plus a graceful fallback |

### Running the Capstone

1. Open the `project/` folder in VS Code.
2. Right-click `index.html` and choose **Open with Live Server**, or double-click the file to open it in your browser.
3. An internet connection is only needed for the quote feature.

See [`project/README.md`](./project/README.md) for the full project documentation.

### Stretch Goals

- Edit existing tasks
- Sort tasks by priority or due date
- Add a short-break timer between focus sessions
- Export and import tasks as a JSON file

---

## How to Use This Repository

### 1. Clone and open

```bash
git clone <your-repo-url>
cd ai-zero-to-hero/28_js_basics
code .
```

### 2. Read the theory

Each module folder contains Markdown (`.md`) notes explaining the concepts.

- Open them in VS Code and press `Ctrl+Shift+V` (`Cmd+Shift+V` on macOS) for a rendered preview.
- Read the notes first, then move on to the code examples.

### 3. Run the JavaScript files

**Option A: Node.js (terminal)**

```bash
node 01_foundation/example.js
```

Replace the path with the file you want to run. This works for every module that does not touch the DOM or browser-only APIs (modules 01 to 10, and parts of 14 and 17).

**Option B: Browser console**

1. Open any page in your browser.
2. Press `F12` to open DevTools and go to the **Console** tab.
3. Paste a snippet and press `Enter`.

### 4. View the HTML pages

Modules 11 to 17 and the capstone include `index.html` pages that load a `script.js`.

1. Install the **Live Server** extension in VS Code.
2. Right-click the module's `index.html` and choose **Open with Live Server**.
3. Edit the code, save, and the page reloads automatically.
4. Open DevTools (`F12`) to see `console.log` output and errors.

Opening `index.html` directly with a double-click also works. Live Server is just more convenient, and some browser features behave better when served over `http://`.

### 5. Do the exercises

For each module:

1. Read the notes.
2. Run the examples and change values to see what happens.
3. Attempt the exercises **without looking at the solutions**.
4. Compare your work with the provided solutions, and note any differences in approach.
5. Re-do any exercise you got stuck on a day later.

### 6. Build the capstone

Finish at least modules 01 to 17 first, then:

1. Read through the `project/` code file by file: `index.html`, then `styles.css`, then `script.js`.
2. Run it and use every feature.
3. Pick a stretch goal and implement it yourself.

---

## Suggested Study Plan

| Week | Modules | Focus |
|---|---|---|
| 1 | 01 to 04 | Getting set up, variables, operators, and conversion |
| 2 | 05 to 07 | Decisions, repetition, and reusable code |
| 3 | 08 to 10 | Collections of data, objects, strings, numbers, and math |
| 4 | 11 to 12 | Making pages interactive |
| 5 | 13 to 14 | Forms, validation, and timers |
| 6 | 15 to 17 | Persistence, APIs, and debugging |
| 7 | Capstone | Read, run, extend, and build your own version |

Adjust the pace to your schedule. Consistency matters more than speed.

---

## Tips for Learning Effectively

- **Type the code yourself.** Copying and pasting skips the learning.
- **Break things on purpose.** Change a line and predict what will happen before you run it.
- **Use the console.** `console.log` and DevTools are your best friends.
- **Read error messages carefully.** They usually tell you exactly where the problem is.
- **Build small things.** After each module, make a tiny program that uses what you just learned.
- **Do not skip debugging (Module 17).** It is the skill that makes everything else faster.

---

## Resources

- [MDN Web Docs: JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): the definitive reference
- [javascript.info](https://javascript.info/): a detailed modern JavaScript tutorial
- [Chrome DevTools documentation](https://developer.chrome.com/docs/devtools)
- [Can I use](https://caniuse.com/): browser support lookup

---

## What's Next

After completing this module you will be ready to move on to more advanced topics such as ES6+ modules, asynchronous patterns, working with frameworks, and using JavaScript to call AI APIs later in the **ai-zero-to-hero** journey.

Happy coding!