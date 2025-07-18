"""change date to datetime format

Revision ID: 6e2af57b2c75
Revises: 843428e10d39
Create Date: 2025-07-09 16:56:58.620295

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6e2af57b2c75"
down_revision: Union[str, Sequence[str], None] = "843428e10d39"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "applications",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=True,
    )
    op.alter_column(
        "project_members",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=True,
    )
    op.alter_column(
        "projects",
        "created_at",
        existing_type=sa.DATE(),
        type_=sa.DateTime(),
        existing_nullable=True,
    )
    op.alter_column("projects", "is_public", existing_type=sa.BOOLEAN(), nullable=True)
    op.alter_column("projects", "ceo_id", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "projects", "is_opensource", existing_type=sa.BOOLEAN(), nullable=True
    )
    op.alter_column("projects", "is_dead", existing_type=sa.BOOLEAN(), nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("projects", "is_dead", existing_type=sa.BOOLEAN(), nullable=False)
    op.alter_column(
        "projects", "is_opensource", existing_type=sa.BOOLEAN(), nullable=False
    )
    op.alter_column("projects", "ceo_id", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column("projects", "is_public", existing_type=sa.BOOLEAN(), nullable=False)
    op.alter_column(
        "projects",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=True,
    )
    op.alter_column(
        "project_members",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=True,
    )
    op.alter_column(
        "applications",
        "created_at",
        existing_type=sa.DateTime(),
        type_=sa.DATE(),
        existing_nullable=True,
    )
    # ### end Alembic commands ###
