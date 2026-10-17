"use strict";

/* ---------- Constants & State ---------- */
const STORAGE_KEYS = { tasks: "focusboard.tasks", sessions: "focusboard.sessions" };
const FALLBACK_QUOTES = [
  "Small steps every day add up to big results.",
  "Done is better than perfect.",
  "Focus on one thing at a time."
];

let tasks = loadFromStorage(STORAGE_KEYS.tasks, []);
let sessions = loadFromStorage(STORAGE_KEYS.sessions, 0);
let currentFilter = "all";

/* ---------- DOM references ---------- */
const form = document.getElementById("task-form");
const titleInput = document.getElementById("task-title");
const priorityInput = document.getElementById("task-priority");
const dueInput = document.getElementById("task-due");
const titleError = document.getElementById("title-error");
const dueError = document.getElementById("due-error");
const taskList = document.getElementById("task-list");
const emptyMsg = document.getElementById("empty");
const statsEl = document.getElementById("stats");
const filterButtons = document.querySelectorAll(".filter");
const clearDoneBtn = document.getElementById("clear-done");
const toastEl = document.getElementById("toast");

/* ---------- localStorage helpers (with error handling) ---------- */
function loadFromStorage(key, fallback) {
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : fallback;
  } catch (err) {
    console.error(`Could not read "${key}":`, err);
    return fallback;
  }
}

function saveToStorage(key, value) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (err) {
    console.error(`Could not save "${key}":`, err);
    showToast("Could not save your data.");
  }
}

/* ---------- Toast ---------- */
let toastTimeout;
function showToast(message) {
  toastEl.textContent = message;
  toastEl.classList.add("show");
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => toastEl.classList.remove("show"), 2500);
}

/* ---------- Form validation ---------- */
function validateForm() {
  let valid = true;
  const title = titleInput.value.trim();

  titleError.textContent = "";
  dueError.textContent = "";
  titleInput.classList.remove("invalid");

  if (title.length < 3) {
    titleError.textContent = "Enter at least 3 characters.";
    titleInput.classList.add("invalid");
    valid = false;
  } else if (title.length > 80) {
    titleError.textContent = "Keep the title under 80 characters.";
    titleInput.classList.add("invalid");
    valid = false;
  }

  if (dueInput.value) {
    const today = new Date().toISOString().split("T")[0];
    if (dueInput.value < today) {
      dueError.textContent = "Pick today or a future date.";
      valid = false;
    }
  }
  return valid;
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  if (!validateForm()) return;

  const task = {
    id: Date.now(),
    title: titleInput.value.trim(),
    priority: priorityInput.value,
    due: dueInput.value || null,
    done: false
  };
  tasks.unshift(task);
  saveToStorage(STORAGE_KEYS.tasks, tasks);
  form.reset();
  priorityInput.value = "medium";
  renderTasks();
  showToast("Task added");
});

/* ---------- Rendering ---------- */
function renderTasks() {
  const visible = tasks.filter((t) => {
    if (currentFilter === "active") return !t.done;
    if (currentFilter === "done") return t.done;
    return true;
  });

  taskList.innerHTML = "";
  const today = new Date().toISOString().split("T")[0];

  visible.forEach((task) => {
    const li = document.createElement("li");
    const overdue = task.due && !task.done && task.due < today;
    li.className = `task ${task.priority}${task.done ? " done" : ""}${overdue ? " overdue" : ""}`;
    li.dataset.id = task.id;

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.done;
    checkbox.setAttribute("aria-label", `Mark "${task.title}" as done`);

    const info = document.createElement("div");
    info.className = "info";

    const title = document.createElement("div");
    title.className = "title";
    title.textContent = task.title; // textContent avoids HTML injection

    const meta = document.createElement("div");
    meta.className = "meta";
    meta.textContent =
      `${task.priority} priority` +
      (task.due ? ` · due ${task.due}${overdue ? " (overdue)" : ""}` : "");

    info.append(title, meta);

    const del = document.createElement("button");
    del.className = "delete";
    del.textContent = "×";
    del.setAttribute("aria-label", `Delete "${task.title}"`);

    li.append(checkbox, info, del);
    taskList.appendChild(li);
  });

  emptyMsg.hidden = visible.length > 0;

  const doneCount = tasks.filter((t) => t.done).length;
  statsEl.textContent = `${tasks.length - doneCount} active, ${doneCount} done`;
}

/* ---------- Event delegation for list actions ---------- */
taskList.addEventListener("click", (e) => {
  const li = e.target.closest(".task");
  if (!li) return;
  const id = Number(li.dataset.id);

  if (e.target.matches(".delete")) {
    tasks = tasks.filter((t) => t.id !== id);
    showToast("Task deleted");
  } else if (e.target.matches('input[type="checkbox"]')) {
    const task = tasks.find((t) => t.id === id);
    if (task) task.done = e.target.checked;
  } else {
    return;
  }
  saveToStorage(STORAGE_KEYS.tasks, tasks);
  renderTasks();
});

filterButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    currentFilter = btn.dataset.filter;
    filterButtons.forEach((b) => b.classList.toggle("active", b === btn));
    renderTasks();
  });
});

clearDoneBtn.addEventListener("click", () => {
  const before = tasks.length;
  tasks = tasks.filter((t) => !t.done);
  if (tasks.length === before) {
    showToast("No completed tasks to clear");
    return;
  }
  saveToStorage(STORAGE_KEYS.tasks, tasks);
  renderTasks();
  showToast("Cleared completed tasks");
});

/* ---------- Live clock (setInterval) ---------- */
const clockEl = document.getElementById("clock");
function updateClock() {
  clockEl.textContent = new Date().toLocaleString([], {
    weekday: "short",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit"
  });
}
updateClock();
setInterval(updateClock, 1000);

/* ---------- Focus timer (setInterval / clearInterval) ---------- */
const timerDisplay = document.getElementById("timer-display");
const startBtn = document.getElementById("timer-start");
const pauseBtn = document.getElementById("timer-pause");
const resetBtn = document.getElementById("timer-reset");
const minutesInput = document.getElementById("timer-minutes");
const sessionsEl = document.getElementById("sessions");

let timerId = null;
let remaining = 25 * 60;

function formatTime(totalSeconds) {
  const m = String(Math.floor(totalSeconds / 60)).padStart(2, "0");
  const s = String(totalSeconds % 60).padStart(2, "0");
  return `${m}:${s}`;
}

function updateTimerDisplay() {
  timerDisplay.textContent = formatTime(remaining);
  document.title = timerId ? `${formatTime(remaining)} – FocusBoard` : "FocusBoard";
}

function updateSessions() {
  sessionsEl.textContent = `Completed sessions: ${sessions}`;
}

function startTimer() {
  if (timerId) return; // already running
  timerId = setInterval(() => {
    remaining--;
    updateTimerDisplay();
    if (remaining <= 0) {
      stopTimer();
      sessions++;
      saveToStorage(STORAGE_KEYS.sessions, sessions);
      updateSessions();
      showToast("Session complete! Take a break.");
      remaining = Number(minutesInput.value) * 60;
      updateTimerDisplay();
    }
  }, 1000);
  timerDisplay.classList.add("running");
}

function stopTimer() {
  clearInterval(timerId);
  timerId = null;
  timerDisplay.classList.remove("running");
  updateTimerDisplay();
}

startBtn.addEventListener("click", startTimer);
pauseBtn.addEventListener("click", stopTimer);
resetBtn.addEventListener("click", () => {
  stopTimer();
  remaining = Number(minutesInput.value) * 60;
  updateTimerDisplay();
});

minutesInput.addEventListener("change", () => {
  let value = Number(minutesInput.value);
  if (!Number.isFinite(value) || value < 1) value = 1;
  if (value > 120) value = 120;
  minutesInput.value = value;
  if (!timerId) {
    remaining = value * 60;
    updateTimerDisplay();
  }
});

/* ---------- Fetch API with error handling ---------- */
const quoteEl = document.getElementById("quote");
const quoteBtn = document.getElementById("quote-btn");

async function loadQuote() {
  quoteEl.textContent = "Loading…";
  try {
    const response = await fetch("https://dummyjson.com/quotes/random");
    if (!response.ok) throw new Error(`Server responded with ${response.status}`);
    const data = await response.json();
    quoteEl.textContent = `“${data.quote}” — ${data.author}`;
  } catch (err) {
    console.error("Quote fetch failed:", err);
    const fallback = FALLBACK_QUOTES[Math.floor(Math.random() * FALLBACK_QUOTES.length)];
    quoteEl.textContent = `“${fallback}”`;
  }
}
quoteBtn.addEventListener("click", loadQuote);

/* ---------- Init ---------- */
renderTasks();
updateTimerDisplay();
updateSessions();
loadQuote();