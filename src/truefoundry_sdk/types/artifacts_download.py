# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artifacts_cache_volume import ArtifactsCacheVolume
from .artifacts_download_artifacts_item import ArtifactsDownloadArtifactsItem


class ArtifactsDownload(UniversalBaseModel):
    """
    +docs=Describes the configuration for the artifacts cache
    +label=Artifacts Download
    +usage=Download and cache models in a volume to enhance loading speeds and reduce costs by avoiding repeated downloads. [Docs](https://docs.truefoundry.com/docs/download-and-cache-models)
    """

    cache_volume: typing.Optional[ArtifactsCacheVolume] = None
    artifacts: typing.List[ArtifactsDownloadArtifactsItem] = pydantic.Field()
    """
    +label=Artifacts
    +usage=List of artifacts to be cached
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
