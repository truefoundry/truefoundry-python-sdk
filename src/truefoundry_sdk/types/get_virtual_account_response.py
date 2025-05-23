# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .virtual_account import VirtualAccount


class GetVirtualAccountResponse(UniversalBaseModel):
    data: VirtualAccount = pydantic.Field()
    """
    Virtual Account
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Virtual Account token (present only when creating a virtual account)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
