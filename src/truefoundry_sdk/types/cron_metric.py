# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CronMetric(UniversalBaseModel):
    type: typing.Literal["cron"] = pydantic.Field(default="cron")
    """
    +value=cron
    """

    desired_replicas: typing.Optional[int] = pydantic.Field(default=None)
    """
    +label=Desired Replicas
    +usage=Desired number of replicas during the given interval. Default value is max_replicas.
    """

    start: str = pydantic.Field()
    """
    +label=Start Schedule
    +docs=Cron expression indicating the start of the cron schedule.
    +usage=Cron expression indicating the start of the cron schedule.
    ```
    * * * * *
    | | | | |
    | | | | |___ day of week (0-6) (Sunday is 0)
    | | | |_____ month (1-12)
    | | |_______ day of month (1-31)
    | |_________ hour (0-23)
    |___________ minute (0-59)
    ```
    """

    end: str = pydantic.Field()
    """
    +label=End Schedule
    +docs=Cron expression indicating the end of the cron schedule.
    +usage=Cron expression indicating the end of the cron schedule.
    ```
    * * * * *
    | | | | |
    | | | | |___ day of week (0-6) (Sunday is 0)
    | | | |_____ month (1-12)
    | | |_______ day of month (1-31)
    | |_________ hour (0-23)
    |___________ minute (0-59)
    ```
    """

    timezone: str = pydantic.Field(default="UTC")
    """
    +usage=Timezone against which the cron schedule will be calculated, e.g. "Asia/Tokyo". Default is machine's local time.
    https://docs.truefoundry.com/docs/list-of-supported-timezones
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
