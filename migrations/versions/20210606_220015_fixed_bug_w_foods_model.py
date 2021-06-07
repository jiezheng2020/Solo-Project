"""fixed bug w foods model

Revision ID: ab62ad2a05ad
Revises: 8e11f70afc78
Create Date: 2021-06-06 22:00:15.813569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab62ad2a05ad'
down_revision = '8e11f70afc78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('foods', sa.Column('serving', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('foods', 'serving')
    # ### end Alembic commands ###
