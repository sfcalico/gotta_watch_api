"""create-user_listings

Revision ID: 54e5d2666b36
Revises: 2323d1c70a7f
Create Date: 2022-01-10 11:31:11.223253

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54e5d2666b36'
down_revision = '2323d1c70a7f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user_listings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('listing_id', sa.Integer)
    )


def downgrade():
    op.drop_table('user_listings')
