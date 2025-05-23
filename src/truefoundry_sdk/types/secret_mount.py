# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SecretMount(UniversalBaseModel):
    type: typing.Literal["secret"] = pydantic.Field(default="secret")
    """
    +value=secret
    """

    mount_path: str = pydantic.Field()
    """
    +label=File path
    +usage=Absolute file path where the file will be created.
    +message=Please enter a valid file path
    """

    secret_fqn: str = pydantic.Field()
    """
    +label=Secret
    +usage=The TrueFoundry secret whose value will be the file content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
