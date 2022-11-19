"""empty message

Revision ID: 24bdba4f13f8
Revises: f2520a7360c9
Create Date: 2022-11-11 01:04:24.475541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24bdba4f13f8'
down_revision = 'f2520a7360c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###