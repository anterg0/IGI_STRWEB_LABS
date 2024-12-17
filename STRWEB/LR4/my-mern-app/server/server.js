const express = require('express');
const connectToDatabase = require('./db');
const dotenv = require('dotenv');
const cors = require('cors');
const session = require('express-session');
dotenv.config();
require('./config/passport-setup');

const app = express();
const PORT = process.env.PORT || 5000;

connectToDatabase();

app.use(cors());

app.use(express.json());

app.use(session({
    secret: 'abobius', 
    resave: false,             
    saveUninitialized: false, 
    cookie: { secure: false }  
}));

app.use('/api', require('./routes/userRoutes'));

app.use('/api/auth', require('./routes/authRoutes'));

app.use('/api/products', require('./routes/productRoutes'));

app.use('/api/news', require('./routes/newsRoutes'));

app.use('/api/manufacturers', require('./routes/manufacturerRoutes'));

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
