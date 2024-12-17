import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const CreateNewsPage = () => {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [message, setMessage] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!title || !content) {
            setMessage('Все поля обязательны!');
            return;
        }

        try {
            const token = localStorage.getItem('token');
            await axios.post('/api/news', { title, content }, {
                headers: { Authorization: `Bearer ${token}` },
            });
            navigate('/news');
        } catch (error) {
            console.error('Ошибка при добавлении новости:', error);
            setMessage('Ошибка при добавлении новости. Попробуйте снова.');
        }
    };

    return (
        <div className="page-container">
            <h1>Добавить новость</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Заголовок"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    required
                />
                <textarea
                    placeholder="Текст новости"
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    required
                />
                <button type="submit" className="filter-button">Добавить новость</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default CreateNewsPage;
