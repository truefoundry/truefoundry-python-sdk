# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fallback_rule import FallbackRule


class FallbackConfig(UniversalBaseModel):
    name: str
    type: typing.Literal["gateway-fallback-config"] = "gateway-fallback-config"
    rules: typing.List[FallbackRule]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
