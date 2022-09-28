"""first

Revision ID: a4eab9a92595
Revises: 
Create Date: 2022-09-27 14:33:38.141048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4eab9a92595'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("sample",
    sa.Column("id",sa.Integer, nullable = False , primary_key = True),
    sa.Column("name",sa.String, nullable = False),
    sa.Column("time",sa.TIMESTAMP(timezone=False),server_default=sa.text('now()'))
    )
    pass


def downgrade() -> None:
    op.drop_table("sample")
    pass
