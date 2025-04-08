from typing import Any, Optional, Protocol, TypeVar

from pydantic import BaseModel

from truefoundry_sdk.core.api_error import ApiError
from truefoundry_sdk.core.pagination import AsyncPager, SyncPager

# Clients
from truefoundry_sdk.v1.agent_versions.client import AgentVersionsClient, AsyncAgentVersionsClient
from truefoundry_sdk.v1.agents.client import AgentsClient, AsyncAgentsClient
from truefoundry_sdk.v1.artifact_versions.client import ArtifactVersionsClient, AsyncArtifactVersionsClient
from truefoundry_sdk.v1.data_directories.client import DataDirectoriesClient, AsyncDataDirectoriesClient
from truefoundry_sdk.v1.model_versions.client import ModelVersionsClient, AsyncModelVersionsClient
from truefoundry_sdk.v1.models.client import ModelsClient, AsyncModelsClient
from truefoundry_sdk.v1.prompt_versions.client import PromptVersionsClient, AsyncPromptVersionsClient
from truefoundry_sdk.v1.prompts.client import PromptsClient, AsyncPromptsClient
from truefoundry_sdk.v1.tool_versions.client import ToolVersionsClient, AsyncToolVersionsClient
from truefoundry_sdk.v1.tools.client import ToolsClient, AsyncToolsClient
from truefoundry_sdk.v1.workspaces.client import WorkspacesClient, AsyncWorkspacesClient

# Response types
from truefoundry_sdk.types.get_agent_version_response import GetAgentVersionResponse
from truefoundry_sdk.types.get_agent_response import GetAgentResponse
from truefoundry_sdk.types.get_artifact_version_response import GetArtifactVersionResponse
from truefoundry_sdk.types.get_data_directory_response import GetDataDirectoryResponse
from truefoundry_sdk.types.get_model_version_response import GetModelVersionResponse
from truefoundry_sdk.types.get_model_response import GetModelResponse
from truefoundry_sdk.types.get_prompt_version_response import GetPromptVersionResponse
from truefoundry_sdk.types.get_prompt_response import GetPromptResponse
from truefoundry_sdk.types.get_tool_version_response import GetToolVersionResponse
from truefoundry_sdk.types.get_tool_response import GetToolResponse
from truefoundry_sdk.types.get_workspace_response import GetWorkspaceResponse

T = TypeVar("T", bound=BaseModel)

class HasListMethod(Protocol[T]):
    def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs: Any) -> SyncPager[T]:
        ...


class HasAsyncListMethod(Protocol[T]):
    async def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs) -> AsyncPager[T]:
        ...


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
        item = _get_by_fqn(self, fqn=fqn)
        return GetAgentVersionResponse.model_validate({"data": item})

class WrappedAgentsClient(AgentsClient):
    def get_by_fqn(self, *, fqn: str) -> GetAgentResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetAgentResponse.model_validate({"data": item})

class WrappedArtifactVersionsClient(ArtifactVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetArtifactVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetArtifactVersionResponse.model_validate({"data": item})

class WrappedDataDirectoriesClient(DataDirectoriesClient):
    def get_by_fqn(self, *, fqn: str) -> GetDataDirectoryResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetDataDirectoryResponse.model_validate({"data": item})

class WrappedModelVersionsClient(ModelVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetModelVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetModelVersionResponse.model_validate({"data": item})

class WrappedModelsClient(ModelsClient):
    def get_by_fqn(self, *, fqn: str) -> GetModelResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetModelResponse.model_validate({"data": item})

class WrappedPromptVersionsClient(PromptVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetPromptVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetPromptVersionResponse.model_validate({"data": item})

class WrappedPromptsClient(PromptsClient):
    def get_by_fqn(self, *, fqn: str) -> GetPromptResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetPromptResponse.model_validate({"data": item})

class WrappedToolVersionsClient(ToolVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetToolVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetToolVersionResponse.model_validate({"data": item})

class WrappedToolsClient(ToolsClient):
    def get_by_fqn(self, *, fqn: str) -> GetToolResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetToolResponse.model_validate({"data": item})

class WrappedWorkspacesClient(WorkspacesClient):
    def get_by_fqn(self, *, fqn: str) -> GetWorkspaceResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetWorkspaceResponse.model_validate({"data": item})



class WrappedAsyncAgentVersionsClient(AsyncAgentVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetAgentVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetAgentVersionResponse.model_validate({"data": item})

class WrappedAsyncAgentsClient(AsyncAgentsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetAgentResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetAgentResponse.model_validate({"data": item})

class WrappedAsyncArtifactVersionsClient(AsyncArtifactVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetArtifactVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetArtifactVersionResponse.model_validate({"data": item})

class WrappedAsyncDataDirectoriesClient(AsyncDataDirectoriesClient):
    async def get_by_fqn(self, *, fqn: str) -> GetDataDirectoryResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetDataDirectoryResponse.model_validate({"data": item})

class WrappedAsyncModelVersionsClient(AsyncModelVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetModelVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetModelVersionResponse.model_validate({"data": item})

class WrappedAsyncModelsClient(AsyncModelsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetModelResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetModelResponse.model_validate({"data": item})

class WrappedAsyncPromptVersionsClient(AsyncPromptVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetPromptVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetPromptVersionResponse.model_validate({"data": item})

class WrappedAsyncPromptsClient(AsyncPromptsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetPromptResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetPromptResponse.model_validate({"data": item})

class WrappedAsyncToolVersionsClient(AsyncToolVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetToolVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetToolVersionResponse.model_validate({"data": item})

class WrappedAsyncToolsClient(AsyncToolsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetToolResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetToolResponse.model_validate({"data": item})

class WrappedAsyncWorkspacesClient(AsyncWorkspacesClient):
    async def get_by_fqn(self, *, fqn: str) -> GetWorkspaceResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetWorkspaceResponse.model_validate({"data": item})
