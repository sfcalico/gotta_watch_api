"""create-listings

Revision ID: 2323d1c70a7f
Revises: c0de822d81ed
Create Date: 2022-01-10 11:27:01.140782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2323d1c70a7f'
down_revision = 'c0de822d81ed'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_table('listings')
