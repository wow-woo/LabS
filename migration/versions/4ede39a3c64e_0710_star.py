"""0710_star

Revision ID: 4ede39a3c64e
Revises: f311fef3e4c5
Create Date: 2020-07-10 18:25:26.995294

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes


# revision identifiers, used by Alembic.
revision = '4ede39a3c64e'
down_revision = 'f311fef3e4c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hearts', sa.Column('match_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'hearts', 'matches', ['match_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'hearts', type_='foreignkey')
    op.drop_column('hearts', 'match_id')
    # ### end Alembic commands ###
