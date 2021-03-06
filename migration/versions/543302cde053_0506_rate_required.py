"""0506_rate_required

Revision ID: 543302cde053
Revises: 52c3437b2916
Create Date: 2020-08-06 23:21:25.856641

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes


# revision identifiers, used by Alembic.
revision = '543302cde053'
down_revision = '52c3437b2916'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('rating_required', sa.BOOLEAN(), server_default='1', nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'rating_required')
    # ### end Alembic commands ###
