const express = require('express');
const { body, validationResult } = require('express-validator');
const News = require('../models/News');
const authMiddleware = require('../middlewares/authMiddleware');
const router = express.Router();
const upload = require('../middlewares/uploadMiddleware');

const newsValidation = [
  body('title').notEmpty().withMessage('Заголовок обязателен').isString().withMessage('Заголовок должен быть строкой').isLength({ min: 5, max: 255 }).withMessage('Заголовок должен быть от 5 до 255 символов'),
  body('content').notEmpty().withMessage('Контент обязателен').isString().withMessage('Контент должен быть строкой').isLength({ min: 10 }).withMessage('Контент должен быть не менее 10 символов'),
];

router.post('/', authMiddleware, upload.single('image'), newsValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const { title, content } = req.body;
  let imageUrl = '';

  if (req.file) {
    imageUrl = `/uploads/${req.file.filename}`;
  }

  try {
    const newNews = new News({ title, content, image: imageUrl });
    await newNews.save();
    res.status(201).json(newNews);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

router.get('/', async (req, res) => {
  try {
    const news = await News.find();
    res.json(news);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.get('/:id', async (req, res) => {
  try {
    const news = await News.findById(req.params.id);
    if (!news) return res.status(404).json({ error: 'News not found' });
    res.json(news);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

router.put('/:id', authMiddleware, upload.single('image'), newsValidation, async (req, res) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({ errors: errors.array() });
  }

  const { title, content } = req.body;
  const { id } = req.params;
  let imageUrl = '';

  if (req.file) {
    imageUrl = `/uploads/${req.file.filename}`;
  }

  try {
    const news = await News.findById(id);

    if (!news) {
      return res.status(404).json({ error: 'Новость не найдена' });
    }

    news.title = title;
    news.content = content;
    if (imageUrl) news.image = imageUrl;

    await news.save();
    res.status(200).json(news);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

router.delete('/:id', authMiddleware, async (req, res) => {
  try {
    const deletedNews = await News.findByIdAndDelete(req.params.id);
    if (!deletedNews) return res.status(404).json({ error: 'News not found' });
    res.json({ message: 'News deleted successfully' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
