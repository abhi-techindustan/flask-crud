"""empty message

Revision ID: 7a3a1667c5f5
Revises: 08a503e01977
Create Date: 2021-03-18 19:11:24.512177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a3a1667c5f5'
down_revision = '08a503e01977'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('signup', sa.Column('otp', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('signup', 'otp')
    # ### end Alembic commands ###
