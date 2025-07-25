# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gcp_key_file_auth import GcpKeyFileAuth


class GcpGcs(UniversalBaseModel):
    """
    +icon=gcp-gcs
    +label=GCP GCS
    """

    type: typing.Literal["integration/blob-storage/gcp/gcs"] = pydantic.Field(
        default="integration/blob-storage/gcp/gcs"
    )
    """
    +value=integration/blob-storage/gcp/gcs
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

    auth_data: typing.Optional[GcpKeyFileAuth] = None
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
