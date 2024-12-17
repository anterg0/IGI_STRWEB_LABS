import React, { useState, useEffect, useContext } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { UserContext } from '../components/UserProvider';

const NewsPage = () => {
    const { user } = useContext(UserContext);
    const [news, setNews] = useState([]);

    useEffect(() => {
        axios.get('/api/news')
            .then(response => setNews(response.data))
            .catch(error => console.error('Ошибка при получении новостей:', error));
    }, []);

    const handleDelete = async (id) => {
        if (window.confirm('Вы уверены, что хотите удалить эту новость?')) {
            try {
                const token = localStorage.getItem('token');
                await axios.delete(`/api/news/${id}`, {
                    headers: { Authorization: `Bearer ${token}` },
                });
                setNews(news.filter(newsItem => newsItem._id !== id));
            } catch (error) {
                console.error('Ошибка при удалении новости:', error);
            }
        }
    };

    return (
        <div className="page-container">
            <h1 className="page-title">Новости</h1>

            {user && (
                <Link to="/news/create">
                    <button className="filter-button create-button">Добавить новость</button>
                </Link>
            )}

            <div className="products-list">
                {news.length === 0 ? (
                    <p className="no-products">Новости не найдены.</p>
                ) : (
                    news.map(newsItem => (
                        <div key={newsItem._id} className="product-item">
                            <h3 className="product-name">
                                <Link to={`/news/${newsItem._id}`} className="product-link">
                                    {newsItem.title}
                                </Link>
                            </h3>
                            <p className="product-price">Дата: {new Date(newsItem.publishedAt).toLocaleDateString()}</p>
                            <p className="product-content">{newsItem.content}</p>

                            {user && (
                                <div className="crud-buttons">
                                    <Link to={`/news/edit/${newsItem._id}`}>
                                        <button className="crud-button edit-button">Редактировать</button>
                                    </Link>
                                    <button
                                        onClick={() => handleDelete(newsItem._id)}
                                        className="crud-button delete-button"
                                    >
                                        Удалить
                                    </button>
                                </div>
                            )}
                        </div>
                    ))
                )}
            </div>
        </div>
    );
};

export default NewsPage;
