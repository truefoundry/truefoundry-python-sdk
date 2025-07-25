# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gcp_region import GcpRegion
from .model_cost_metric import ModelCostMetric
from .model_type import ModelType


class VertexModelV2(UniversalBaseModel):
    """
    +label=Vertex Model
    +icon=googleCloud
    """

    type: typing.Literal["integration/model/vertex"] = pydantic.Field(default="integration/model/vertex")
    """
    +value=integration/model/vertex
    """

    name: str = pydantic.Field()
    """
    +label=Display Name
    +sort=1
    +usage=Name to identify this Vertex AI model in the UI
    +message=2 to 62 characters long alphanumeric word, may contain - in between, cannot start with a number
    """

    model_id: str = pydantic.Field()
    """
    +label=Model ID
    +sort=2
    +usage=The unique identifier for the Vertex AI model
    +message=Model ID must not be empty
    """

    region: typing.Optional[GcpRegion] = None
    model_types: typing.List[ModelType] = pydantic.Field()
    """
    +label=Model Types
    +sort=4
    +usage=Specify the type of the Vertex AI model (e.g., chat, text, etc.)
    """

    cost: typing.Optional[ModelCostMetric] = None
    authorized_subjects: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    +label=Access Control
    +sort=6
    +usage=List of subjects that are authorized to access this integration. List of user fqn in format <user_type>:<username>.
    +uiType=Hidden
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
