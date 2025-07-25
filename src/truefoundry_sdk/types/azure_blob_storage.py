# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .azure_connection_string_auth import AzureConnectionStringAuth


class AzureBlobStorage(UniversalBaseModel):
    """
    +icon=azure-blob
    +label=Azure ABS
    """

    type: typing.Literal["integration/blob-storage/azure/blob"] = pydantic.Field(
        default="integration/blob-storage/azure/blob"
    )
    """
    +value=integration/blob-storage/azure/blob
    """

    name: str = pydantic.Field()
    """
    +label=Display Name
    +usage=The name of the integration that will be displayed in the TrueFoundry UI.
    +sort=100
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    """

    storage_root: str = pydantic.Field()
    """
    +label=Storage Root
    +usage=The root path of the storage.
    +sort=200
    """

    auth_data: typing.Optional[AzureConnectionStringAuth] = None
    authorized_subjects: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    +label=Access Control
    +usage=List of subjects that are authorized to access this integration. List of user fqn in format <user_type>:<username>.
    +sort=600
    +uiType=AuthorizedSubjects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
