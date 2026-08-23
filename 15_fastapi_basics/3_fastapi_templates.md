## FastAPI Templates

FastAPI can be used to render HTML pages using templates.

The most commonly used template engine with FastAPI is Jinja2.

## What Are Templates?

Templates are HTML files that can contain dynamic data.

Instead of creating HTML directly inside Python code, we create separate HTML files inside a templates directory.

## Example project structure:

project/
│
├── main.py
│
└── templates/
    └── index.html

## Jinja2

Jinja2 is a Python template engine that allows dynamic data to be inserted into HTML.

## Install Jinja2:

pip install jinja2
Template Directory

Create a folder named:

templates

Store your HTML files inside this folder.

Example:

templates/
├── index.html
├── about.html
└── contact.html
Template Syntax

Jinja2 uses special syntax to work with dynamic data.

Displaying Data
<h1>Hello, {{ name }}</h1>

{{ }} is used to display a value provided by the Python application.

Conditional Statements
{% if user %}
    <h1>Welcome, {{ user }}</h1>
{% else %}
    <h1>User not found</h1>
{% endif %}
Loops
{% for item in items %}
    <p>{{ item }}</p>
{% endfor %}

{% %} is used for Jinja2 statements such as conditions and loops.

FastAPI + Templates

FastAPI provides support for working with Jinja2 templates through its templating functionality.

The general flow is:

Browser
   ↓
FastAPI Route
   ↓
Jinja2 Template
   ↓
HTML Response
   ↓
Browser
Important Packages

For FastAPI templates, you generally need:

pip install fastapi
pip install uvicorn
pip install jinja2
Templates vs APIs

A normal FastAPI API commonly returns JSON:

Client → FastAPI → JSON

With templates:

Browser → FastAPI → Jinja2 → HTML

## Key Points

Templates are usually HTML files.
Jinja2 is the template engine commonly used with FastAPI.
Templates are stored in a templates directory.
{{ }} is used to display dynamic values.
{% %} is used for Jinja2 logic such as loops and conditions.
Templates are useful when FastAPI needs to serve HTML pages, not just JSON APIs.