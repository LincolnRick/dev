const cards = [];

function getAllCards() {
  return cards;
}

function addCard(card) {
  const newCard = { id: Date.now().toString(), ...card };
  cards.push(newCard);
  return newCard;
}

module.exports = { getAllCards, addCard };
