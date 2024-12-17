import React, { useState, useEffect } from 'react';

const Footer = () => {
    const [currentTime, setCurrentTime] = useState('');
    const [userTimezone, setUserTimezone] = useState('');

    useEffect(() => {
        const localDate = new Date().toLocaleString("en-US", { timeZoneName: "short" });
        const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

        setCurrentTime(localDate);
        setUserTimezone(timezone);
    }, []);

    return (
        <footer className="footer">
            <p>Текущая дата (локальная): {currentTime}</p>
            <p>Тайм-зона пользователя: {userTimezone}</p>
            <p>Текущая дата (UTC): {new Date().toISOString()}</p>
        </footer>
    );
};

export default Footer;
