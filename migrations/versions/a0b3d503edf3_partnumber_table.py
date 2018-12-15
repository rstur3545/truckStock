"""PartNumber table

Revision ID: a0b3d503edf3
Revises: 
Create Date: 2018-10-12 16:17:18.948832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a0b3d503edf3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('partnum',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('partnumber', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=10), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_partnum_partnumber'), 'partnum', ['partnumber'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_partnum_partnumber'), table_name='partnum')
    op.drop_table('partnum')
    # ### end Alembic commands ###
