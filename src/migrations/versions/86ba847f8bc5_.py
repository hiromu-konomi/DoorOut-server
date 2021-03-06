"""empty message

Revision ID: 86ba847f8bc5
Revises: fd5ccf0e8a2c
Create Date: 2021-03-24 14:55:41.412916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86ba847f8bc5'
down_revision = 'fd5ccf0e8a2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'likes', ['post_id', 'user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'likes', type_='unique')
    # ### end Alembic commands ###
