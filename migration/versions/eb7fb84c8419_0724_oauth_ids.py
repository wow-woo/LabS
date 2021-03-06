"""0724_oauth_ids

Revision ID: eb7fb84c8419
Revises: 29e170f95e52
Create Date: 2020-07-24 23:58:26.734816

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes


# revision identifiers, used by Alembic.
revision = 'eb7fb84c8419'
down_revision = '29e170f95e52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('oauth_apple_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('oauth_google_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('oauth_kakao_id', sa.Integer(), nullable=True))
    op.add_column('users', sa.Column('oauth_naver_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'oauth_naver', ['oauth_naver_id'], ['id'])
    op.create_foreign_key(None, 'users', 'oauth_google', ['oauth_google_id'], ['id'])
    op.create_foreign_key(None, 'users', 'oauth_apple', ['oauth_apple_id'], ['id'])
    op.create_foreign_key(None, 'users', 'oauth_kakao', ['oauth_kakao_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'oauth_naver_id')
    op.drop_column('users', 'oauth_kakao_id')
    op.drop_column('users', 'oauth_google_id')
    op.drop_column('users', 'oauth_apple_id')
    # ### end Alembic commands ###
