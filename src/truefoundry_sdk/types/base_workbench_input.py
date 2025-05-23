# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_workbench_input_mounts_item import BaseWorkbenchInputMountsItem
from .kustomize import Kustomize
from .resources import Resources


class BaseWorkbenchInput(UniversalBaseModel):
    """
    +docs=Describes the configuration for the service
    """

    name: str = pydantic.Field()
    """
    +usage=Name of the workbench. This uniquely identifies this workbench in the workspace.
    > Name can only contain alphanumeric characters and '-' and can be atmost 25 characters long
    +sort=1
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    """

    home_directory_size: int = pydantic.Field(default=20)
    """
    +label=Home Directory Size in GB (Persistent)
    +usage=Size of the home directory for the workbench (Persistent Storage)
    +sort=6
    """

    resources: typing.Optional[Resources] = None
    env: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    +label=Environment Variables
    +usage=Configure environment variables to be injected in the service either as plain text or secrets. [Docs](https://docs.truefoundry.com/docs/environment-variables-and-secrets-jobs)
    +sort=10110
    """

    mounts: typing.Optional[typing.List[BaseWorkbenchInputMountsItem]] = pydantic.Field(default=None)
    """
    +usage=Configure data to be mounted to workbench pod(s) as a string, secret or volume. [Docs](https://docs.truefoundry.com/docs/mounting-volumes-job)
    +sort=10111
    """

    service_account: typing.Optional[str] = pydantic.Field(default=None)
    """
    +sort=10113
    """

    kustomize: typing.Optional[Kustomize] = None
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
