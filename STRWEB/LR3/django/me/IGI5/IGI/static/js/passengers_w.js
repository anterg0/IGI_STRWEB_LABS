
class Passenger {
    constructor(surname, name, flightNumber) {
        this.surname = surname;
        this.name = name;
        this.flightNumber = flightNumber;
    }

    getSurname() {
        return this.surname;
    }

    setSurname(surname) {
        this.surname = surname;
    }

    getName() {
        return this.name;
    }

    setName(name) {
        this.name = name;
    }

    getFlightNumber() {
        return this.flightNumber;
    }

    setFlightNumber(flightNumber) {
        this.flightNumber = flightNumber;
    }

    displayPassengerInfo() {
        return `${this.surname} ${this.name} - Рейс: ${this.flightNumber}`;
    }

    findSameSurname(allPassengers) {
        return allPassengers.filter(passenger => passenger.surname === this.surname);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const passengersList = [];

    document.getElementById('addPassengerBtn').addEventListener('click', function() {
        const surname = document.getElementById('surname').value;
        const name = document.getElementById('name').value;
        const flightNumber = document.getElementById('flightNumber').value;

        if (surname && name && flightNumber) {

            const newPassenger = { surname, name, flightNumber };

            passengersList.push(newPassenger);

            displayPassengers();

            document.getElementById('surname').value = '';
            document.getElementById('name').value = '';
            document.getElementById('flightNumber').value = '';
        } else {
            alert("Пожалуйста, заполните все поля.");
        }
    });

    function displayPassengers() {
        const passengerListDiv = document.getElementById('passengerList');
        passengerListDiv.innerHTML = '';

        passengersList.forEach(passenger => {
            const div = document.createElement('div');
            div.textContent = `${passenger.surname} ${passenger.name} - Рейс: ${passenger.flightNumber}`;
            passengerListDiv.appendChild(div);
        });
    }

    function searchForSameSurname() {
        const surnameToSearch = prompt("Введите фамилию для поиска однофамильцев:");
        const foundPassengers = passengersList.filter(passenger => passenger.surname === surnameToSearch);

        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '';

        if (foundPassengers.length > 1) {
            foundPassengers.forEach(passenger => {
                const div = document.createElement('div');
                div.textContent = `${passenger.surname} ${passenger.name} - Рейс: ${passenger.flightNumber}`;
                resultDiv.appendChild(div);
            });
        } else {
            resultDiv.textContent = 'Однофамильцев не найдено.';
        }
    }
    document.getElementById('searchSurname').addEventListener('click', searchForSameSurname);
});
