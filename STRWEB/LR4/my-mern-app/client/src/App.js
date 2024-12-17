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
import CreateProductPage from './pages/CreateProductPage';
import EditProductPage from './pages/EditProductPage';
import CreateManufacturerPage from './pages/CreateManufacturerPage';
import EditManufacturerPage from './pages/EditManufacturerPage';
import NewsPage from './pages/NewsPage';
import CreateNewsPage from './pages/CreateNewsPage';
import EditNewsPage from './pages/EditNewsPage';
import NewsDetailPage from './pages/DetailNewsPage';
import Dashboard from './pages/Dashboard';
import Footer from './components/Footer';

const App = () => {
    return (
        <UserProvider>
            <Router>
                <Navbar />
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/dashboard" element={<Dashboard />} />
                    <Route path="/news" element={<NewsPage />} />
                    <Route path="/news/:id" element={<NewsDetailPage />} />
                    <Route path="/news/create" element={<CreateNewsPage />} />
                    <Route path="/news/edit/:id" element={<EditNewsPage />} />
                    <Route path="/products" element={<ProductPage />} />
                    <Route path="/manufacturers" element={<ManufacturersPage />} />
                    <Route path="/external" element={<ExternalAPIsPage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegisterPage />} />
                    <Route path="/products/create" element={<CreateProductPage />}/>
                    <Route path="/products/edit/:id" element={<EditProductPage />} />
                    <Route path="/manufacturers/create" element={<CreateManufacturerPage />} />
                    <Route path="/manufacturers/edit/:id" element={<EditManufacturerPage />} />
                </Routes>
                <Footer/>
            </Router>
        </UserProvider>
    );
};

export default App;
