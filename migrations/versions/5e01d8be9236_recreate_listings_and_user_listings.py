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
    op.create_table(
        'listings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String),
        sa.Column('year', sa.String),
        sa.Column('type', sa.String),
        sa.Column('poster', sa.String)
    )
    op.create_table(
        'user_listings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer),
        sa.Column('listing_id', sa.Integer)
    )


def downgrade():
    op.drop_table('listings')
    op.drop_table('user_listings')
