"""create prompts table

Revision ID: 08629079c6bd
Revises: 
Create Date: 2023-12-28 14:30:52.644558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08629079c6bd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    create table prompts (
               id bigserial primary key,
               name text,
               email text
    )
    """)


def downgrade():
    op.execute("drop table prompts;")
