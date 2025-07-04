# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .spark_build import SparkBuild
from .spark_image_build_build_source import SparkImageBuildBuildSource


class SparkImageBuild(UniversalBaseModel):
    """
    +docs=Describes that we are building a new image based on the spec
    +label=Build a new image
    +icon=fa-brands fa-docker:#0db7ed
    TODO (gw): Fix sorting for this such that it looks similar to SparkImage
    """

    type: typing.Literal["spark-image-build"] = pydantic.Field(default="spark-image-build")
    """
    +value=spark-image-build
    """

    docker_registry: typing.Optional[str] = pydantic.Field(default=None)
    """
    +docs=FQN of the container registry. You can the FQN of your desired container registry (or add one)
    in the  Integrations page[Integrations](https://app.truefoundry.tech/integrations?tab=docker-registry) page
    +label=Docker Registry
    +usage=FQN of the container registry. If you can't find your registry here,
    add it through the [Integrations](/integrations?tab=docker-registry) page
    +sort=1002
    """

    build_source: SparkImageBuildBuildSource = pydantic.Field()
    """
    TODO (gw): The following is a hack till the uiType GitSelect is fixed fron frontend
    +label=Fetch source code
    +sort=1003
    """

    build_spec: SparkBuild

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
