"""edit comments column

Revision ID: b5973c65dc53
Revises: dcf5fd8d8307
Create Date: 2021-03-18 12:10:39.122957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b5973c65dc53'
down_revision = 'dcf5fd8d8307'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('timestamp', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'timestamp')
    # ### end Alembic commands ###