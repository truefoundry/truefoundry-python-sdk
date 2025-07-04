# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_output_based_cost_metric_value import InputOutputBasedCostMetricValue


class PerThousandTokensCostMetric(UniversalBaseModel):
    metric: str = pydantic.Field()
    """
    +value=per_1000_tokens
    """

    value: InputOutputBasedCostMetricValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
