"""empty message

Revision ID: 0ddc755a4418
Revises: 9c86c93f41b4
Create Date: 2021-07-07 17:57:27.905177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ddc755a4418'
down_revision = '9c86c93f41b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather_data_cities', sa.Column('city_id', sa.Integer(), nullable=True))
    op.add_column('weather_data_cities', sa.Column('temp', sa.Integer(), nullable=True))
    op.add_column('weather_data_cities', sa.Column('wind_speed', sa.Float(), nullable=True))
    op.add_column('weather_data_cities', sa.Column('pressure', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weather_data_cities', 'pressure')
    op.drop_column('weather_data_cities', 'wind_speed')
    op.drop_column('weather_data_cities', 'temp')
    op.drop_column('weather_data_cities', 'city_id')
    # ### end Alembic commands ###
