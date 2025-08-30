// Basic Card model
class Card {
  constructor({ id, name, set, rarity }) {
    this.id = id;
    this.name = name;
    this.set = set;
    this.rarity = rarity;
  }
}

module.exports = Card;
