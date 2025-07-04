# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .azure_foundry_model_v2 import AzureFoundryModelV2
from .collaborator import Collaborator


class AzureFoundryProviderAccount(UniversalBaseModel):
    """
    +label=Azure Foundry Provider Account
    +icon=azure
    """

    type: typing.Literal["provider-account/azure-foundry"] = pydantic.Field(default="provider-account/azure-foundry")
    """
    +value=provider-account/azure-foundry
    """

    name: str = pydantic.Field()
    """
    +label=Name
    +sort=100
    +usage=The name of the Azure Foundry provider account
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    +uiProps={"disableEdit":true}
    """

    integrations: typing.List[AzureFoundryModelV2] = pydantic.Field()
    """
    +label=Integrations
    +sort=200
    +usage=List of integrations that are associated with the Azure Foundry provider account
    +uiType=IntegrationsGroup
    """

    collaborators: typing.Optional[typing.List[Collaborator]] = pydantic.Field(default=None)
    """
    +label=Collaborators
    +sort=300
    +usage=List of users who have access to this provider account
    +uiType=Collaborators
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
