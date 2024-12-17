const express = require('express');
const Product = require('../models/Product');
const authMiddleware = require('../middlewares/authMiddleware');
const Manufacturer = require('../models/Manufacturer');
const router = express.Router();

router.get('/', async (req, res) => {
    const { search, sort } = req.query;
    const query = {};

    if (search) {
        query.name = { $regex: search, $options: 'i' };
    }

    try {
        const products = await Product.find(query)
            .populate('manufacturer', 'name country')
            .sort(sort || 'createdAt');
        res.json(products);
    } catch (err) {
        console.log(err);
        res.status(500).json({ error: err.message });
    }
});

router.get('/:id', async (req, res) => {
    try {
        const product = await Product.findById(req.params.id).populate('manufacturer', 'name country');
        if (!product) return res.status(404).json({ error: 'Товар не найден' });
        res.json(product);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

router.post('/', authMiddleware, async (req, res) => {
    const { name, manufacturer, articleCode, price } = req.body;

    try {
        const newProduct = new Product({ name, manufacturer, articleCode, price });
        await newProduct.save();
        res.status(201).json(newProduct);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

router.put('/:id', authMiddleware, async (req, res) => {
    try {
        const product = await Product.findByIdAndUpdate(req.params.id, req.body, { new: true })
            .populate('manufacturer', 'name country');
        if (!product) return res.status(404).json({ error: 'Товар не найден' });
        res.json(product);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

router.delete('/:id', authMiddleware, async (req, res) => {
    try {
        const product = await Product.findByIdAndDelete(req.params.id);
        if (!product) return res.status(404).json({ error: 'Товар не найден' });
        res.json({ message: 'Товар удалён' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;
