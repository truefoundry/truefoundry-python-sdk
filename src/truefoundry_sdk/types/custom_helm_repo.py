# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_basic_auth import CustomBasicAuth


class CustomHelmRepo(UniversalBaseModel):
    """
    +label=Custom Helm Repo
    +icon=puzzle-piece
    """

    type: typing.Literal["integration/helm-repo/custom"] = pydantic.Field(default="integration/helm-repo/custom")
    """
    +value=integration/helm-repo/custom
    """

    name: str = pydantic.Field()
    """
    +label=Display Name
    +usage=The name of the integration that will be displayed in the TrueFoundry UI.
    +sort=100
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    """

    repo_url: str = pydantic.Field()
    """
    +label=Helm Repo URL
    +usage=The URL of the Helm Repo.
    +sort=200
    """

    auth_data: CustomBasicAuth
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
