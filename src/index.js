const express = require('express');

const app = express();
app.use(express.json());

// Root endpoint
app.get('/', (req, res) => {
  res.json({ message: 'TCG Collection API' });
});

// Cards routes
const cardsRouter = require('./routes/cards');
app.use('/cards', cardsRouter);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
