const express = require('express');
const Manufacturer = require('../models/Manufacturer');
const authMiddleware = require('../middlewares/authMiddleware');
const router = express.Router();

router.get('/', async (req, res) => {
    try {
        const manufacturers = await Manufacturer.find();
        res.json(manufacturers);
    } catch (err) {
        console.error('Ошибка при получении производителей:', err);
        res.status(500).json({ error: 'Ошибка на сервере' });
    }
});

router.get('/:id', async (req, res) => {
    try {
        const product = await Manufacturer.findById(req.params.id);
        if (!product) return res.status(404).json({ error: 'Производитель не найден' });
        res.json(product);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

router.post('/', authMiddleware, async (req, res) => {
    const { name, country } = req.body;
    try {
        const newManufacturer = new Manufacturer({ name, country });
        await newManufacturer.save();
        res.status(201).json(newManufacturer);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

router.put('/:id', authMiddleware, async (req, res) => {
    try {
        const updatedManufacturer = await Manufacturer.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updatedManufacturer) return res.status(404).json({ error: 'Производитель не найден' });
        res.json(updatedManufacturer);
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

router.delete('/:id', authMiddleware, async (req, res) => {
    try {
        const deletedManufacturer = await Manufacturer.findByIdAndDelete(req.params.id);
        if (!deletedManufacturer) return res.status(404).json({ error: 'Производитель не найден' });
        res.json({ message: 'Производитель удалён' });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
});

module.exports = router;
