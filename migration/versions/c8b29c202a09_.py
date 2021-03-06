"""empty message

Revision ID: c8b29c202a09
Revises: c9e88e0e18ee
Create Date: 2020-04-29 21:51:28.884623

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes


# revision identifiers, used by Alembic.
revision = 'c8b29c202a09'
down_revision = 'c9e88e0e18ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hearts', sa.Column('hi', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hearts', 'hi')
    # ### end Alembic commands ###
