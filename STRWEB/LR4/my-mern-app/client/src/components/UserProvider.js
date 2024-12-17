import React, { useState, useEffect, createContext } from 'react';
import axios from 'axios';

export const UserContext = createContext();

const UserProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const token = localStorage.getItem('token');

        if (token && !user) {
            fetchUserData(token);
        } else {
            setLoading(false);
        }
    }, []);

    const fetchUserData = async (token) => {
        try {
            const response = await axios.get('/api/user', {
                headers: { Authorization: `Bearer ${token}` }
            });
            const userInfo = {
                name: response.data.name,
                email: response.data.email,
                city: response.data.city,
            };
            localStorage.setItem('user', JSON.stringify(userInfo));
            setUser(userInfo);
        } catch (error) {
            console.error('Ошибка при получении данных пользователя:', error);
        } finally {
            setLoading(false);
        }
    };

    const loginUser = (userData) => {
        setUser(userData);
    };

    const logoutUser = () => {
        setUser(null);
        localStorage.removeItem('token');
        localStorage.removeItem('user');
    };

    return (
        <UserContext.Provider value={{ user, loginUser, logoutUser, loading }}>
            {children}
        </UserContext.Provider>
    );
};

export default UserProvider;
