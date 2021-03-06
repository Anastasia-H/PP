"""empty message

Revision ID: 50f4ad104198
Revises: 
Create Date: 2020-12-01 21:09:38.032141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50f4ad104198'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('user_ID', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('firstName', sa.String(), nullable=False),
    sa.Column('lastName', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('userStatus', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_ID')
    )
    op.create_table('Article',
    sa.Column('article_ID', sa.Integer(), nullable=False),
    sa.Column('user_ID', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('text', sa.String(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('complete', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_ID'], ['User.user_ID'], ),
    sa.PrimaryKeyConstraint('article_ID')
    )
    op.create_table('UsersArticles',
    sa.Column('version_id', sa.Integer(), nullable=False),
    sa.Column('user_ID', sa.Integer(), nullable=True),
    sa.Column('moderator_ID', sa.Integer(), nullable=True),
    sa.Column('article_ID', sa.Integer(), nullable=True),
    sa.Column('edited_text', sa.String(), nullable=True),
    sa.Column('edited_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['article_ID'], ['Article.article_ID'], ),
    sa.ForeignKeyConstraint(['user_ID'], ['User.user_ID'], ),
    sa.PrimaryKeyConstraint('version_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UsersArticles')
    op.drop_table('Article')
    op.drop_table('User')
    # ### end Alembic commands ###
