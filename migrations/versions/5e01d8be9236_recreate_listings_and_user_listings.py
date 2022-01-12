"""recreate-listings-and-user_listings

Revision ID: 5e01d8be9236
Revises: 54e5d2666b36
Create Date: 2022-01-11 13:23:51.235199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e01d8be9236'
down_revision = '54e5d2666b36'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    op.drop_table('listings')
    op.drop_table('user_listings')
