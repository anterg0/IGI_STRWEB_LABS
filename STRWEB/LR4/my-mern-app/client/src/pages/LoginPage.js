import React, { useState, useContext } from 'react';
import axios from 'axios';
import { UserContext } from '../components/UserProvider';
import { useNavigate } from 'react-router-dom';
import { jwtDecode } from 'jwt-decode';

const LoginPage = () => {
    const { loginUser } = useContext(UserContext);
    const [formData, setFormData] = useState({
        email: '',
        password: '',
    });

    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post('/api/auth/login', formData);
            const { token } = response.data;

            localStorage.setItem('token', token);

            const decodedToken = jwtDecode(token);
            loginUser(decodedToken);

            setMessage(`Добро пожаловать, ${decodedToken.name || 'Пользователь'}!`);
            navigate('/');
        } catch (error) {
            console.error('Ошибка входа:', error.response?.data?.error || error.message);
            setMessage(error.response?.data?.error || 'Ошибка входа. Проверьте данные.');
        }
    };

    return (
        <div className="page-container">
            <h1>Вход</h1>
            <form onSubmit={handleSubmit}>
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
                <button type="submit">Войти</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default LoginPage;
