from typing import Any, Optional, Protocol, TypeVar

from .agent_versions.client import AgentVersionsClient, AsyncAgentVersionsClient
from .agents.client import AgentsClient, AsyncAgentsClient
from .applications.client import ApplicationsClient, AsyncApplicationsClient
from .artifact_versions.client import ArtifactVersionsClient, AsyncArtifactVersionsClient
from .artifacts.client import ArtifactsClient, AsyncArtifactsClient
from .core.pagination import AsyncPager, SyncPager
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .data_directories.client import AsyncDataDirectoriesClient, DataDirectoriesClient
from .errors import NotFoundError
from .model_versions.client import AsyncModelVersionsClient, ModelVersionsClient
from .models.client import AsyncModelsClient, ModelsClient
from .prompt_versions.client import AsyncPromptVersionsClient, PromptVersionsClient
from .prompts.client import AsyncPromptsClient, PromptsClient
from .secret_groups.client import AsyncSecretGroupsClient, SecretGroupsClient
from .tool_versions.client import AsyncToolVersionsClient, ToolVersionsClient
from .tools.client import AsyncToolsClient, ToolsClient
from .tracing_projects.client import AsyncTracingProjectsClient, TracingProjectsClient
from .types.get_agent_response import GetAgentResponse
from .types.get_agent_version_response import GetAgentVersionResponse
from .types.get_application_response import GetApplicationResponse
from .types.get_artifact_response import GetArtifactResponse
from .types.get_artifact_version_response import GetArtifactVersionResponse
from .types.get_data_directory_response import GetDataDirectoryResponse
from .types.get_model_response import GetModelResponse
from .types.get_model_version_response import GetModelVersionResponse
from .types.get_prompt_response import GetPromptResponse
from .types.get_prompt_version_response import GetPromptVersionResponse
from .types.get_secret_group_response import GetSecretGroupResponse
from .types.get_tool_response import GetToolResponse
from .types.get_tool_version_response import GetToolVersionResponse
from .types.get_tracing_project_response import GetTracingProjectResponse
from .types.get_workspace_response import GetWorkspaceResponse
from .types.http_error import HttpError
from .workspaces.client import AsyncWorkspacesClient, WorkspacesClient
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class HasListMethod(Protocol[T]):
    def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs: Any) -> SyncPager[T]: ...


class HasAsyncListMethod(Protocol[T]):
    async def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs) -> AsyncPager[T]: ...


def _get_by_fqn(client: HasListMethod[T], *, fqn: str, request_options: Optional[RequestOptions] = None) -> T:
    result = None
    for item in client.list(fqn=fqn, limit=1, request_options=request_options):
        result = item
        break
    if not result:
        raise NotFoundError(
            body=HttpError(
                message=f"No entity found with fqn {fqn}",
                status_code=404,
            )
        )
    return result


async def _aget_by_fqn(
    client: HasAsyncListMethod[T], *, fqn: str, request_options: Optional[RequestOptions] = None
) -> T:
    result = None
    pager = await client.list(fqn=fqn, limit=1, request_options=request_options)
    async for item in pager:
        result = item
        break

    if not result:
        raise NotFoundError(
            body=HttpError(
                message=f"No entity found with fqn {fqn}",
                status_code=404,
            )
        )
    return result


class WrappedAgentsClient(AgentsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetAgentResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentResponse, {"data": item})  # type: ignore[arg-type,var-annotated]


class WrappedAgentVersionsClient(AgentVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetAgentVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentVersionResponse, {"data": item})


class WrappedApplicationsClient(ApplicationsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetApplicationResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetApplicationResponse, {"data": item})


class WrappedArtifactsClient(ArtifactsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactResponse, {"data": item})


class WrappedArtifactVersionsClient(ArtifactVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedDataDirectoriesClient(DataDirectoriesClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetDataDirectoryResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetDataDirectoryResponse, {"data": item})


class WrappedModelsClient(ModelsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelResponse, {"data": item})


class WrappedModelVersionsClient(ModelVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedPromptsClient(PromptsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptResponse, {"data": item})


class WrappedPromptVersionsClient(PromptVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


class WrappedSecretGroupsClient(SecretGroupsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetSecretGroupResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetSecretGroupResponse, {"data": item})


class WrappedToolsClient(ToolsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetToolResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetToolResponse, {"data": item})


class WrappedToolVersionsClient(ToolVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetToolVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetToolVersionResponse, {"data": item})


class WrappedTracingProjectsClient(TracingProjectsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetTracingProjectResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetTracingProjectResponse, {"data": item})


class WrappedWorkspacesClient(WorkspacesClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetWorkspaceResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetWorkspaceResponse, {"data": item})


class WrappedAsyncAgentsClient(AsyncAgentsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetAgentResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentResponse, {"data": item})


class WrappedAsyncAgentVersionsClient(AsyncAgentVersionsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetAgentVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentVersionResponse, {"data": item})


class WrappedAsyncApplicationsClient(AsyncApplicationsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetApplicationResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetApplicationResponse, {"data": item})


class WrappedAsyncArtifactsClient(AsyncArtifactsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactResponse, {"data": item})


class WrappedAsyncArtifactVersionsClient(AsyncArtifactVersionsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetArtifactVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedAsyncDataDirectoriesClient(AsyncDataDirectoriesClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetDataDirectoryResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetDataDirectoryResponse, {"data": item})


class WrappedAsyncModelsClient(AsyncModelsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelResponse, {"data": item})


class WrappedAsyncModelVersionsClient(AsyncModelVersionsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetModelVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedAsyncPromptsClient(AsyncPromptsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptResponse, {"data": item})


class WrappedAsyncPromptVersionsClient(AsyncPromptVersionsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetPromptVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


class WrappedAsyncSecretGroupsClient(AsyncSecretGroupsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetSecretGroupResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetSecretGroupResponse, {"data": item})


class WrappedAsyncToolsClient(AsyncToolsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetToolResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetToolResponse, {"data": item})


class WrappedAsyncToolVersionsClient(AsyncToolVersionsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetToolVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetToolVersionResponse, {"data": item})


class WrappedAsyncTracingProjectsClient(AsyncTracingProjectsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetTracingProjectResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetTracingProjectResponse, {"data": item})


class WrappedAsyncWorkspacesClient(AsyncWorkspacesClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetWorkspaceResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetWorkspaceResponse, {"data": item})
