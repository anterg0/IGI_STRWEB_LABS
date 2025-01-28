const express = require('express');
const { body, validationResult } = require('express-validator');
const Manufacturer = require('../models/Manufacturer');
const authMiddleware = require('../middlewares/authMiddleware');
const router = express.Router();

const manufacturerValidation = [
    body('name').notEmpty().withMessage('Имя производителя обязательно').isString().withMessage('Имя должно быть строкой'),
    body('country').optional().isString().withMessage('Страна должна быть строкой'),
  ];

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

router.post('/', authMiddleware, manufacturerValidation, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
  
    const { name, country } = req.body;
    try {
      const newManufacturer = new Manufacturer({ name, country });
      await newManufacturer.save();
      res.status(201).json(newManufacturer);
    } catch (err) {
      res.status(400).json({ error: err.message });
    }
  });
  

  router.put('/:id', authMiddleware, manufacturerValidation, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }
  
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
