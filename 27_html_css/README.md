# Web Basics, HTML & CSS

> **Module 27** of my [AI Zero to Hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero) roadmap, a comprehensive full-stack AI engineer journey.

**Author:** Sheharyar Sarmad
**LinkedIn:** [sheharyar-sarmad](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/)
**GitHub:** [Sheharyar-Sarmad/ai-zero-to-hero](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero)

---

## Why This Module Exists

After finishing the System Design foundation (Module 25) and Git & GitHub (Module 26), I'm shifting focus toward **building real products**. My next goal is the **JavaScript / TypeScript ecosystem: MERN, PERN and Next.js**, and shipping projects with it. The destination is to become a well-rounded engineer who can build the model, the backend and the interface.

Every web app starts with HTML and CSS, so that is where this module begins.

---

## Part 1: How the Web Works (Start Here)

Before writing any code, understand what actually happens when you open a website.

### The Big Picture

1. **You type a URL** (e.g. `github.com`) into the browser.
2. **DNS** translates that domain name into an IP address, like a phone book for the internet.
3. Your browser (the **client**) sends an **HTTP/HTTPS request** to that IP address.
4. The **server** receives the request, processes it, and sends back a **response** (HTML, CSS, JavaScript, images, JSON, etc.).
5. The browser **renders** the response into the page you see.

### Key Terms

| Term | Meaning |
|------|---------|
| **Client** | The device/browser making the request (your laptop, phone) |
| **Server** | A computer that stores files/data and responds to requests |
| **HTTP / HTTPS** | The protocol of communication between client and server (HTTPS is the encrypted version) |
| **DNS** | Converts domain names into IP addresses |
| **URL** | The full address of a resource, e.g. `https://example.com/about` |
| **Browser** | Software that requests, receives and renders web content (Chrome, Brave, Firefox) |
| **Frontend** | What the user sees and interacts with |
| **Backend** | Server-side logic, databases and APIs |
| **API** | A way for the frontend and backend to talk to each other |

### The Three Pillars of the Frontend

| Technology | Role | Analogy (human body) |
|-----------|------|----------------------|
| **HTML** | Structure and content | Skeleton |
| **CSS** | Styling and layout | Skin and clothes |
| **JavaScript** | Behavior and interactivity | Muscles and brain |

This module covers the first two. JavaScript comes next.

---

## Part 2: HTML & CSS Resources

### Main Course (One Shot)

One video covers **web basics, HTML and CSS** end to end:

- **YouTube:** [Web Basics + HTML + CSS (One Shot)](https://www.youtube.com/watch?v=9cmy6AK3IBA)

### Go Deeper (Free Reference)

For a better understanding of any topic from the video, use the W3Schools references. They are excellent for looking things up and practicing in the browser:

- **HTML:** [w3schools.com/html](https://www.w3schools.com/html/default.asp)
- **CSS:** [w3schools.com/css](https://www.w3schools.com/css/default.asp)

### PDF Notes

My own study notes for this module are included in this folder as PDFs, so you can revise without rewatching the videos.

> **Note:** You can also learn this module in a simpler way, for example by following only one resource, but combining the free resources above gives a deeper and more reliable understanding. HTML/CSS has a lot of free material, so use it.

---

## Part 3: Topics Covered

### HTML
- Document structure (`<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`)
- Headings, paragraphs, text formatting
- Links and images
- Lists (ordered, unordered)
- Tables and forms (inputs, labels, buttons)
- Semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`)
- Media (audio/video) and iframes

### CSS
- Selectors (element, class, id, descendant, pseudo-classes)
- Colors, fonts and units (`px`, `rem`, `%`, `vh`/`vw`)
- The **box model** (margin, border, padding, content)
- Display, position and z-index
- **Flexbox** and **CSS Grid** for layouts
- Responsive design and media queries
- Transitions, transforms and basic animations

---

## Part 4: The Challenge, Build a Portfolio Website

This is the most important part of the module. Watching tutorials is not enough; **you only learn to code by coding.**

### The Task

After completing HTML and CSS, build a **personal portfolio website of 2-3 pages** (for example Home, Projects, Contact), written **entirely by hand**.

### Rules

- Write every line of HTML and CSS yourself.
- Don't generate the code with AI and don't copy-paste whole templates. Looking up syntax in the docs is fine.
- Make it **responsive** (it should look good on both mobile and desktop).
- Use semantic HTML and a clean folder structure.
- Link the pages together with a navigation bar.

### Suggested Structure

```
portfolio/
├── index.html
├── projects.html
├── contact.html
├── css/
│   └── style.css
└── images/
```

### If the Challenge Feels Too Hard

Starting out is fine. If you don't feel ready to design a portfolio from scratch, practice with guided projects first:

1. Go to [**Frontend Mentor**](https://www.frontendmentor.io/) and log in.
2. Download the starter assets of any **easy (Newbie / Junior)** project.
3. Build it from the design file, then compare your result to the design.
4. Repeat with 2-3 projects, then come back and build your portfolio.

---

## Part 5: What's Next

The static pages you build here are **not interactive yet**. The next step is making the web come alive with JavaScript, which I'm splitting into two levels:

| Module | Level | Focus |
|--------|-------|-------|
| `js_basics` | Beginner | Variables, data types, operators, conditions, loops, functions, arrays, objects, DOM manipulation, events |
| `js_advance` | Advanced | Closures, scope, `this`, prototypes and classes, async JS (callbacks, promises, `async/await`), fetch API, ES6+ features, modules, error handling |

After JavaScript the plan is:

**TypeScript → Node.js & Express → MERN / PERN stack → Next.js → full-stack projects**

---

## Progress Checklist

- [ ] Understand how the web works
- [ ] Complete the HTML & CSS one-shot video
- [ ] Study the W3Schools HTML and CSS references
- [ ] Review the PDF notes
- [ ] (Optional) Complete 2-3 Frontend Mentor projects
- [ ] Build the 2-3 page portfolio website by hand
- [ ] Push the portfolio to GitHub
- [ ] Move on to `js_basics`

---

*Part of my journey to become a complete engineer. Follow along on [GitHub](https://github.com/Sheharyar-Sarmad/ai-zero-to-hero) and [LinkedIn](https://www.linkedin.com/in/sheharyar-sarmad-9b7736289/).*