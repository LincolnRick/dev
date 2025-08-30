from fastapi import FastAPI
from routes import wishlist

app = FastAPI()
app.include_router(wishlist.router)
