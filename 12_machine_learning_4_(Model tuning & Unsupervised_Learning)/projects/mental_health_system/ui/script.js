(() => {
    "use strict";

    const API_BASE = "http://127.0.0.1:8000";

    const form = document.getElementById("predict-form");
    const submitBtn = document.getElementById("submit-btn");
    const resetBtn = document.getElementById("reset-btn");
    const errorRetryBtn = document.getElementById("error-retry-btn");

    const stateIdle = document.getElementById("state-idle");
    const stateLoading = document.getElementById("state-loading");
    const stateResult = document.getElementById("state-result");
    const stateError = document.getElementById("state-error");

    const scoreNumberEl = document.getElementById("score-number");
    const scoreBandEl = document.getElementById("score-band");
    const scoreContextEl = document.getElementById("score-context");
    const gaugeFill = document.getElementById("gauge-fill");
    const errorLabelEl = document.getElementById("error-label");
    const errorCopyEl = document.getElementById("error-copy");
    const progressBar = document.getElementById("progress-bar");

    const GAUGE_ARC_LENGTH = 314;

    // Particles
    function createParticles() {
        const container = document.getElementById("particles");
        if (!container) return;
        for (let i = 0; i < 50; i++) {
            const particle = document.createElement("div");
            particle.className = "particle";
            particle.style.left = Math.random() * 100 + "%";
            particle.style.width = (2 + Math.random() * 4) + "px";
            particle.style.height = particle.style.width;
            particle.style.animationDuration = (15 + Math.random() * 25) + "s";
            particle.style.animationDelay = (Math.random() * 20) + "s";
            particle.style.opacity = 0.2 + Math.random() * 0.3;
            container.appendChild(particle);
        }
    }
    createParticles();

    // Gauge Ticks
    function drawTicks() {
        document.querySelectorAll(".gauge-ticks").forEach((g) => {
            g.innerHTML = "";
            const cx = 120,
                cy = 140,
                rOuter = 100,
                rInner = 90;
            for (let i = 0; i <= 10; i += 2) {
                const angle = Math.PI - (i / 10) * Math.PI;
                const x1 = cx + rOuter * Math.cos(angle);
                const y1 = cy - rOuter * Math.sin(angle);
                const x2 = cx + rInner * Math.cos(angle);
                const y2 = cy - rInner * Math.sin(angle);
                const line = document.createElementNS("http://www.w3.org/2000/svg", "line");
                line.setAttribute("x1", x1.toFixed(1));
                line.setAttribute("y1", y1.toFixed(1));
                line.setAttribute("x2", x2.toFixed(1));
                line.setAttribute("y2", y2.toFixed(1));
                g.appendChild(line);
            }
        });
    }
    drawTicks();

    // Segmented Control
    const segGroup = document.getElementById("stress_level_group");
    const stressHiddenInput = document.getElementById("stress_level");

    if (segGroup) {
        segGroup.querySelectorAll(".seg-btn").forEach((btn) => {
            btn.addEventListener("click", () => {
                segGroup.querySelectorAll(".seg-btn").forEach((b) => b.classList.remove("active"));
                btn.classList.add("active");
                stressHiddenInput.value = btn.dataset.value;
                clearFieldError(stressHiddenInput);
            });
        });
    }

    // Field Helpers
    function fieldWrapper(input) {
        if (!input) return null;
        return input.closest(".field");
    }

    function setFieldError(input, message) {
        if (!input) return;
        const wrap = fieldWrapper(input);
        if (!wrap) return;
        wrap.classList.add("field-error");
        const msgEl = wrap.querySelector(".error-msg");
        if (msgEl) msgEl.textContent = message;
    }

    function clearFieldError(input) {
        if (!input) return;
        const wrap = fieldWrapper(input);
        if (!wrap) return;
        wrap.classList.remove("field-error");
        const msgEl = wrap.querySelector(".error-msg");
        if (msgEl) msgEl.textContent = "";
    }

    function clearAllErrors() {
        if (!form) return;
        form.querySelectorAll(".field").forEach((f) => f.classList.remove("field-error"));
        form.querySelectorAll(".error-msg").forEach((m) => (m.textContent = ""));
    }

    // Validation
    function validate(payload) {
        const errors = [];
        const numericChecks = [
            ["age", 10, 100],
            ["avg_daily_usage_hours", 0, 24],
            ["daily_unlocks", 0, Infinity],
            ["study_hours", 0, 24],
            ["physical_activity_hours", 0, 24],
            ["sleep_hours_per_night", 0, 24],
        ];

        numericChecks.forEach(([key, min, max]) => {
            const input = document.getElementById(key);
            const val = payload[key];
            if (val === "" || val === null || Number.isNaN(val)) {
                errors.push([input, "This field is required."]);
            } else if (val < min || val > max) {
                errors.push([input, `Must be between ${min} and ${max === Infinity ? "0+" : max}.`]);
            }
        });

        ["gender", "country", "academic_level", "most_used_platform", "purpose_of_use"].forEach((key) => {
            const input = document.getElementById(key);
            if (!payload[key] || String(payload[key]).trim() === "") {
                errors.push([input, "This field is required."]);
            }
        });

        if (!payload.stress_level) {
            errors.push([stressHiddenInput, "Please select a stress level."]);
        }

        return errors;
    }

    // Collect Payload
    function collectPayload() {
        const fd = new FormData(form);
        return {
            age: fd.get("age") === "" ? NaN : parseInt(fd.get("age"), 10),
            gender: fd.get("gender") || "",
            country: (fd.get("country") || "").trim(),
            academic_level: fd.get("academic_level") || "",
            most_used_platform: fd.get("most_used_platform") || "",
            purpose_of_use: fd.get("purpose_of_use") || "",
            avg_daily_usage_hours: fd.get("avg_daily_usage_hours") === "" ? NaN : parseFloat(fd.get("avg_daily_usage_hours")),
            daily_unlocks: fd.get("daily_unlocks") === "" ? NaN : parseInt(fd.get("daily_unlocks"), 10),
            study_hours: fd.get("study_hours") === "" ? NaN : parseFloat(fd.get("study_hours")),
            physical_activity_hours: fd.get("physical_activity_hours") === "" ? NaN : parseFloat(fd.get("physical_activity_hours")),
            sleep_hours_per_night: fd.get("sleep_hours_per_night") === "" ? NaN : parseFloat(fd.get("sleep_hours_per_night")),
            stress_level: fd.get("stress_level") || "",
        };
    }

    // UI State Management
    function hideAllStates() {
        [stateIdle, stateLoading, stateResult, stateError].forEach(el => {
            if (el) el.classList.add("hidden");
        });
    }

    function showState(name) {
        hideAllStates();
        const states = {
            idle: stateIdle,
            loading: stateLoading,
            result: stateResult,
            error: stateError
        };
        if (states[name]) {
            states[name].classList.remove("hidden");
        }
    }

    function setSubmitting(isSubmitting) {
        if (!submitBtn) return;
        submitBtn.disabled = isSubmitting;
        submitBtn.classList.toggle("loading", isSubmitting);
    }

    function bandFor(score) {
        if (score < 4) {
            return {
                label: "Strained",
                context: "Your patterns suggest significant strain. Consider prioritizing sleep, reducing screen time, and reaching out to someone you trust."
            };
        }
        if (score < 7) {
            return {
                label: "Balanced",
                context: "Your habits show a balanced baseline. Small improvements in sleep or stress management could boost your wellness further."
            };
        }
        return {
            label: "Strong",
            context: "Your habits point to a resilient, well-supported baseline. Keep up the great work maintaining these healthy patterns."
        };
    }

    function renderResult(score) {
        const clamped = Math.max(0, Math.min(10, score));
        const { label, context } = bandFor(clamped);

        if (scoreNumberEl) scoreNumberEl.textContent = score.toFixed(2);
        if (scoreBandEl) scoreBandEl.textContent = label;
        if (scoreContextEl) scoreContextEl.textContent = context;

        if (gaugeFill) {
            gaugeFill.style.transition = "none";
            gaugeFill.style.strokeDashoffset = String(GAUGE_ARC_LENGTH);
            requestAnimationFrame(() => {
                gaugeFill.style.transition = "";
                const offset = GAUGE_ARC_LENGTH * (1 - clamped / 10);
                gaugeFill.style.strokeDashoffset = String(offset);
            });
        }

        showState("result");
    }

    function renderError(label, copy) {
        if (errorLabelEl) errorLabelEl.textContent = label;
        if (errorCopyEl) errorCopyEl.textContent = copy;
        showState("error");
    }

    // Apply Server Validation Errors
    function applyServerValidationErrors(detail) {
        if (!Array.isArray(detail)) return false;
        let matched = false;
        detail.forEach((err) => {
            const field = Array.isArray(err.loc) ? err.loc[err.loc.length - 1] : null;
            const input = field ? document.getElementById(field) : null;
            const target = field === "stress_level" ? stressHiddenInput : input;
            if (target) {
                setFieldError(target, err.msg || "Invalid value.");
                matched = true;
            }
        });
        return matched;
    }

    // Form Submit
    if (form) {
        form.addEventListener("submit", async (e) => {
            e.preventDefault();
            clearAllErrors();

            const payload = collectPayload();
            const clientErrors = validate(payload);

            if (clientErrors.length > 0) {
                clientErrors.forEach(([input, msg]) => input && setFieldError(input, msg));
                if (clientErrors[0][0]) clientErrors[0][0].focus();
                return;
            }

            setSubmitting(true);
            showState("loading");

            if (progressBar) {
                progressBar.style.animation = "none";
                progressBar.style.width = "0%";
                requestAnimationFrame(() => {
                    progressBar.style.animation = "progress-load 2s ease-in-out infinite";
                });
            }

            try {
                const res = await fetch(`${API_BASE}/predict`, {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload),
                });

                if (res.status === 422) {
                    const body = await res.json().catch(() => null);
                    const matched = body && applyServerValidationErrors(body.detail);
                    renderError(
                        "Check Your Inputs",
                        matched ?
                        "The API rejected some fields — details are marked on the form." :
                        "Please review your inputs and try again."
                    );
                    return;
                }

                if (!res.ok) {
                    let detailMsg = `The API responded with status ${res.status}.`;
                    const body = await res.json().catch(() => null);
                    if (body && typeof body.detail === "string") detailMsg = body.detail;
                    renderError("Prediction Failed", detailMsg);
                    return;
                }

                const data = await res.json();
                if (typeof data.predicted_mental_health_score !== "number") {
                    renderError("Unexpected Response", "The API responded but the score was missing.");
                    return;
                }

                renderResult(data.predicted_mental_health_score);

            } catch (err) {
                renderError(
                    "Can't Reach Server",
                    `Couldn't connect to ${API_BASE}. Make sure the backend is running.`
                );
            } finally {
                setSubmitting(false);
            }
        });
    }

    // Live Error Clearing
    if (form) {
        form.querySelectorAll("input, select").forEach((el) => {
            el.addEventListener("input", () => clearFieldError(el));
            el.addEventListener("change", () => clearFieldError(el));
        });
    }

    // Reset Buttons
    if (resetBtn) {
        resetBtn.addEventListener("click", () => {
            showState("idle");
        });
    }
    if (errorRetryBtn) {
        errorRetryBtn.addEventListener("click", () => {
            showState("idle");
        });
    }

    // Check API Health
    async function checkApiHealth() {
        try {
            const response = await fetch(`${API_BASE}/health`);
            if (response.ok) {
                const data = await response.json();
                console.log("✅ API is healthy:", data);
                return true;
            }
        } catch (error) {
            console.warn("⚠️ API not reachable:", error.message);
            return false;
        }
        return false;
    }

    checkApiHealth();

})();