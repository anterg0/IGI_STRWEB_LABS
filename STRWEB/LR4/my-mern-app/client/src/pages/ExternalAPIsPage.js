import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ExternalApiPage = () => {
    const [joke, setJoke] = useState('');
    const [quote, setQuote] = useState('');

    useEffect(() => {
        axios.get('https://v2.jokeapi.dev/joke/Programming?type=single')
            .then(response => setJoke(response.data.joke))
            .catch(error => console.error(error));
    }, []);

    useEffect(() => {
        axios.get('https://catfact.ninja/fact')
            .then(response => setQuote(response.data.fact))
            .catch(error => console.error('Ошибка при получении цитаты:', error));
    }, []);

    return (
        <div className="page-container">
            <h1>Внешний API</h1>

            <h2>Случайная шутка:</h2>
            <p>{joke || 'Загрузка...'}</p>

            <h2>Случайный факт про котов:</h2>
            <p>{quote || 'Загрузка...'}</p>
        </div>
    );
};

export default ExternalApiPage;
