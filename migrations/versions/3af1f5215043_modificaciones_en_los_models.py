"""Modificaciones en los models

Revision ID: 3af1f5215043
Revises: e666200ddbb8
Create Date: 2024-09-15 22:05:16.908590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3af1f5215043'
down_revision = 'e666200ddbb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('features', schema=None) as batch_op:
        batch_op.alter_column('movie_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('room_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('features', schema=None) as batch_op:
        batch_op.alter_column('room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('movie_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
