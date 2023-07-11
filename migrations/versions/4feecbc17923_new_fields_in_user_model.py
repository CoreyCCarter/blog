"""new fields in user model

Revision ID: 4feecbc17923
Revises: fe1c69ef41dd
Create Date: 2023-07-03 04:38:38.169694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4feecbc17923'
down_revision = 'fe1c69ef41dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=1000), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
