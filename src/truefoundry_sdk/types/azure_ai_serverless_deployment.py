# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AzureAiServerlessDeployment(UniversalBaseModel):
    """
    +label=Azure AI Serverless Deployment
    """

    type: typing.Literal["serverless"] = pydantic.Field(default="serverless")
    """
    +value=serverless
    """

    deployment_name: typing_extensions.Annotated[str, FieldMetadata(alias="deploymentName")] = pydantic.Field()
    """
    +label=Azure Deployment Name
    +usage=Name of the Azure AI deployment
    +sort=100
    """

    region: str = pydantic.Field()
    """
    +label=Azure Region
    +usage=Region where the Azure AI deployment is located
    +sort=200
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
