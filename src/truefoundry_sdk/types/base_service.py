# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .artifacts_download import ArtifactsDownload
from .base_service_image import BaseServiceImage
from .base_service_mounts_item import BaseServiceMountsItem
from .health_probe import HealthProbe
from .kustomize import Kustomize
from .port import Port
from .resources import Resources


class BaseService(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    +usage=Name of the service. This uniquely identifies this service in the workspace.
    > Name can only contain alphanumeric characters and '-' and can be atmost 25 characters long
    +sort=1
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    """

    image: BaseServiceImage = pydantic.Field()
    """
    +docs=Specify whether you want to deploy a Docker image or build and deploy from source code
    +label=Deploy a Docker image or build and deploy from source code
    +icon=fa-solid fa-cloud-arrow-up:#21B6A8
    +sort=2
    """

    artifacts_download: typing.Optional[ArtifactsDownload] = None
    resources: typing.Optional[Resources] = None
    env: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    +label=Environment Variables
    +usage=Configure environment variables to be injected in the service either as plain text or secrets. [Docs](https://docs.truefoundry.com/docs/env-variables)
    +icon=fa-globe
    +sort=6
    """

    ports: typing.List[Port] = pydantic.Field()
    """
    +docs=Specify the ports you want the service to be exposed to
    +label=Configure ports and endpoints to route customer traffic
    +usage=Expose the deployment to make it accessible over the internet or keep it private. Implement authentication to restrict access. [Docs](https://docs.truefoundry.com/docs/define-ports-and-domains)
    +icon=fa-plug
    +sort=4
    """

    service_account: typing.Optional[str] = None
    mounts: typing.Optional[typing.List[BaseServiceMountsItem]] = pydantic.Field(default=None)
    """
    +usage=Configure data to be mounted to service pod(s) as a string, secret or volume. [Docs](https://docs.truefoundry.com/docs/mounting-volumes-service)
    +sort=10011
    """

    labels: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    +label=Labels
    """

    kustomize: typing.Optional[Kustomize] = None
    liveness_probe: typing.Optional[HealthProbe] = None
    readiness_probe: typing.Optional[HealthProbe] = None
    workspace_fqn: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Workspace FQN
    +docs=Fully qualified name of the workspace
    +uiType=Hidden
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
