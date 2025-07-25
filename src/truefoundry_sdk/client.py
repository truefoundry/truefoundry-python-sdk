import os
import typing

import httpx

from truefoundry_sdk._wrapped_clients import (
    WrappedAgentsClient,
    WrappedAgentVersionsClient,
    WrappedApplicationsClient,
    WrappedArtifactsClient,
    WrappedArtifactVersionsClient,
    WrappedAsyncAgentsClient,
    WrappedAsyncAgentVersionsClient,
    WrappedAsyncApplicationsClient,
    WrappedAsyncArtifactsClient,
    WrappedAsyncArtifactVersionsClient,
    WrappedAsyncDataDirectoriesClient,
    WrappedAsyncModelsClient,
    WrappedAsyncModelVersionsClient,
    WrappedAsyncPromptsClient,
    WrappedAsyncPromptVersionsClient,
    WrappedAsyncSecretGroupsClient,
    WrappedAsyncToolsClient,
    WrappedAsyncToolVersionsClient,
    WrappedAsyncTracingProjectsClient,
    WrappedAsyncWorkspacesClient,
    WrappedDataDirectoriesClient,
    WrappedModelsClient,
    WrappedModelVersionsClient,
    WrappedPromptsClient,
    WrappedPromptVersionsClient,
    WrappedSecretGroupsClient,
    WrappedToolsClient,
    WrappedToolVersionsClient,
    WrappedTracingProjectsClient,
    WrappedWorkspacesClient,
)
from truefoundry_sdk.base_client import AsyncBaseTrueFoundry, BaseTrueFoundry


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
        self.agents = WrappedAgentsClient(client_wrapper=self._client_wrapper)
        self.agent_versions = WrappedAgentVersionsClient(client_wrapper=self._client_wrapper)
        self.applications = WrappedApplicationsClient(client_wrapper=self._client_wrapper)
        self.artifacts = WrappedArtifactsClient(client_wrapper=self._client_wrapper)
        self.artifact_versions = WrappedArtifactVersionsClient(client_wrapper=self._client_wrapper)
        self.data_directories = WrappedDataDirectoriesClient(client_wrapper=self._client_wrapper)
        self.models = WrappedModelsClient(client_wrapper=self._client_wrapper)
        self.model_versions = WrappedModelVersionsClient(client_wrapper=self._client_wrapper)
        self.prompts = WrappedPromptsClient(client_wrapper=self._client_wrapper)
        self.prompt_versions = WrappedPromptVersionsClient(client_wrapper=self._client_wrapper)
        self.secret_groups = WrappedSecretGroupsClient(client_wrapper=self._client_wrapper)
        self.tools = WrappedToolsClient(client_wrapper=self._client_wrapper)
        self.tool_versions = WrappedToolVersionsClient(client_wrapper=self._client_wrapper)
        self.tracing_projects = WrappedTracingProjectsClient(client_wrapper=self._client_wrapper)
        self.workspaces = WrappedWorkspacesClient(client_wrapper=self._client_wrapper)


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
        self.agents = WrappedAsyncAgentsClient(client_wrapper=self._client_wrapper)
        self.agent_versions = WrappedAsyncAgentVersionsClient(client_wrapper=self._client_wrapper)
        self.applications = WrappedAsyncApplicationsClient(client_wrapper=self._client_wrapper)
        self.artifacts = WrappedAsyncArtifactsClient(client_wrapper=self._client_wrapper)
        self.artifact_versions = WrappedAsyncArtifactVersionsClient(client_wrapper=self._client_wrapper)
        self.data_directories = WrappedAsyncDataDirectoriesClient(client_wrapper=self._client_wrapper)
        self.models = WrappedAsyncModelsClient(client_wrapper=self._client_wrapper)
        self.model_versions = WrappedAsyncModelVersionsClient(client_wrapper=self._client_wrapper)
        self.prompts = WrappedAsyncPromptsClient(client_wrapper=self._client_wrapper)
        self.prompt_versions = WrappedAsyncPromptVersionsClient(client_wrapper=self._client_wrapper)
        self.secret_groups = WrappedAsyncSecretGroupsClient(client_wrapper=self._client_wrapper)
        self.tools = WrappedAsyncToolsClient(client_wrapper=self._client_wrapper)
        self.tool_versions = WrappedAsyncToolVersionsClient(client_wrapper=self._client_wrapper)
        self.tracing_projects = WrappedAsyncTracingProjectsClient(client_wrapper=self._client_wrapper)
        self.workspaces = WrappedAsyncWorkspacesClient(client_wrapper=self._client_wrapper)


TrueFoundry.__doc__ = BaseTrueFoundry.__doc__
AsyncTrueFoundry.__doc__ = AsyncBaseTrueFoundry.__doc__
