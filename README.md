# TCG Collector API

API para gerenciar sets, cartas, coleção pessoal e lista de desejos (wishlist) de cartas TCG.

## Requisitos
- Node.js \>= 18
- npm

## Instalação
1. Clone o repositório.
2. Instale as dependências:
   ```bash
   npm install
   ```

## Execução
Inicie o servidor em modo de desenvolvimento:
```bash
npm run dev
```

## Endpoints Básicos
### Sets
- `GET /sets` – lista todos os sets disponíveis.
- `GET /sets/:id` – detalhes de um set específico.

### Cartas
- `GET /cards` – lista todas as cartas disponíveis.
- `GET /cards/:id` – detalhes de uma carta específica.

### Coleção
- `GET /collection` – lista as cartas da coleção do usuário.
- `POST /collection` – adiciona uma carta à coleção.
- `DELETE /collection/:id` – remove uma carta da coleção.

### Wishlist
- `GET /wishlist` – lista as cartas na lista de desejos.
- `POST /wishlist` – adiciona uma carta à wishlist.
- `DELETE /wishlist/:id` – remove uma carta da wishlist.

