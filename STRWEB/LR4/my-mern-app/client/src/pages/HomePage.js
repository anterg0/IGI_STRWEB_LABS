import React, { useEffect, useState } from 'react';
import axios from 'axios';

const HomePage = () => {
    const [latestNews, setLatestNews] = useState(null);

    useEffect(() => {
        axios.get('/api/news')
            .then(response => {
                const sortedNews = response.data.sort((a, b) => new Date(b.publishedAt) - new Date(a.publishedAt));
                setLatestNews(sortedNews[0]);
            })
            .catch(error => console.error('Ошибка при получении новости:', error));
    }, []);

    const CustomComponent = ({ number = 3 }) => {
        return <h4>Число {number}</h4>;
    };

    return (
        <div className="page-container">
            {/* <CustomComponent number="5" /> */}
            <h1 className="page-title">Главная страница</h1>

            {latestNews ? (
                <div className="news-block">
                    <h2 className="news-title">{latestNews.title}</h2>
                    <p className="news-date">Дата: {new Date(latestNews.publishedAt).toLocaleDateString()}</p>
                    <p className="news-text">{latestNews.content}</p>
                </div>
            ) : (
                <p>Загрузка новости...</p>
            )}
        </div>
    );
};

export default HomePage;
