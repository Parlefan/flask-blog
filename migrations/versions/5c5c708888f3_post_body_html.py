"""Post body_html

Revision ID: 5c5c708888f3
Revises: 3ee4d9972db5
Create Date: 2016-10-10 17:15:54.337519

"""

# revision identifiers, used by Alembic.
revision = '5c5c708888f3'
down_revision = '3ee4d9972db5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###
