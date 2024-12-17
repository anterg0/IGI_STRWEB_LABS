import React, { useEffect, useState, useContext } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { UserContext } from '../components/UserProvider';

const ManufacturersPage = () => {
    const [manufacturers, setManufacturers] = useState([]);
    const [search, setSearch] = useState('');
    const [sort, setSort] = useState('');
    const { user } = useContext(UserContext);
    const navigate = useNavigate();

    useEffect(() => {
        axios.get('/api/manufacturers', {
            params: { search, sort }
        })
            .then(response => setManufacturers(response.data))
            .catch(error => console.error('Ошибка при получении производителей:', error));
    }, [search, sort]);

    const handleDelete = async (id) => {
        if (window.confirm('Вы уверены, что хотите удалить этого производителя?')) {
            try {
                const token = localStorage.getItem('token');
                await axios.delete(`/api/manufacturers/${id}`, {
                    headers: { Authorization: `Bearer ${token}` },
                });
                setManufacturers(manufacturers.filter(manufacturer => manufacturer._id !== id));
            } catch (error) {
                console.error('Ошибка при удалении производителя:', error);
            }
        }
    };

    return (
        <div className="page-container">
            <h1 className="page-title">Производители</h1>

            <div className="filter-container">
                <input
                    type="text"
                    className="filter-input"
                    placeholder="Поиск производителей..."
                    value={search}
                    onChange={e => setSearch(e.target.value)}
                />

                <select
                    className="filter-select"
                    value={sort}
                    onChange={e => setSort(e.target.value)}
                >
                    <option value="">По умолчанию</option>
                    <option value="name">Имя</option>
                    <option value="-country">Страна</option>
                </select>

                <button className="filter-button">
                    Применить
                </button>
            </div>

            {user && (
                <button
                    className="crud-button create-button"
                    onClick={() => navigate('/manufacturers/create')}
                >
                    Добавить производителя
                </button>
            )}

            {manufacturers.length === 0 ? (
                <p className="no-products">Производители не найдены.</p>
            ) : (
                <div className="products-list">
                    {manufacturers.map(manufacturer => (
                        <div key={manufacturer._id} className="product-item">
                            <h3 className="product-name">{manufacturer.name}</h3>
                            <p className="product-price">Страна: {manufacturer.country || 'Не указана'}</p>

                            {user && (
                                <div className="crud-buttons">
                                    <button
                                        className="crud-button edit-button"
                                        onClick={() => navigate(`/manufacturers/edit/${manufacturer._id}`)}
                                    >
                                        Редактировать
                                    </button>
                                    <button
                                        className="crud-button delete-button"
                                        onClick={() => handleDelete(manufacturer._id)}
                                    >
                                        Удалить
                                    </button>
                                </div>
                            )}
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
};

export default ManufacturersPage;
