document.addEventListener("DOMContentLoaded", async function() {
    const preloader = document.getElementById("preloader");

    try {

        const [factResponse, jokeResponse] = await Promise.all([
            fetch("https://catfact.ninja/fact").then(res => res.json()),
            fetch("https://official-joke-api.appspot.com/random_joke").then(res => res.json())
        ]);

        document.getElementById("catFact").textContent = factResponse.fact;
        document.getElementById("joke").textContent = `${jokeResponse.setup} - ${jokeResponse.punchline}`;

        preloader.style.display = "none";
    } catch (error) {
        console.error("Ошибка при загрузке данных:", error);
        preloader.style.display = "none";
        alert("Не удалось загрузить данные.");
    }
});