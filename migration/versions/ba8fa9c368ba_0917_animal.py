"""0917_animal

Revision ID: ba8fa9c368ba
Revises: 57ba692d8dca
Create Date: 2020-09-17 22:04:23.420141

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ba8fa9c368ba'
down_revision = '57ba692d8dca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('animals', sa.Column('title', mysql.TEXT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('animals', 'title')
    # ### end Alembic commands ###
