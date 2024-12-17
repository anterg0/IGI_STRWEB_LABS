import React, { useEffect, useState, useContext } from 'react';
import axios from 'axios';
import { Link, useNavigate } from 'react-router-dom';
import { UserContext } from '../components/UserProvider';

const ProductsPage = () => {
    const [products, setProducts] = useState([]);
    const [search, setSearch] = useState('');
    const [sort, setSort] = useState('');
    const { user } = useContext(UserContext);
    const navigate = useNavigate();

    const fetchData = async () => {
        try {
            const response = await axios.get('/api/products', {
                params: { search, sort },
            });
            setProducts(response.data);
        } catch (error) {
            console.error('Ошибка при получении товаров:', error);
        }
    };

    useEffect(() => {
        fetchData();
    }, []);

    const handleDelete = async (id) => {
        if (window.confirm('Вы уверены, что хотите удалить товар?')) {
            try {
                const token = localStorage.getItem('token');
                await axios.delete(`/api/products/${id}`, {
                    headers: { Authorization: `Bearer ${token}` },
                });
                fetchData();
            } catch (error) {
                console.error('Ошибка при удалении товара:', error);
            }
        }
    };

    return (
        <div className="page-container">
            <h1 className="page-title">Список товаров</h1>

            {/* Панель поиска и сортировки */}
            <div className="filter-container">
                <input
                    type="text"
                    className="filter-input"
                    placeholder="Поиск товаров..."
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
                    <option value="-price">Цена по убыванию</option>
                </select>

                <button className="filter-button" onClick={fetchData}>Применить</button>
            </div>

            {/* Кнопка добавления товара (только для авторизованных пользователей) */}
            {user && (
                <button
                    className="crud-button create-button"
                    onClick={() => navigate('/products/create')}
                >
                    Добавить товар
                </button>
            )}

            {/* Список товаров */}
            <ul className="products-list">
                {products.length > 0 ? (
                    products.map(product => (
                        <li key={product._id} className="product-item">
                            <h2 className="product-name">{product.name}</h2>
                            <p className="product-code">Артикул: {product.articleCode}</p>
                            <p className="product-manufacturer">
                                Производитель: {product.manufacturer?.name || 'Не указано'}
                            </p>
                            <p className="product-price">Цена: {product.price} руб.</p>

                            {/* Кнопки редактирования и удаления (только для авторизованных пользователей) */}
                            {user && (
                                <div className="crud-buttons">
                                    <button
                                        className="crud-button edit-button"
                                        onClick={() => navigate(`/products/edit/${product._id}`)}
                                    >
                                        Редактировать
                                    </button>
                                    <button
                                        className="crud-button delete-button"
                                        onClick={() => handleDelete(product._id)}
                                    >
                                        Удалить
                                    </button>
                                </div>
                            )}
                        </li>
                    ))
                ) : (
                    <p className="no-products">Товары не найдены.</p>
                )}
            </ul>
        </div>
    );
};

export default ProductsPage;
