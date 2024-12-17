// src/pages/EditNewsPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useNavigate, useParams } from 'react-router-dom';

const EditNewsPage = () => {
    const { id } = useParams();
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const navigate = useNavigate();

    useEffect(() => {
        axios.get(`/api/news/${id}`)
            .then(response => {
                setTitle(response.data.title);
                setContent(response.data.content);
            })
            .catch(error => console.error('Ошибка при получении новости:', error));
    }, [id]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const token = localStorage.getItem('token');
            await axios.put(`/api/news/${id}`, { title, content }, {
                headers: { Authorization: `Bearer ${token}` },
            });
            navigate('/news');
        } catch (error) {
            console.error('Ошибка при редактировании новости:', error);
        }
    };

    return (
        <div className="page-container">
            <h1>Редактировать новость</h1>
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
                <button type="submit" className="filter-button">Сохранить изменения</button>
            </form>
        </div>
    );
};

export default EditNewsPage;
