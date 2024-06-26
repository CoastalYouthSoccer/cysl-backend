"""initial creation

Revision ID: c3e031976b6a
Revises: 
Create Date: 2024-05-11 17:08:30.676550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'c3e031976b6a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('misconduct',
    sa.Column('game_dt', sa.DateTime(), nullable=False),
    sa.Column('venue', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('age_group', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('gender', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('home_team', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('home_team_coach', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('home_score', sa.Integer(), nullable=False),
    sa.Column('away_team', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('away_team_coach', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('away_score', sa.Integer(), nullable=False),
    sa.Column('reported_by', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('referee', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('ar1', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('ar2', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('code', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('offender_name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('coach_player', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('player_nbr', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('offender_team', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('minute', sa.Integer(), nullable=False),
    sa.Column('offense', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('season',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('start_dt', sa.Date(), nullable=False),
    sa.Column('end_dt', sa.Date(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('season')
    op.drop_table('misconduct')
    # ### end Alembic commands ###
