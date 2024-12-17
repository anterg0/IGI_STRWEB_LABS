import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const CreateManufacturerPage = () => {
    const [name, setName] = useState('');
    const [country, setCountry] = useState('');
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!name || !country) {
            setMessage('Все поля обязательны!');
            return;
        }

        try {
            const token = localStorage.getItem('token');
            await axios.post(
                '/api/manufacturers',
                { name, country },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            navigate('/manufacturers');
        } catch (error) {
            console.error('Ошибка при добавлении производителя:', error);
            setMessage('Ошибка при добавлении производителя. Попробуйте снова.');
        }
    };

    return (
        <div className="page-container">
            <h1>Добавить производителя</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Название"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                />
                <input
                    type="text"
                    placeholder="Страна"
                    value={country}
                    onChange={(e) => setCountry(e.target.value)}
                    required
                />
                <button type="submit" className="filter-button">Добавить</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default CreateManufacturerPage;
