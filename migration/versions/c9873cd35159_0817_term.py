"""0817_term

Revision ID: c9873cd35159
Revises: 11568915fcb2
Create Date: 2020-08-17 20:16:16.829133

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c9873cd35159'
down_revision = '11568915fcb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('terms', sa.Column('symbol', mysql.CHAR(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('terms', 'symbol')
    # ### end Alembic commands ###
