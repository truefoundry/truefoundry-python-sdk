# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GcpKeyFileAuth(UniversalBaseModel):
    """
    +label=GCP Key File Auth
    """

    type: typing.Literal["key-file"] = pydantic.Field(default="key-file")
    """
    +value=key-file
    """

    key_file_content: typing.Dict[str, typing.Optional[typing.Any]] = pydantic.Field()
    """
    +uiType=JsonInput
    +label=Key File Content
    +sort=100
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
