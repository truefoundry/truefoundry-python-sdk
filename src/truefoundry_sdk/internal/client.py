# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .applications.client import ApplicationsClient, AsyncApplicationsClient
from .artifact_versions.client import ArtifactVersionsClient, AsyncArtifactVersionsClient
from .clusters.client import AsyncClustersClient, ClustersClient
from .deployments.client import AsyncDeploymentsClient, DeploymentsClient
from .docker_registries.client import AsyncDockerRegistriesClient, DockerRegistriesClient
from .metrics.client import AsyncMetricsClient, MetricsClient
from .ml.client import AsyncMlClient, MlClient
from .raw_client import AsyncRawInternalClient, RawInternalClient
from .users.client import AsyncUsersClient, UsersClient
from .vcs.client import AsyncVcsClient, VcsClient
from .workflows.client import AsyncWorkflowsClient, WorkflowsClient


class InternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalClient(client_wrapper=client_wrapper)
        self.users = UsersClient(client_wrapper=client_wrapper)

        self.clusters = ClustersClient(client_wrapper=client_wrapper)

        self.deployments = DeploymentsClient(client_wrapper=client_wrapper)

        self.applications = ApplicationsClient(client_wrapper=client_wrapper)

        self.vcs = VcsClient(client_wrapper=client_wrapper)

        self.docker_registries = DockerRegistriesClient(client_wrapper=client_wrapper)

        self.metrics = MetricsClient(client_wrapper=client_wrapper)

        self.workflows = WorkflowsClient(client_wrapper=client_wrapper)

        self.artifact_versions = ArtifactVersionsClient(client_wrapper=client_wrapper)

        self.ml = MlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalClient
        """
        return self._raw_client

    def get_id_from_fqn(
        self, type: str, *, fqn: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Get IDs associated with the FQN for various entity types, such as deployment, application, workspace, or cluster.

        Parameters
        ----------
        type : str
            Entity Type

        fqn : str
            Entity FQN

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            Returns the IDs for the specified entity type based on the provided FQN. For example, deploymentId, applicationId, and workspaceId for type deployment, or applicationId and workspaceId for type app.

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.get_id_from_fqn(
            type="type",
            fqn="fqn",
        )
        """
        _response = self._raw_client.get_id_from_fqn(type, fqn=fqn, request_options=request_options)
        return _response.data


class AsyncInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalClient(client_wrapper=client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=client_wrapper)

        self.clusters = AsyncClustersClient(client_wrapper=client_wrapper)

        self.deployments = AsyncDeploymentsClient(client_wrapper=client_wrapper)

        self.applications = AsyncApplicationsClient(client_wrapper=client_wrapper)

        self.vcs = AsyncVcsClient(client_wrapper=client_wrapper)

        self.docker_registries = AsyncDockerRegistriesClient(client_wrapper=client_wrapper)

        self.metrics = AsyncMetricsClient(client_wrapper=client_wrapper)

        self.workflows = AsyncWorkflowsClient(client_wrapper=client_wrapper)

        self.artifact_versions = AsyncArtifactVersionsClient(client_wrapper=client_wrapper)

        self.ml = AsyncMlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalClient
        """
        return self._raw_client

    async def get_id_from_fqn(
        self, type: str, *, fqn: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Optional[typing.Any]]:
        """
        Get IDs associated with the FQN for various entity types, such as deployment, application, workspace, or cluster.

        Parameters
        ----------
        type : str
            Entity Type

        fqn : str
            Entity FQN

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Optional[typing.Any]]
            Returns the IDs for the specified entity type based on the provided FQN. For example, deploymentId, applicationId, and workspaceId for type deployment, or applicationId and workspaceId for type app.

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.get_id_from_fqn(
                type="type",
                fqn="fqn",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_id_from_fqn(type, fqn=fqn, request_options=request_options)
        return _response.data
