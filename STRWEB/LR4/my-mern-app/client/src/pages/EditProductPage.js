import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const EditProductPage = () => {
    const { id } = useParams();
    const [name, setName] = useState('');
    const [manufacturer, setManufacturer] = useState('');
    const [articleCode, setArticleCode] = useState('');
    const [price, setPrice] = useState('');
    const [manufacturers, setManufacturers] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        // Загружаем товар
        const fetchProduct = async () => {
            try {
                const response = await axios.get(`/api/products/${id}`);
                const product = response.data;
                setName(product.name);
                setManufacturer(product.manufacturer._id);
                setArticleCode(product.articleCode);
                setPrice(product.price);
            } catch (error) {
                console.error('Ошибка при получении товара:', error);
            }
        };

        // Загружаем производителей
        const fetchManufacturers = async () => {
            try {
                const response = await axios.get('/api/manufacturers');
                setManufacturers(response.data);
            } catch (error) {
                console.error('Ошибка при получении производителей:', error);
            }
        };

        fetchProduct();
        fetchManufacturers();
    }, [id]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('token');
            await axios.put(
                `/api/products/${id}`,
                { name, manufacturer, articleCode, price },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            navigate('/products');
        } catch (error) {
            console.error('Ошибка при редактировании товара:', error);
        }
    };

    return (
        <div className="page-container">
            <h1>Редактировать товар</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Название"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                />
                {/* Выбор производителя */}
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
                <button type="submit" className="filter-button">
                    Сохранить
                </button>
            </form>
        </div>
    );
};

export default EditProductPage;
