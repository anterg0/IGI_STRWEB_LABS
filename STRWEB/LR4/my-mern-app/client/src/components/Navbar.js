import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { UserContext } from './UserProvider';

const Navbar = () => {
    const { user, logoutUser } = useContext(UserContext);

    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <Link to="/">Мебельный магазин</Link>
            </div>
            <ul className="navbar-links">
                <li><Link to="/products">Каталог</Link></li>
                <li><Link to="/manufacturers">Производители</Link></li>
                <li><Link to="/external">Внешние API</Link></li>
                <li><Link to="/news">Новости</Link></li>
            </ul>
            <div className="navbar-auth">
                {user ? (
                    <div className="user-info">
                        <span>Привет, {user.name}!</span>
                        <button onClick={logoutUser}>Выйти</button>
                    </div>
                ) : (
                    <div className="auth-links">
                        <Link to="/login">Войти</Link>
                        <Link to="/register">Регистрация</Link>
                    </div>
                )}
            </div>
        </nav>
    );
};

export default Navbar;
