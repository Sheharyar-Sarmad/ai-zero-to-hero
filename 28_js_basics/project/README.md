# FocusBoard

A task manager with a built-in focus timer, built with vanilla HTML, CSS and JavaScript as the capstone for the **28 JS Basics** course.

## Features

- **Add tasks** with a title, priority (low, medium, high) and optional due date
- **Form validation** with inline error messages
- **Complete, delete and filter** tasks (All, Active, Done) and clear finished ones
- **Overdue highlighting** for tasks past their due date
- **Focus timer** with a custom length (1 to 120 minutes) and a completed-sessions counter
- **Live clock** that updates every second
- **Quote of the moment** loaded from a public API, with an offline fallback
- **Persistent data**: tasks and sessions are saved in `localStorage`

## Concepts practiced

| Topic | Where it is used |
|---|---|
| Functions, arrays, objects | Task data and `filter`, `find`, `map` |
| DOM manipulation | Rendering the task list with `createElement` |
| Event listeners | Form submit, filters, event delegation on the list |
| Forms and validation | Title length and due date checks |
| Timers and intervals | `setInterval` for the clock and focus timer |
| localStorage and JSON | `JSON.stringify` / `JSON.parse` for saving tasks |
| Fetch API | Random quote from `dummyjson.com` |
| Error handling | `try/catch` around storage and fetch calls |

## Project structure

```
project/
├── README.md
├── index.html
├── styles.css
└── script.js
```

## How to run

1. Open the `project` folder in VS Code.
2. Right-click `index.html` and choose **Open with Live Server**, or just open the file in your browser.
3. An internet connection is only needed for the quote feature.

## Ideas for improvement

- Edit existing tasks
- Sort tasks by priority or due date
- Add a short break timer between focus sessions
- Export and import tasks as a JSON file