"""empty message

Revision ID: 830e8ee32cbf
Revises: c7268fc25b87
Create Date: 2017-11-12 00:01:29.053438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '830e8ee32cbf'
down_revision = 'c7268fc25b87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_tags',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_tags')
    # ### end Alembic commands ###
