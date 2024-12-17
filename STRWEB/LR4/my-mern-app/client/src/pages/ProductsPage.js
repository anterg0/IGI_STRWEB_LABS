import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ProductPage = () => {
    const { id } = useParams();
    const [product, setProduct] = useState(null);

    useEffect(() => {
        axios.get(`http://localhost:5000/api/products/${id}`)
            .then(response => setProduct(response.data))
            .catch(error => console.error(error));
    }, [id]);

    if (!product) {
        return <p>Загрузка...</p>;
    }

    return (
        <div>
            <h1>{product.name}</h1>
            <p>Цена: {product.price}</p>
            <p>Описание: {product.description}</p>
            <p>Производитель: {product.manufacturer}</p>
        </div>
    );
};

export default ProductPage;
