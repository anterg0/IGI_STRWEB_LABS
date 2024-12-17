const mongoose = require('mongoose');

const externalAPISchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    maxlength: 100,
  },
  baseUrl: {
    type: String,
    required: true,
    match: /^https?:\/\/.+/,
  },
  endpointPath: {
    type: String,
    required: true,
  },
}, { timestamps: true });

module.exports = mongoose.model('ExternalAPI', externalAPISchema);
