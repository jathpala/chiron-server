"""Create meta table

Revision ID: dcac393e8921
Revises:
Create Date: 2024-07-21 02:16:12.838229
"""
# pylint: disable=wrong-import-order
# pylint: disable=missing-function-docstring
# pylint: disable=no-member

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "dcac393e8921"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    meta_tbl = op.create_table(
        "meta",
        sa.Column("key", sa.String, primary_key=True),
        sa.Column("value", sa.String, nullable=False)
    )
    op.bulk_insert(
        meta_tbl,
        [
            {"key": "schema", "value": "chiron_server"},
            {"key": "version", "value": "1.0"}
        ]
    )

def downgrade() -> None:
    op.drop_table("meta")
