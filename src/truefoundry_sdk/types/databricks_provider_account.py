# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collaborator import Collaborator
from .databricks_integrations import DatabricksIntegrations
from .databricks_provider_account_auth_data import DatabricksProviderAccountAuthData


class DatabricksProviderAccount(UniversalBaseModel):
    """
    +label=Databricks Provider Account
    +icon=databricks
    """

    type: typing.Literal["provider-account/databricks"] = pydantic.Field(default="provider-account/databricks")
    """
    +value=provider-account/databricks
    """

    name: str = pydantic.Field()
    """
    +label=Name
    +sort=100
    +usage=The name of the Databricks provider account
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    +uiProps={"disableEdit":true}
    """

    auth_data: DatabricksProviderAccountAuthData = pydantic.Field()
    """
    +label=Auth Data
    +sort=300
    +usage=Databricks authentication credentials
    """

    base_url: str = pydantic.Field()
    """
    +label=Base URL
    +sort=400
    +usage=The base URL of your Databricks workspace
    +message=Base URL must not be empty
    """

    integrations: typing.List[DatabricksIntegrations] = pydantic.Field()
    """
    +label=Integrations
    +sort=500
    +usage=List of integrations that are associated with the Databricks provider account
    +uiType=IntegrationsGroup
    """

    collaborators: typing.Optional[typing.List[Collaborator]] = pydantic.Field(default=None)
    """
    +label=Collaborators
    +sort=200
    +usage=List of users who have access to this provider account
    +uiType=Collaborators
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
