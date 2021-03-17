"""add comments table

Revision ID: dcf5fd8d8307
Revises: 9e9249efc2b6
Create Date: 2021-03-17 14:26:39.922719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dcf5fd8d8307'
down_revision = '9e9249efc2b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comment', sa.Text(), nullable=False))
    op.drop_column('comments', 'title')
    op.drop_column('comments', 'comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('comments', sa.TEXT(), autoincrement=False, nullable=False))
    op.add_column('comments', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('comments', 'comment')
    # ### end Alembic commands ###
