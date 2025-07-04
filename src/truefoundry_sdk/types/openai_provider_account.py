# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .collaborator import Collaborator
from .open_ai_integrations import OpenAiIntegrations
from .openai_api_key_auth import OpenaiApiKeyAuth


class OpenaiProviderAccount(UniversalBaseModel):
    """
    +label=OpenAI Provider Account
    +icon=openai
    """

    type: typing.Literal["provider-account/openai"] = pydantic.Field(default="provider-account/openai")
    """
    +value=provider-account/openai
    """

    name: str = pydantic.Field()
    """
    +label=Name
    +sort=100
    +usage=The name of the OpenAI provider account
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    +uiProps={"disableEdit":true}
    """

    auth_data: OpenaiApiKeyAuth
    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Base URL
    +sort=300
    +usage=Optional custom base URL for OpenAI API
    +message=Base URL must not be empty
    """

    integrations: typing.List[OpenAiIntegrations] = pydantic.Field()
    """
    +label=Integrations
    +sort=400
    +usage=List of integrations that are associated with the OpenAI provider account
    +uiType=IntegrationsGroup
    """

    collaborators: typing.Optional[typing.List[Collaborator]] = pydantic.Field(default=None)
    """
    +label=Collaborators
    +sort=500
    +usage=List of users who have access to this provider account
    +uiType=Collaborators
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
