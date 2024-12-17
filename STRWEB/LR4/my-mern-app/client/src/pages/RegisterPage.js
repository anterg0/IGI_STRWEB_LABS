import React, { useState } from 'react';
import axios from 'axios';

const RegisterPage = () => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        city: '',
    });

    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/auth/register', formData);
            setMessage('Регистрация успешна! Пожалуйста, войдите в систему.');
        } catch (error) {
            console.error('Ошибка регистрации:', error.response?.data?.error || error.message);
            setMessage(error.response?.data?.error || 'Ошибка регистрации. Попробуйте снова.');
        }
    };

    return (
        <div className="page-container">
            <h1>Регистрация</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    name="name"
                    placeholder="Имя"
                    value={formData.name}
                    onChange={handleChange}
                />
                <input
                    type="email"
                    name="email"
                    placeholder="Электронная почта"
                    value={formData.email}
                    onChange={handleChange}
                />
                <input
                    type="password"
                    name="password"
                    placeholder="Пароль"
                    value={formData.password}
                    onChange={handleChange}
                />
                <input
                    type="text"
                    name="city"
                    placeholder="Город"
                    value={formData.city}
                    onChange={handleChange}
                />
                <button type="submit">Зарегистрироваться</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default RegisterPage;
