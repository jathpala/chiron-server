"""Create demographics table

Revision ID: fed617684e34
Revises: dcac393e8921
Create Date: 2024-07-21 23:06:14.183143

"""

# pylint: disable=wrong-import-order
# pylint: disable=missing-function-docstring
# pylint: disable=no-member
# pylint: disable=singleton-comparison

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fed617684e34"
down_revision: Union[str, None] = "dcac393e8921"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "demographics",
        sa.Column("mrn", sa.String, primary_key=True),
        sa.Column("firstname", sa.String, nullable=False),
        sa.Column("middlenames", sa.String, server_default=None),
        sa.Column("lastname", sa.String, server_default=None),
        sa.Column("onlyname", sa.Boolean, server_default=sa.sql.expression.false()),
        sa.Column("dob", sa.String),
        sa.Column("sex", sa.String)
    )

    with op.batch_alter_table("demographics") as batch_op:
        batch_op.create_check_constraint(
            "onlyname_constraint",
            sa.or_(
                sa.and_(
                    sa.column("onlyname") == True,
                    sa.column("lastname") == None
                ),
                sa.and_(
                    sa.column("onlyname") == False,
                    sa.column("lastname") != None
                )
            )
        )
        batch_op.create_check_constraint(
            "sex_enum_constraint",
            sa.column("sex").in_(
                ["male", "female", "other"]
            )
        )


def downgrade() -> None:
    op.drop_table("demographics")
