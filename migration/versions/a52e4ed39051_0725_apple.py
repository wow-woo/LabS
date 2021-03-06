"""0725_apple

Revision ID: a52e4ed39051
Revises: eb7fb84c8419
Create Date: 2020-07-25 21:47:22.158092

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a52e4ed39051'
down_revision = 'eb7fb84c8419'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_ibfk_4', 'users', type_='foreignkey')
    op.drop_column('users', 'oauth_apple_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('oauth_apple_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_ibfk_4', 'users', 'oauth_apple', ['oauth_apple_id'], ['id'])
    # ### end Alembic commands ###
