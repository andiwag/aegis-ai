"""Import domain models so Alembic sees Base.metadata.

Identity and later modules add imports here when they grow tables.
"""

from aegis.db import Base

__all__ = ["Base"]
