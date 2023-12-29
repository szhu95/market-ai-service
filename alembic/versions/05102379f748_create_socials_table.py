"""create socials table

Revision ID: 05102379f748
Revises: 08629079c6bd
Create Date: 2023-12-28 16:50:47.924160

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05102379f748'
down_revision: Union[str, None] = '08629079c6bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("""
    create table socials (
               id bigserial primary key,
               name text,
               post text
    )
    """)


def downgrade():
    op.execute("drop table socials;")
