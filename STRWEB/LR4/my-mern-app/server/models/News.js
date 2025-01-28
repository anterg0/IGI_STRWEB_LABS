const mongoose = require('mongoose');

const newsSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    minlength: 5,
    maxlength: 255,
  },
  content: {
    type: String,
    required: true,
    minlength: 10,
  },
  image: {
    type: String,
    default: '',
  },
  publishedAt: {
    type: Date,
    default: Date.now,
  },
});

module.exports = mongoose.model('News', newsSchema);
