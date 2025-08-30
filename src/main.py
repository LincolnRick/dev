from fastapi import FastAPI
from .routes import sets, cards

app = FastAPI(title="TCG Collection API")

app.include_router(sets.router)
app.include_router(cards.router)
