"""create-users

Revision ID: c0de822d81ed
Revises: 
Create Date: 2022-01-10 11:17:45.454761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0de822d81ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('password', sa.String),
        sa.Column('bio', sa.String)
    )


def downgrade():
    op.drop_table('users')
