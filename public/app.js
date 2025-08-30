async function loadCards() {
  try {
    const res = await fetch('/cards');
    const data = await res.json();
    const grid = document.getElementById('card-grid');
    data.forEach(card => {
      const div = document.createElement('div');
      div.className = 'card';
      div.textContent = card.name || card.id;
      grid.appendChild(div);
    });
  } catch (err) {
    console.error('Erro ao carregar cartas', err);
  }
}

loadCards();
