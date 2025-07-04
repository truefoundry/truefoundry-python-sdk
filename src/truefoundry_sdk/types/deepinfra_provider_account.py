# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collaborator import Collaborator
from .deepinfra_integrations import DeepinfraIntegrations
from .deepinfra_key_auth import DeepinfraKeyAuth


class DeepinfraProviderAccount(UniversalBaseModel):
    """
    +label=DeepInfra Provider Account
    +icon=deepinfra
    """

    type: typing.Literal["provider-account/deepinfra"] = pydantic.Field(default="provider-account/deepinfra")
    """
    +value=provider-account/deepinfra
    """

    name: str = pydantic.Field()
    """
    +label=Name
    +sort=100
    +usage=The name of the DeepInfra provider account
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    +uiProps={"disableEdit":true}
    """

    auth_data: DeepinfraKeyAuth
    integrations: typing.Optional[typing.List[DeepinfraIntegrations]] = pydantic.Field(default=None)
    """
    +label=Integrations
    +sort=300
    +usage=List of integrations that are associated with the DeepInfra provider account
    +uiType=IntegrationsGroup
    """

    collaborators: typing.Optional[typing.List[Collaborator]] = pydantic.Field(default=None)
    """
    +label=Collaborators
    +sort=400
    +usage=List of users who have access to this provider account
    +uiType=Collaborators
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
