import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const HomePage = () => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/api/products')
            .then(response => setProducts(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Каталог товаров</h1>
            <div>
                {products.length === 0 ? (
                    <p>Товары не найдены</p>
                ) : (
                    <ul>
                        {products.map(product => (
                            <li key={product._id}>
                                <Link to={`/products/${product._id}`}>
                                    <h3>{product.name}</h3>
                                    <p>Цена: {product.price}</p>
                                </Link>
                            </li>
                        ))}
                    </ul>
                )}
            </div>
        </div>
    );
};

export default HomePage;
