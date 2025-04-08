from typing import Any, Optional, Protocol, TypeVar

from pydantic import BaseModel

from truefoundry_sdk.core.api_error import ApiError
from truefoundry_sdk.core.pagination import AsyncPager, SyncPager
from truefoundry_sdk.core.pydantic_utilities import parse_obj_as

# Clients
from truefoundry_sdk.v1.agent_versions.client import (
    AgentVersionsClient,
    AsyncAgentVersionsClient,
)
from truefoundry_sdk.v1.artifact_versions.client import (
    ArtifactVersionsClient,
    AsyncArtifactVersionsClient,
)
from truefoundry_sdk.v1.model_versions.client import (
    ModelVersionsClient,
    AsyncModelVersionsClient,
)
from truefoundry_sdk.v1.prompt_versions.client import (
    PromptVersionsClient,
    AsyncPromptVersionsClient,
)
from truefoundry_sdk.v1.tool_versions.client import (
    ToolVersionsClient,
    AsyncToolVersionsClient,
)
from truefoundry_sdk.v1.workspaces.client import WorkspacesClient, AsyncWorkspacesClient

# Response types
from truefoundry_sdk.types.get_agent_version_response import GetAgentVersionResponse
from truefoundry_sdk.types.get_artifact_version_response import (
    GetArtifactVersionResponse,
)
from truefoundry_sdk.types.get_model_version_response import GetModelVersionResponse
from truefoundry_sdk.types.get_prompt_version_response import GetPromptVersionResponse
from truefoundry_sdk.types.get_tool_version_response import GetToolVersionResponse
from truefoundry_sdk.types.get_workspace_response import GetWorkspaceResponse

T = TypeVar("T", bound=BaseModel)


class HasListMethod(Protocol[T]):
    def list(
        self, *, fqn: str, limit: Optional[int] = None, **kwargs: Any
    ) -> SyncPager[T]: ...


class HasAsyncListMethod(Protocol[T]):
    async def list(
        self, *, fqn: str, limit: Optional[int] = None, **kwargs
    ) -> AsyncPager[T]: ...


def _get_by_fqn(client: HasListMethod[T], *, fqn: str) -> T:
    result = None
    for item in client.list(fqn=fqn, limit=1):
        result = item
        break
    if not result:
        raise ApiError(
            body=f"No entity found with fqn {fqn}",
            status_code=404,
        )
    return result


async def _aget_by_fqn(client: HasAsyncListMethod[T], *, fqn: str) -> T:
    result = None
    pager = await client.list(fqn=fqn, limit=1)
    async for item in pager:
        result = item
        break

    if not result:
        raise ApiError(
            body=f"No entity found with fqn {fqn}",
            status_code=404,
        )
    return result


class WrappedAgentVersionsClient(AgentVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetAgentVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentVersionResponse, {"data": item})


class WrappedArtifactVersionsClient(ArtifactVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetArtifactVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedModelVersionsClient(ModelVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetModelVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedPromptVersionsClient(PromptVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetPromptVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


class WrappedToolVersionsClient(ToolVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetToolVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetToolVersionResponse, {"data": item})


class WrappedWorkspacesClient(WorkspacesClient):
    def get_by_fqn(self, *, fqn: str) -> GetWorkspaceResponse:
        item = _get_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetWorkspaceResponse, {"data": item})


class WrappedAsyncAgentVersionsClient(AsyncAgentVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetAgentVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetAgentVersionResponse, {"data": item})


class WrappedAsyncArtifactVersionsClient(AsyncArtifactVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetArtifactVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedAsyncModelVersionsClient(AsyncModelVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetModelVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedAsyncPromptVersionsClient(AsyncPromptVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetPromptVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


class WrappedAsyncToolVersionsClient(AsyncToolVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetToolVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetToolVersionResponse, {"data": item})


class WrappedAsyncWorkspacesClient(AsyncWorkspacesClient):
    async def get_by_fqn(self, *, fqn: str) -> GetWorkspaceResponse:
        item = await _aget_by_fqn(self, fqn=fqn)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetWorkspaceResponse, {"data": item})
