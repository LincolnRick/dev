"""Database model base class.

The project makes use of SQLAlchemy for persisting some models, but the test
environment used in this kata does not install SQLAlchemy.  Importing
``models`` therefore previously failed during module initialisation.  To keep
the models package lightweight and to allow the Pydantic models (such as the
``WishlistItem``) to be imported without SQLAlchemy being present, we attempt
to import :func:`declarative_base` and fall back to a simple stub when the
dependency is missing.
"""

try:  # pragma: no cover - optional dependency handling
    from sqlalchemy.orm import declarative_base
    Base = declarative_base()
except ModuleNotFoundError:  # SQLAlchemy not installed
    class Base:  # type: ignore[override]
        """Fallback base class used when SQLAlchemy is unavailable."""

