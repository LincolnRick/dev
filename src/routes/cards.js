const express = require('express');
const router = express.Router();
const cardService = require('../services/cardService');

// Get all cards in collection
router.get('/', (req, res) => {
  const cards = cardService.getAllCards();
  res.json(cards);
});

// Add a card to collection
router.post('/', (req, res) => {
  const card = cardService.addCard(req.body);
  res.status(201).json(card);
});

module.exports = router;
