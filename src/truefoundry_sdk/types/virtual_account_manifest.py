# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permissions import Permissions


class VirtualAccountManifest(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    +label=Name
    +sort=1
    +message=3 to 25 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    +usage=Virtual Account Name
    """

    type: typing.Literal["virtual-account"] = pydantic.Field(default="virtual-account")
    """
    +value=virtual-account
    """

    expiration_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Expiration Date (UTC)
    +sort=2
    +message=Expiration date of the virtual account
    +usage=Expiration Date of the Virtual Account (should be in the format yyyy-mm-dd)
    +uiType=DatePicker
    """

    permissions: typing.List[Permissions] = pydantic.Field()
    """
    +label=Permissions
    +sort=3
    +uiType=ServiceAccountPermissions
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
