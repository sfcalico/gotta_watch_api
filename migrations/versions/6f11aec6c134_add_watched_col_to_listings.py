"""add-watched-col-to-listings

Revision ID: 6f11aec6c134
Revises: 3b98e928a4ad
Create Date: 2022-01-11 16:41:54.753325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f11aec6c134'
down_revision = '3b98e928a4ad'
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
        sa.Column('user_id', sa.Integer),
        sa.Column('watched', sa.Boolean)
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
