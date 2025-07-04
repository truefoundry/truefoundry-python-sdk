# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ClusterManifestMonitoring(UniversalBaseModel):
    """
    +label=Monitoring
    +icon=fa-gear:#68BBE3
    +sort=50
    """

    loki_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Cluster Loki URL
    """

    victoria_logs_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Cluster VictoriaLogs URL
    """

    prometheus_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Cluster Prometheus URL
    """

    kubecost_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Cluster Kubecost URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
