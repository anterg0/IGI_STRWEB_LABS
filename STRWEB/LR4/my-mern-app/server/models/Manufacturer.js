const mongoose = require('mongoose');

const manufacturerSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    unique: true,
    maxlength: 100,
  },
}, { timestamps: true });

module.exports = mongoose.model('Manufacturer', manufacturerSchema);
