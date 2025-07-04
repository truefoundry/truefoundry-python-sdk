# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rate_limit_rule import RateLimitRule


class RateLimitConfig(UniversalBaseModel):
    name: str
    type: typing.Literal["gateway-rate-limiting-config"] = "gateway-rate-limiting-config"
    rules: typing.List[RateLimitRule]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
