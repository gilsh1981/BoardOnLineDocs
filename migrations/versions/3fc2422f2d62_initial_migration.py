"""Initial migration.

Revision ID: 3fc2422f2d62
Revises: b74e46d19d82
Create Date: 2024-05-30 07:51:43.244576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fc2422f2d62'
down_revision = 'b74e46d19d82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=150), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
