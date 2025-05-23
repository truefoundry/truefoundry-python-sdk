# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artifact_path import ArtifactPath


class LocalArtifactSource(UniversalBaseModel):
    type: typing.Literal["local"] = pydantic.Field(default="local")
    """
    Type of the source
    """

    paths: typing.List[ArtifactPath] = pydantic.Field()
    """
    Array of ArtifactPath objects representing the source and destination paths
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
