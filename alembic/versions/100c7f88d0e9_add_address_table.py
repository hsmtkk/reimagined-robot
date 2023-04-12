"""add address table

Revision ID: 100c7f88d0e9
Revises: 
Create Date: 2023-04-12 19:32:49.012040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '100c7f88d0e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address1', sa.String(), nullable=True),
    sa.Column('address2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('postalcode', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'addresses', ['address_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'address_id')
    op.drop_column('users', 'phone_number')
    op.drop_table('addresses')
    # ### end Alembic commands ###
