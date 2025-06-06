# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ApplicationsListRequestLifecycleStage(str, enum.Enum):
    ACTIVE = "active"
    DELETING = "deleting"
    DELETION_FAILED = "deletion_failed"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
        deletion_failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ApplicationsListRequestLifecycleStage.ACTIVE:
            return active()
        if self is ApplicationsListRequestLifecycleStage.DELETING:
            return deleting()
        if self is ApplicationsListRequestLifecycleStage.DELETION_FAILED:
            return deletion_failed()
