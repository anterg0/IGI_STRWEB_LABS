const express = require('express');
const Product = require('../models/Product');
const authMiddleware = require('../middlewares/authMiddleware');
const router = express.Router();

router.get('/', async (req, res) => {
    const products = await Product.find();
    res.json(products);
});

router.post('/', authMiddleware, async (req, res) => {
    const { title, manufacturer, price } = req.body;

    try {
        const newProduct = new Product({ title, manufacturer, price });
        await newProduct.save();
        res.status(201).json(newProduct);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

module.exports = router;
