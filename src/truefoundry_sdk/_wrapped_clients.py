from typing import Any, Optional, Protocol, TypeVar

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
from .types.get_application_response import GetApplicationResponse
from .types.get_artifact_response import GetArtifactResponse
from .types.get_artifact_version_response import GetArtifactVersionResponse
from .types.get_data_directory_response import GetDataDirectoryResponse
from .types.get_model_response import GetModelResponse
from .types.get_model_version_response import GetModelVersionResponse
from .types.get_prompt_response import GetPromptResponse
from .types.get_prompt_version_response import GetPromptVersionResponse
from .types.get_secret_group_response import GetSecretGroupResponse
from .types.get_workspace_response import GetWorkspaceResponse
from .types.http_error import HttpError
from .workspaces.client import AsyncWorkspacesClient, WorkspacesClient
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)
R = TypeVar("R", bound=BaseModel)


class HasListMethod(Protocol[T, R]):
    def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs: Any) -> SyncPager[T, R]: ...


class HasAsyncListMethod(Protocol[T, R]):
    async def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs) -> AsyncPager[T, R]: ...


def _get_by_fqn(client: HasListMethod[T, R], *, fqn: str, request_options: Optional[RequestOptions] = None) -> T:
    result = None
    for item in client.list(fqn=fqn, limit=1, request_options=request_options):
        result = item
        break
    if not result:
        raise NotFoundError(
            body=HttpError(
                message=f"No entity found with fqn {fqn}",
                statusCode=404,
            )
        )
    return result


async def _aget_by_fqn(
    client: HasAsyncListMethod[T, R], *, fqn: str, request_options: Optional[RequestOptions] = None
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
                statusCode=404,
            )
        )
    return result


class WrappedApplicationsClient(ApplicationsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetApplicationResponse:
        """
        Get Application by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicationResponse
            Application details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetApplicationResponse, {"data": item})


class WrappedArtifactsClient(ArtifactsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactResponse:
        """
        Get Artifact by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the artifact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArtifactResponse
            Artifact details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifacts.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactResponse, {"data": item})


class WrappedArtifactVersionsClient(ArtifactVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactVersionResponse:
        """
        Get Artifact Version by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the artifact version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArtifactVersionResponse
            Artifact version details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifact_versions.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedDataDirectoriesClient(DataDirectoriesClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetDataDirectoryResponse:
        """
        Get Data Directory by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the data directory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDataDirectoryResponse
            Data directory details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.data_directories.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetDataDirectoryResponse, {"data": item})


class WrappedModelsClient(ModelsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelResponse:
        """
        Get Model by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelResponse
            Model details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.models.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelResponse, {"data": item})


class WrappedModelVersionsClient(ModelVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelVersionResponse:
        """
        Get Model Version by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the model version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelVersionResponse
            Model version details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.model_versions.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedPromptsClient(PromptsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptResponse:
        """
        Get Prompt by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPromptResponse
            Prompt details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prompts.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptResponse, {"data": item})


class WrappedPromptVersionsClient(PromptVersionsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptVersionResponse:
        """
        Get Prompt Version by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the prompt version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPromptVersionResponse
            Prompt version details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.prompt_versions.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


class WrappedSecretGroupsClient(SecretGroupsClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetSecretGroupResponse:
        """
        Get Secret Group by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the secret group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretGroupResponse
            Secret group details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.secret_groups.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetSecretGroupResponse, {"data": item})


class WrappedWorkspacesClient(WorkspacesClient):
    def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetWorkspaceResponse:
        """
        Get Workspace by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceResponse
            Workspace details

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.workspaces.get_by_fqn(
            fqn="fqn",
        )
        """
        item = _get_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetWorkspaceResponse, {"data": item})


class WrappedAsyncApplicationsClient(AsyncApplicationsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetApplicationResponse:
        """
        Get Application by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicationResponse
            Application details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.applications.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetApplicationResponse, {"data": item})


class WrappedAsyncArtifactsClient(AsyncArtifactsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetArtifactResponse:
        """
        Get Artifact by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the artifact

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArtifactResponse
            Artifact details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.artifacts.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactResponse, {"data": item})


class WrappedAsyncArtifactVersionsClient(AsyncArtifactVersionsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetArtifactVersionResponse:
        """
        Get Artifact Version by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the artifact version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArtifactVersionResponse
            Artifact version details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.artifact_versions.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetArtifactVersionResponse, {"data": item})


class WrappedAsyncDataDirectoriesClient(AsyncDataDirectoriesClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetDataDirectoryResponse:
        """
        Get Data Directory by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the data directory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDataDirectoryResponse
            Data directory details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.data_directories.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetDataDirectoryResponse, {"data": item})


class WrappedAsyncModelsClient(AsyncModelsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetModelResponse:
        """
        Get Model by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelResponse
            Model details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.models.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelResponse, {"data": item})


class WrappedAsyncModelVersionsClient(AsyncModelVersionsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetModelVersionResponse:
        """
        Get Model Version by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the model version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelVersionResponse
            Model version details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.model_versions.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetModelVersionResponse, {"data": item})


class WrappedAsyncPromptsClient(AsyncPromptsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetPromptResponse:
        """
        Get Prompt by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the prompt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPromptResponse
            Prompt details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.prompts.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptResponse, {"data": item})


class WrappedAsyncPromptVersionsClient(AsyncPromptVersionsClient):
    async def get_by_fqn(
        self, fqn: str, *, request_options: Optional[RequestOptions] = None
    ) -> GetPromptVersionResponse:
        """
        Get Prompt Version by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the prompt version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPromptVersionResponse
            Prompt version details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.prompt_versions.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetPromptVersionResponse, {"data": item})


class WrappedAsyncSecretGroupsClient(AsyncSecretGroupsClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetSecretGroupResponse:
        """
        Get Secret Group by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the secret group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSecretGroupResponse
            Secret group details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.secret_groups.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetSecretGroupResponse, {"data": item})


class WrappedAsyncWorkspacesClient(AsyncWorkspacesClient):
    async def get_by_fqn(self, fqn: str, *, request_options: Optional[RequestOptions] = None) -> GetWorkspaceResponse:
        """
        Get Workspace by FQN.

        Parameters
        ----------
        fqn : str
            FQN of the workspace

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceResponse
            Workspace details

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )

        async def main() -> None:
            await client.workspaces.get_by_fqn(
                fqn="fqn",
            )

        asyncio.run(main())
        """
        item = await _aget_by_fqn(self, fqn=fqn, request_options=request_options)  # type: ignore[arg-type,var-annotated]
        return parse_obj_as(GetWorkspaceResponse, {"data": item})
