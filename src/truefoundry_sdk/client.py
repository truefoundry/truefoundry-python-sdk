import os
import typing

import httpx
from .base_client import AsyncBaseTrueFoundry, BaseTrueFoundry


class TrueFoundry(BaseTrueFoundry):
    def __init__(
        self,
        *,
        base_url: str,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("TFY_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        super().__init__(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
        )

    @property
    def applications(self):
        if self._applications is None:
            from ._wrapped_clients import WrappedApplicationsClient  # noqa: E402

            self._applications = WrappedApplicationsClient(client_wrapper=self._client_wrapper)
        return self._applications

    @property
    def artifacts(self):
        if self._artifacts is None:
            from ._wrapped_clients import WrappedArtifactsClient  # noqa: E402

            self._artifacts = WrappedArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def artifact_versions(self):
        if self._artifact_versions is None:
            from ._wrapped_clients import WrappedArtifactVersionsClient  # noqa: E402

            self._artifact_versions = WrappedArtifactVersionsClient(client_wrapper=self._client_wrapper)
        return self._artifact_versions

    @property
    def data_directories(self):
        if self._data_directories is None:
            from ._wrapped_clients import WrappedDataDirectoriesClient  # noqa: E402

            self._data_directories = WrappedDataDirectoriesClient(client_wrapper=self._client_wrapper)
        return self._data_directories

    @property
    def models(self):
        if self._models is None:
            from ._wrapped_clients import WrappedModelsClient  # noqa: E402

            self._models = WrappedModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def model_versions(self):
        if self._model_versions is None:
            from ._wrapped_clients import WrappedModelVersionsClient  # noqa: E402

            self._model_versions = WrappedModelVersionsClient(client_wrapper=self._client_wrapper)
        return self._model_versions

    @property
    def prompts(self):
        if self._prompts is None:
            from ._wrapped_clients import WrappedPromptsClient  # noqa: E402

            self._prompts = WrappedPromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def prompt_versions(self):
        if self._prompt_versions is None:
            from ._wrapped_clients import WrappedPromptVersionsClient  # noqa: E402

            self._prompt_versions = WrappedPromptVersionsClient(client_wrapper=self._client_wrapper)
        return self._prompt_versions

    @property
    def secret_groups(self):
        if self._secret_groups is None:
            from ._wrapped_clients import WrappedSecretGroupsClient  # noqa: E402

            self._secret_groups = WrappedSecretGroupsClient(client_wrapper=self._client_wrapper)
        return self._secret_groups

    @property
    def workspaces(self):
        if self._workspaces is None:
            from ._wrapped_clients import WrappedWorkspacesClient  # noqa: E402

            self._workspaces = WrappedWorkspacesClient(client_wrapper=self._client_wrapper)
        return self._workspaces


class AsyncTrueFoundry(AsyncBaseTrueFoundry):
    def __init__(
        self,
        *,
        base_url: str,
        api_key: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = os.getenv("TFY_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        super().__init__(
            base_url=base_url,
            api_key=api_key,
            timeout=timeout,
            follow_redirects=follow_redirects,
            httpx_client=httpx_client,
        )

    @property
    def applications(self):
        if self._applications is None:
            from ._wrapped_clients import WrappedAsyncApplicationsClient  # noqa: E402

            self._applications = WrappedAsyncApplicationsClient(client_wrapper=self._client_wrapper)
        return self._applications

    @property
    def artifacts(self):
        if self._artifacts is None:
            from ._wrapped_clients import WrappedAsyncArtifactsClient  # noqa: E402

            self._artifacts = WrappedAsyncArtifactsClient(client_wrapper=self._client_wrapper)
        return self._artifacts

    @property
    def artifact_versions(self):
        if self._artifact_versions is None:
            from ._wrapped_clients import WrappedAsyncArtifactVersionsClient  # noqa: E402

            self._artifact_versions = WrappedAsyncArtifactVersionsClient(client_wrapper=self._client_wrapper)
        return self._artifact_versions

    @property
    def data_directories(self):
        if self._data_directories is None:
            from ._wrapped_clients import WrappedAsyncDataDirectoriesClient  # noqa: E402

            self._data_directories = WrappedAsyncDataDirectoriesClient(client_wrapper=self._client_wrapper)
        return self._data_directories

    @property
    def models(self):
        if self._models is None:
            from ._wrapped_clients import WrappedAsyncModelsClient  # noqa: E402

            self._models = WrappedAsyncModelsClient(client_wrapper=self._client_wrapper)
        return self._models

    @property
    def model_versions(self):
        if self._model_versions is None:
            from ._wrapped_clients import WrappedAsyncModelVersionsClient  # noqa: E402

            self._model_versions = WrappedAsyncModelVersionsClient(client_wrapper=self._client_wrapper)
        return self._model_versions

    @property
    def prompts(self):
        if self._prompts is None:
            from ._wrapped_clients import WrappedAsyncPromptsClient  # noqa: E402

            self._prompts = WrappedAsyncPromptsClient(client_wrapper=self._client_wrapper)
        return self._prompts

    @property
    def prompt_versions(self):
        if self._prompt_versions is None:
            from ._wrapped_clients import WrappedAsyncPromptVersionsClient  # noqa: E402

            self._prompt_versions = WrappedAsyncPromptVersionsClient(client_wrapper=self._client_wrapper)
        return self._prompt_versions

    @property
    def secret_groups(self):
        if self._secret_groups is None:
            from ._wrapped_clients import WrappedAsyncSecretGroupsClient  # noqa: E402

            self._secret_groups = WrappedAsyncSecretGroupsClient(client_wrapper=self._client_wrapper)
        return self._secret_groups

    @property
    def workspaces(self):
        if self._workspaces is None:
            from ._wrapped_clients import WrappedAsyncWorkspacesClient  # noqa: E402

            self._workspaces = WrappedAsyncWorkspacesClient(client_wrapper=self._client_wrapper)
        return self._workspaces


TrueFoundry.__doc__ = BaseTrueFoundry.__doc__
AsyncTrueFoundry.__doc__ = AsyncBaseTrueFoundry.__doc__
