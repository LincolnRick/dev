const express = require('express');
const path = require('path');

const app = express();
app.use(express.json());

// Serve static files for the front-end layout
const publicDir = path.join(__dirname, '..', 'public');
app.use(express.static(publicDir));

// Root endpoint serves the layout
app.get('/', (req, res) => {
  res.sendFile(path.join(publicDir, 'index.html'));
});

// Cards routes
const cardsRouter = require('./routes/cards');
app.use('/cards', cardsRouter);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
