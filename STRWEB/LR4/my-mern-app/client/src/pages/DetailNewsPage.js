import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const NewsDetailPage = () => {
    const { id } = useParams();
    const [newsItem, setNewsItem] = useState(null);

    useEffect(() => {
        axios.get(`/api/news/${id}`)
            .then(response => setNewsItem(response.data))
            .catch(error => console.error('Ошибка при получении новости:', error));
    }, [id]);

    if (!newsItem) return <p>Загрузка...</p>;

    return (
        <div className="page-container">
            <h1>{newsItem.title}</h1>
            <img src={newsItem.image} alt={newsItem.title} className="news-image" />
            <p>{new Date(newsItem.publishedAt).toLocaleString()}</p>
            <p>{newsItem.content}</p>
        </div>
    );
};

export default NewsDetailPage;
