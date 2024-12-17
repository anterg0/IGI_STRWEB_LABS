const express = require('express');
const authMiddleware = require('../middlewares/authMiddleware');
const router = express.Router();

router.get('/user', authMiddleware, async (req, res) => {
    try {
        const user = req.user;
        res.json(user);
    } catch (error) {
        res.status(500).json({ error: 'Ошибка сервера' });
    }
});

module.exports = router;
