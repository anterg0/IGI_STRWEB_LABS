import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const CreateProductPage = () => {
    const [name, setName] = useState('');
    const [manufacturer, setManufacturer] = useState('');
    const [articleCode, setArticleCode] = useState('');
    const [price, setPrice] = useState('');
    const [manufacturers, setManufacturers] = useState([]);
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        const fetchManufacturers = async () => {
            try {
                const response = await axios.get('/api/manufacturers');
                setManufacturers(response.data);
            } catch (error) {
                console.error('Ошибка при получении производителей:', error);
            }
        };
        fetchManufacturers();
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Валидация на стороне клиента
        if (!name || !manufacturer || !articleCode || !price) {
            setMessage('Все поля обязательны!');
            return;
        }

        try {
            const token = localStorage.getItem('token');
            await axios.post(
                '/api/products',
                { name, manufacturer, articleCode, price },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            navigate('/products');
        } catch (error) {
            console.error('Ошибка при добавлении товара:', error);
            setMessage('Ошибка при добавлении товара. Попробуйте снова.');
        }
    };

    return (
        <div className="page-container">
            <h1>Добавить товар</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Название"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                />
                <select
                    value={manufacturer}
                    onChange={(e) => setManufacturer(e.target.value)}
                    required
                >
                    <option value="">Выберите производителя</option>
                    {manufacturers.map((manufacturer) => (
                        <option key={manufacturer._id} value={manufacturer._id}>
                            {manufacturer.name}
                        </option>
                    ))}
                </select>
                <input
                    type="text"
                    placeholder="Артикул"
                    value={articleCode}
                    onChange={(e) => setArticleCode(e.target.value)}
                    required
                />
                <input
                    type="number"
                    placeholder="Цена"
                    value={price}
                    onChange={(e) => setPrice(e.target.value)}
                    required
                />
                <button type="submit" className="filter-button">Добавить</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default CreateProductPage;
