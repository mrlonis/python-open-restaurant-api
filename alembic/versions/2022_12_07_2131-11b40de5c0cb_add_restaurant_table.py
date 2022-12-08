"""Add Restaurant Table

Revision ID: 11b40de5c0cb
Revises:
Create Date: 2022-12-07 21:31:23.559324

"""
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
from alembic import op

# revision identifiers, used by Alembic.
revision = "11b40de5c0cb"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "restaurant",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("weekday", sa.Integer(), nullable=False),
        sa.Column("open", sa.Time(), nullable=False),
        sa.Column("close", sa.Time(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_restaurant_id"), "restaurant", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_restaurant_id"), table_name="restaurant")
    op.drop_table("restaurant")
    # ### end Alembic commands ###
