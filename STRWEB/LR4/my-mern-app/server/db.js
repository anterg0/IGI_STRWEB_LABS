const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

const uri = process.env.MONGO_URI;

const connectToDatabase = async () => {
    try {
        console.log('Trying to connect to ', uri);
        await mongoose.connect(process.env.MONGO_URI, {
            dbName: 'react-project',
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        
        console.log('Connected to MongoDB with Mongoose');
    } catch (error) {
        console.error('Error connecting to MongoDB:', error.message);
        process.exit(1);
    }
};

module.exports = connectToDatabase;