"""created models

Revision ID: f81346d2f387
Revises: ffdc0a98111c
Create Date: 2021-06-02 21:40:41.124922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f81346d2f387'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('exercises',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('cpm', sa.Integer(), nullable=False),
    sa.Column('exerciseType', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('calories', sa.Integer(), nullable=False),
    sa.Column('foodType', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('diaries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exerciseEntries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('exercise_id', sa.Integer(), nullable=False),
    sa.Column('diary_id', sa.Integer(), nullable=False),
    sa.Column('exerciseType', sa.String(length=20), nullable=False),
    sa.Column('totalCalories', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['diary_id'], ['diaries.id'], ),
    sa.ForeignKeyConstraint(['exercise_id'], ['exercises.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('foodEntries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('food_id', sa.Integer(), nullable=False),
    sa.Column('diary_id', sa.Integer(), nullable=False),
    sa.Column('mealType', sa.String(length=20), nullable=False),
    sa.Column('totalCalories', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['diary_id'], ['diaries.id'], ),
    sa.ForeignKeyConstraint(['food_id'], ['foods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('age', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('dailyGoal', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('gender', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('height', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('weight', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'weight')
    op.drop_column('users', 'height')
    op.drop_column('users', 'gender')
    op.drop_column('users', 'dailyGoal')
    op.drop_column('users', 'age')
    op.drop_table('foodEntries')
    op.drop_table('exerciseEntries')
    op.drop_table('diaries')
    op.drop_table('foods')
    op.drop_table('exercises')
    # ### end Alembic commands ###