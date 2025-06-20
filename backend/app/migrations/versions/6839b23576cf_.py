"""empty message

Revision ID: 6839b23576cf
Revises:
Create Date: 2025-06-18 17:10:45.560341

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6839b23576cf"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created_at", sa.Date(), nullable=True),
        sa.Column("is_public", sa.Boolean(), nullable=False),
        sa.Column("status", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("title"),
    )
    op.create_index(op.f("ix_projects_id"), "projects", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_projects_id"), table_name="projects")
    op.drop_table("projects")
    # ### end Alembic commands ###
