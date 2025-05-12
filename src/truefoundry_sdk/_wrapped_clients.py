from typing import Any, Optional, Protocol, TypeVar

from pydantic import BaseModel


from .errors import NotFoundError
from .core.pagination import AsyncPager, SyncPager
from .core.pydantic_utilities import parse_obj_as

# Clients
from .core.request_options import RequestOptions
from .types.http_error import HttpError
from .agent_versions.client import AgentVersionsClient, AsyncAgentVersionsClient
from .applications.client import ApplicationsClient, AsyncApplicationsClient
from .artifact_versions.client import ArtifactVersionsClient, AsyncArtifactVersionsClient
from .model_versions.client import ModelVersionsClient, AsyncModelVersionsClient
from .prompt_versions.client import PromptVersionsClient, AsyncPromptVersionsClient
from .tool_versions.client import ToolVersionsClient, AsyncToolVersionsClient
from .tracing_projects.client import AsyncTracingProjectsClient, TracingProjectsClient
from .workspaces.client import WorkspacesClient, AsyncWorkspacesClient

# Response types
from .types.get_agent_version_response import GetAgentVersionResponse
from .types.get_application_response import GetApplicationResponse
from .types.get_artifact_version_response import GetArtifactVersionResponse
from .types.get_model_version_response import GetModelVersionResponse
from .types.get_prompt_version_response import GetPromptVersionResponse
from .types.get_tool_version_response import GetToolVersionResponse
from .types.get_tracing_project_response import GetTracingProjectResponse
from .types.get_workspace_response import GetWorkspaceResponse

T = TypeVar("T", bound=BaseModel)


class HasListMethod(Protocol[T]):
    def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs: Any) -> SyncPager[T]:
        ...


class HasAsyncListMethod(Protocol[T]):
    async def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs) -> AsyncPager[T]:
        ...


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


async def _aget_by_fqn(client: HasAsyncListMethod[T], *, fqn: str, request_options: Optional[RequestOptions] = None) -> T:
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


class WrappedAgentVersionsClient(AgentVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetAgentVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentVersionResponse, {"data": item})


class WrappedApplicationsClient(ApplicationsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetApplicationResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetApplicationResponse, {"data": item})


class WrappedArtifactVersionsClient(ArtifactVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedModelVersionsClient(ModelVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedPromptVersionsClient(PromptVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptVersionResponse:
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


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


class WrappedAsyncAgentVersionsClient(AsyncAgentVersionsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetAgentVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentVersionResponse, {"data": item})


class WrappedAsyncApplicationsClient(AsyncApplicationsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetApplicationResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetApplicationResponse, {"data": item})


class WrappedAsyncArtifactVersionsClient(AsyncArtifactVersionsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedAsyncModelVersionsClient(AsyncModelVersionsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedAsyncPromptVersionsClient(AsyncPromptVersionsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


class WrappedAsyncToolVersionsClient(AsyncToolVersionsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetToolVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetToolVersionResponse, {"data": item})


class WrappedAsyncTracingProjectsClient(AsyncTracingProjectsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetTracingProjectResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetTracingProjectResponse, {"data": item})


class WrappedAsyncWorkspacesClient(AsyncWorkspacesClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetWorkspaceResponse:
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetWorkspaceResponse, {"data": item})
