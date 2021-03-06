"""0514_mbti_result

Revision ID: 56ce85771cf2
Revises: f454cdf86693
Create Date: 2020-05-14 22:23:18.059290

"""
from alembic import op
import sqlalchemy as sa
from libs.database.types import LaboratoryTypes
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '56ce85771cf2'
down_revision = 'f454cdf86693'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mbti_results',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('raw', mysql.JSON(), nullable=True),
    sa.Column('result_mbti', mysql.CHAR(length=10), nullable=True),
    sa.Column('animal_id', sa.Integer(), nullable=True),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['animal_id'], ['animals.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('mbti_questions', sa.Column('trait', mysql.CHAR(length=5), nullable=True))
    op.drop_column('mbti_questions', 'determinant')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mbti_questions', sa.Column('determinant', mysql.CHAR(length=5), nullable=True))
    op.drop_column('mbti_questions', 'trait')
    op.drop_table('mbti_results')
    # ### end Alembic commands ###
