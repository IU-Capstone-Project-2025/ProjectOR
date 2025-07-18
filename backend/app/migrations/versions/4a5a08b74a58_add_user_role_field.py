"""add user role field

Revision ID: 4a5a08b74a58
Revises: d48f4d45faf0
Create Date: 2025-07-02 19:41:06.985166

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "4a5a08b74a58"
down_revision: Union[str, Sequence[str], None] = "d48f4d45faf0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    user_role = postgresql.ENUM(
        "VIEWER",
        "FOUNDER",
        "DEVELOPER",
        "INVESTOR",
        name="user_role_enum",
    )
    user_role.create(op.get_bind(), checkfirst=True)
    op.add_column("users", sa.Column("level", sa.Integer(), nullable=True))
    op.add_column(
        "users",
        sa.Column(
            "role",
            user_role,
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "role")
    op.drop_column("users", "level")
    # ### end Alembic commands ###
