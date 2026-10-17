// ==========================================
// SOLUTIONS: Timers and Intervals
// ==========================================

// --- Solution 1: setTimeout ---
setTimeout(() => {
    console.log('Welcome to the dashboard!');
}, 3000);

// --- Solution 2: setInterval & clearInterval ---
let countdown = 5;

const countdownInterval = setInterval(() => {
    if (countdown > 0) {
        console.log(`Countdown: ${countdown}`);
        countdown--;
    } else {
        console.log('Liftoff!');
        clearInterval(countdownInterval);
    }
}, 1000);