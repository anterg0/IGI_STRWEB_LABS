document.addEventListener("DOMContentLoaded", () => {
    const countdownElement = document.getElementById("countdown");
    const messageElement = document.getElementById("message");
    const countdownEndKey = "countdownEndTime";

    const now = new Date().getTime();
    let countdownEndTime = localStorage.getItem(countdownEndKey);

    if (!countdownEndTime || now > parseInt(countdownEndTime)) {
        countdownEndTime = now + 60 * 60 * 1000; // 1 час
        localStorage.setItem(countdownEndKey, countdownEndTime);
    }

    const updateCountdown = () => {
        const now = new Date().getTime();
        const remainingTime = parseInt(countdownEndTime) - now;

        if (remainingTime <= 0) {
            countdownElement.textContent = "00:00:00";
            messageElement.textContent = "Отсчет закончен!";
            clearInterval(interval);
            localStorage.removeItem(countdownEndKey); 
            return;
        }

        const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

        countdownElement.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    };

    const interval = setInterval(updateCountdown, 1000);
    updateCountdown();
});
