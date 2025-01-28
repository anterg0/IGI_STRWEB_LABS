const express = require('express');
const bcrypt = require('bcrypt');
const { body, validationResult } = require('express-validator');
const jwt = require('jsonwebtoken');
const User = require('../models/User');
const router = express.Router();
const passport = require('passport');
require('../config/passport-setup');

const userValidation = [
    body('name').notEmpty().withMessage('Имя обязательно').isString().withMessage('Имя должно быть строкой').isLength({ min: 2, max: 50 }).withMessage('Имя должно быть от 2 до 50 символов'),
    body('email').isEmail().withMessage('Неверный формат электронной почты').normalizeEmail(),
    body('password').optional().isLength({ min: 6 }).withMessage('Пароль должен содержать не менее 6 символов'),
  ];

const JWT_SECRET = process.env.JWT_SECRET;

router.post('/register', userValidation, async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { name, email, password, city } = req.body;

    const newUser = new User({ name, email, password: password, city });

    try {
        await newUser.save();
        res.status(201).json({ message: 'Пользователь зарегистрирован' });
    } catch (err) {
        res.status(400).json({ error: err.message });
    }
});

router.post('/login', async (req, res) => {
    const { email, password } = req.body;

    const user = await User.findOne({ email });
    if (!user) {
        return res.status(404).json({ error: 'Пользователь не найден' });
    }

    const isValidPassword = await bcrypt.compare(password, user.password);
    if (!isValidPassword) {
        return res.status(401).json({ error: 'Неверный пароль' });
    }

    const token = jwt.sign({ id: user._id }, JWT_SECRET, { expiresIn: '1h' });
    res.json({ token, message: 'Вход выполнен успешно' });
});

router.get('/google', passport.authenticate('google', {
    scope: ['profile', 'email'],
}));

router.get('/google/callback', passport.authenticate('google', {
    failureRedirect: '/login',
}), (req, res) => {
    res.redirect(`http://localhost:3000/dashboard?token=${req.user.token}`); 
});

module.exports = router;
