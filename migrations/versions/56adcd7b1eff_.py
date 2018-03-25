"""empty message

Revision ID: 56adcd7b1eff
Revises: 
Create Date: 2018-03-25 05:36:09.352332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56adcd7b1eff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('screen_name', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('followers_count', sa.Integer(), nullable=True),
    sa.Column('friends_count', sa.Integer(), nullable=True),
    sa.Column('listed_count', sa.Integer(), nullable=True),
    sa.Column('statuses_count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('status',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.Column('favorite_count', sa.Integer(), nullable=True),
    sa.Column('retweet_count', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('status')
    op.drop_table('user')
    # ### end Alembic commands ###