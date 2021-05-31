"""empty message

Revision ID: c42839c4e729
Revises: 0625d55d47de
Create Date: 2021-03-23 11:28:31.704850

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c42839c4e729'
down_revision = '0625d55d47de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('child_comments', 'parent_comment_id',
               existing_type=mysql.CHAR(collation='utf8mb4_unicode_ci', length=32),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('child_comments', 'parent_comment_id',
               existing_type=mysql.CHAR(collation='utf8mb4_unicode_ci', length=32),
               nullable=True)
    # ### end Alembic commands ###