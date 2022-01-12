"""add-user_id-to-listings

Revision ID: 3b98e928a4ad
Revises: 5e01d8be9236
Create Date: 2022-01-11 14:26:33.140753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b98e928a4ad'
down_revision = '5e01d8be9236'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'listings',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String),
        sa.Column('year', sa.String),
        sa.Column('type', sa.String),
        sa.Column('poster', sa.String),
        sa.Column('user_id', sa.Integer)
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
