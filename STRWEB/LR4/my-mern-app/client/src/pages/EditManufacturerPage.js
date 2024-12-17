import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const EditManufacturerPage = () => {
    const { id } = useParams();
    const [name, setName] = useState('');
    const [country, setCountry] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        // Загружаем данные производителя
        const fetchManufacturer = async () => {
            try {
                const response = await axios.get(`/api/manufacturers/${id}`);
                setName(response.data.name);
                setCountry(response.data.country);
            } catch (error) {
                console.error('Ошибка при получении данных производителя:', error);
            }
        };
        fetchManufacturer();
    }, [id]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('token');
            await axios.put(
                `/api/manufacturers/${id}`,
                { name, country },
                { headers: { Authorization: `Bearer ${token}` } }
            );
            navigate('/manufacturers');
        } catch (error) {
            console.error('Ошибка при редактировании производителя:', error);
        }
    };

    return (
        <div className="page-container">
            <h1>Редактировать производителя</h1>
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
                />
                <button type="submit" className="filter-button">Сохранить</button>
            </form>
        </div>
    );
};

export default EditManufacturerPage;
