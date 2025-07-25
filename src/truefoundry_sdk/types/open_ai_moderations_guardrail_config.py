# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_guardrail_config import BaseGuardrailConfig
from .open_ai_moderations_guardrail_config_category_thresholds_value import (
    OpenAiModerationsGuardrailConfigCategoryThresholdsValue,
)
from .openai_api_key_auth import OpenaiApiKeyAuth


class OpenAiModerationsGuardrailConfig(BaseGuardrailConfig):
    """
    +label=OpenAI Moderation Guardrail Config
    +icon=openai
    """

    type: typing.Optional[typing.Literal["integration/guardrail-config/openai-moderations"]] = pydantic.Field(
        default=None
    )
    """
    +value=integration/guardrail-config/openai-moderations
    +sort=50
    """

    auth_data: typing.Optional[OpenaiApiKeyAuth] = None
    base_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Base URL
    +sort=300
    +usage=Optional custom base URL for OpenAI API
    +message=Base URL must not be empty
    """

    model: typing.Optional[str] = pydantic.Field(default="omni-moderation-latest")
    """
    +label=OpenAI Moderation Model
    +sort=400
    +usage=The model to use for the OpenAI Moderation API.
    """

    category_thresholds: typing.Optional[typing.Dict[str, OpenAiModerationsGuardrailConfigCategoryThresholdsValue]] = (
        pydantic.Field(default=None)
    )
    """
    +label=Category Thresholds
    +sort=500
    +usage=The thresholds for the OpenAI Moderation API.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
