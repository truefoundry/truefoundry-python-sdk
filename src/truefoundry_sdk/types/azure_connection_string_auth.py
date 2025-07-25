# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AzureConnectionStringAuth(UniversalBaseModel):
    """
    +label=Azure Connection String
    """

    type: typing.Literal["connection-string"] = pydantic.Field(default="connection-string")
    """
    +value=connection-string
    """

    connection_string: str = pydantic.Field()
    """
    +label=Connection String
    +usage=The connection string for the Azure managed identity.
    +sort=100
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
