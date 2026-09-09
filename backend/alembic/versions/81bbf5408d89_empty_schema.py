"""Empty schema.

Domain tables arrive with their modules. This revision exists so
``alembic upgrade head`` is a real command from the first models chapter.

Revision ID: 81bbf5408d89
Revises:
Create Date: 2026-09-10 01:44:54.891355

"""

from typing import Sequence, Union

revision: str = "81bbf5408d89"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
