"""Application entry point for the TCG Collection API.

This module creates the :class:`FastAPI` application instance and registers
all available routers.  During the initial scaffold of this repository the
file accidentally instantiated the application twice which meant that only
the routes registered after the second instantiation were exposed.  The
wishlist endpoints used in the tests were therefore missing.  The revised
implementation below ensures the app is created a single time and that all
routers are included.
"""

from fastapi import FastAPI
from routes import cards, sets, wishlist


# Create the FastAPI app and register all routers.
app = FastAPI(title="TCG Collection API")
app.include_router(wishlist.router)
app.include_router(sets.router)
app.include_router(cards.router)


__all__ = ["app"]
