window.addEventListener('DOMContentLoaded', (event) => {
    // Запрос даты рождения при загрузке страницы
    const dobInput = prompt("Введите вашу дату рождения (в формате YYYY-MM-DD):");

    if (!dobInput) {
        alert("Дата рождения не была введена.");
        return;
    }

    const birthDate = new Date(dobInput);
    const today = new Date();
    const age = today.getFullYear() - birthDate.getFullYear();
    const month = today.getMonth() - birthDate.getMonth();
    const day = today.getDate() - birthDate.getDate();

    const isAdult = age > 18 || (age === 18 && month >= 0 && day >= 0);

    const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
    const dayOfWeek = daysOfWeek[birthDate.getDay()];

    const messageElement = document.getElementById('message');
    if (!isAdult) {
        messageElement.innerHTML = `Вы совершеннолетний. Ваш день рождения был в ${dayOfWeek}.`;
        alert("Вы несовершеннолетний. Для использования сайта требуется разрешение родителей.");
        messageElement.innerHTML = "Вы несовершеннолетний.";
    }
});