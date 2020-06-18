"""0618_2_heart

Revision ID: f2abe176ea17
Revises: f185b8b43637
Create Date: 2020-06-18 22:03:35.797028

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f2abe176ea17'
down_revision = 'f185b8b43637'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heart_recharges',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('google_purchase_token', mysql.CHAR(length=100), nullable=True),
    sa.Column('google_order_id', mysql.CHAR(length=100), nullable=True),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('type', mysql.CHAR(length=20), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('symbol', mysql.CHAR(length=10), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_symbol'), 'items', ['symbol'], unique=True)
    op.create_table('stars',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', mysql.TEXT(), nullable=True),
    sa.Column('rate', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('hearts', sa.Column('from_user_id', sa.Integer(), nullable=True))
    op.add_column('hearts', sa.Column('to_user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_hearts_from_user_id'), 'hearts', ['from_user_id'], unique=False)
    op.create_index(op.f('ix_hearts_to_user_id'), 'hearts', ['to_user_id'], unique=False)
    op.create_foreign_key(None, 'hearts', 'users', ['from_user_id'], ['id'])
    op.create_foreign_key(None, 'hearts', 'users', ['to_user_id'], ['id'])
    op.drop_column('hearts', 'to_user')
    op.drop_column('hearts', 'hi')
    op.drop_column('hearts', 'from_user')
    op.add_column('user_point_transactions', sa.Column('heart_id', sa.Integer(), nullable=True))
    op.add_column('user_point_transactions', sa.Column('heart_recharge_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'user_point_transactions', 'heart_recharges', ['heart_recharge_id'], ['id'])
    op.create_foreign_key(None, 'user_point_transactions', 'hearts', ['heart_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_point_transactions', type_='foreignkey')
    op.drop_constraint(None, 'user_point_transactions', type_='foreignkey')
    op.drop_column('user_point_transactions', 'heart_recharge_id')
    op.drop_column('user_point_transactions', 'heart_id')
    op.add_column('hearts', sa.Column('from_user', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('hearts', sa.Column('hi', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
    op.add_column('hearts', sa.Column('to_user', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'hearts', type_='foreignkey')
    op.drop_constraint(None, 'hearts', type_='foreignkey')
    op.drop_index(op.f('ix_hearts_to_user_id'), table_name='hearts')
    op.drop_index(op.f('ix_hearts_from_user_id'), table_name='hearts')
    op.drop_column('hearts', 'to_user_id')
    op.drop_column('hearts', 'from_user_id')
    op.drop_table('stars')
    op.drop_index(op.f('ix_items_symbol'), table_name='items')
    op.drop_table('items')
    op.drop_table('heart_recharges')
    # ### end Alembic commands ###
