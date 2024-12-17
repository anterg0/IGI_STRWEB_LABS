import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import ProductPage from './pages/ProductsPage';
import ManufacturersPage from './pages/ManufacturersPage';
import ExternalAPIsPage from './pages/ExternalAPIsPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import UserProvider from './components/UserProvider';

const App = () => {
    return (
        <UserProvider>
            <Router>
                <Navbar />
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/products/:id" element={<ProductPage />} />
                    <Route path="/manufacturers" element={<ManufacturersPage />} />
                    <Route path="/external" element={<ExternalAPIsPage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegisterPage />} />
                </Routes>
            </Router>
        </UserProvider>
    );
};

export default App;
