"""0801_acquaintance_shy

Revision ID: 52c3437b2916
Revises: a52e4ed39051
Create Date: 2020-08-01 14:09:10.588302

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '52c3437b2916'
down_revision = 'a52e4ed39051'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('acquaintance', mysql.JSON(), nullable=True))
    op.add_column('users', sa.Column('acquaintance_shy', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'acquaintance_shy')
    op.drop_column('users', 'acquaintance')
    # ### end Alembic commands ###
