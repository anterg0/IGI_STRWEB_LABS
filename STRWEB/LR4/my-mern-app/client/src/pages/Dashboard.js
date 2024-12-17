import React, { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

const Dashboard = () => {
    const location = useLocation();
    const params = new URLSearchParams(location.search);
    const token = params.get('token');

    useEffect(() => {
        if (token) {
            localStorage.setItem('token', token);
        }
    }, [token]);

    return (
        <div>
            <h1>Добро пожаловать на Dashboard</h1>
        </div>
    );
};

export default Dashboard;
