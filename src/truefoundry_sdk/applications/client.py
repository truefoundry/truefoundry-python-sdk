# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.application import Application
from ..types.delete_application_response import DeleteApplicationResponse
from ..types.deployment import Deployment
from ..types.get_application_deployment_response import GetApplicationDeploymentResponse
from ..types.get_application_response import GetApplicationResponse
from .raw_client import AsyncRawApplicationsClient, RawApplicationsClient
from .types.applications_cancel_deployment_response import ApplicationsCancelDeploymentResponse
from .types.applications_list_request_device_type_filter import ApplicationsListRequestDeviceTypeFilter
from .types.applications_list_request_lifecycle_stage import ApplicationsListRequestLifecycleStage

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ApplicationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplicationsClient
        """
        return self._raw_client

    def list(
        self,
        *,
        limit: typing.Optional[int] = 100,
        offset: typing.Optional[int] = 0,
        application_id: typing.Optional[str] = None,
        workspace_id: typing.Optional[str] = None,
        application_name: typing.Optional[str] = None,
        fqn: typing.Optional[str] = None,
        workspace_fqn: typing.Optional[str] = None,
        application_type: typing.Optional[str] = None,
        name_search_query: typing.Optional[str] = None,
        environment_id: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        application_set_id: typing.Optional[str] = None,
        paused: typing.Optional[bool] = None,
        device_type_filter: typing.Optional[ApplicationsListRequestDeviceTypeFilter] = None,
        last_deployed_by_subjects: typing.Optional[str] = None,
        lifecycle_stage: typing.Optional[ApplicationsListRequestLifecycleStage] = None,
        is_recommendation_present_and_visible: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Application]:
        """
        Retrieves a list of all latest applications. Supports filtering by application ID, name, type, and other parameters. Pagination is available based on query parameters.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of items per page

        offset : typing.Optional[int]
            Number of items to skip

        application_id : typing.Optional[str]
            Application id of the application

        workspace_id : typing.Optional[str]
            Workspace id of the application (comma separated for multiple)

        application_name : typing.Optional[str]
            Name of application

        fqn : typing.Optional[str]
            Fully qualified name (FQN) of the application

        workspace_fqn : typing.Optional[str]
            Fully qualified name (FQN) of the workspace

        application_type : typing.Optional[str]
            Type of application (comma separated for multiple). Allowed Values: async-service, service, job, spark-job, helm, notebook, codeserver, rstudio, ssh-server, volume, application, application-set, intercept, workflow

        name_search_query : typing.Optional[str]
            Search query for application name

        environment_id : typing.Optional[str]
            Filter by Environment ids of the application (comma separated for multiple)

        cluster_id : typing.Optional[str]
            Filter by Cluster ids of the application (comma separated for multiple)

        application_set_id : typing.Optional[str]
            Filter by Application Set id of the application

        paused : typing.Optional[bool]
            Filter by Application Paused status

        device_type_filter : typing.Optional[ApplicationsListRequestDeviceTypeFilter]
            Filter by device type of the application. Allowed values: cpu, nvidia_gpu, aws_inferentia, nvidia_mig_gpu, nvidia_timeslicing_gpu, gcp_tpu

        last_deployed_by_subjects : typing.Optional[str]
            Filter by last deployed by specific users

        lifecycle_stage : typing.Optional[ApplicationsListRequestLifecycleStage]
            Filter by application lifecycle state

        is_recommendation_present_and_visible : typing.Optional[bool]
            Filter out applications with recommendations that are allowed to be shown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Application]
            Retrieve latest applications based on the specified query parameters. If pagination parameters are provided, the response includes paginated data.

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.applications.list(
            limit=10,
            offset=0,
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            limit=limit,
            offset=offset,
            application_id=application_id,
            workspace_id=workspace_id,
            application_name=application_name,
            fqn=fqn,
            workspace_fqn=workspace_fqn,
            application_type=application_type,
            name_search_query=name_search_query,
            environment_id=environment_id,
            cluster_id=cluster_id,
            application_set_id=application_set_id,
            paused=paused,
            device_type_filter=device_type_filter,
            last_deployed_by_subjects=last_deployed_by_subjects,
            lifecycle_stage=lifecycle_stage,
            is_recommendation_present_and_visible=is_recommendation_present_and_visible,
            request_options=request_options,
        )

    def create_or_update(
        self,
        *,
        manifest: typing.Dict[str, typing.Optional[typing.Any]],
        dry_run: typing.Optional[bool] = OMIT,
        force_deploy: typing.Optional[bool] = OMIT,
        trigger_on_deploy: typing.Optional[bool] = OMIT,
        workspace_id: typing.Optional[str] = OMIT,
        application_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        application_set_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApplicationDeploymentResponse:
        """
        Create a new Application Deployment based on the provided manifest.

        Parameters
        ----------
        manifest : typing.Dict[str, typing.Optional[typing.Any]]
            Manifest of application

        dry_run : typing.Optional[bool]
            Dry run

        force_deploy : typing.Optional[bool]
            Cancels any ongoing deployments

        trigger_on_deploy : typing.Optional[bool]
            Trigger on deploy

        workspace_id : typing.Optional[str]
            workspace id of the workspace

        application_id : typing.Optional[str]
            Id of the application

        name : typing.Optional[str]
            Name of application

        application_set_id : typing.Optional[str]
            Application Set Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicationDeploymentResponse
            Returns new deployment on successful creation
                  - It also creates an application if not already present
                  - validates third party requirements
                  - updates application, version

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.create_or_update(
            manifest={"key": "value"},
        )
        """
        _response = self._raw_client.create_or_update(
            manifest=manifest,
            dry_run=dry_run,
            force_deploy=force_deploy,
            trigger_on_deploy=trigger_on_deploy,
            workspace_id=workspace_id,
            application_id=application_id,
            name=name,
            application_set_id=application_set_id,
            request_options=request_options,
        )
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetApplicationResponse:
        """
        Get Application associated with the provided application ID.

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicationResponse
            Application details retrieved successfully

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DeleteApplicationResponse:
        """
        Delete Application associated with the provided application ID.

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteApplicationResponse
            Delete application response.

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def scale_to_zero(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Pause a running application by scaling to 0 replicas

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.scale_to_zero(
            id="id",
        )
        """
        _response = self._raw_client.scale_to_zero(id, request_options=request_options)
        return _response.data

    def scale_to_original(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Deployment:
        """
        Resume a paused application by scaling back to the original number of replicas

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deployment
            Scales back a paused applicaion to the original number of replicas

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.scale_to_original(
            id="id",
        )
        """
        _response = self._raw_client.scale_to_original(id, request_options=request_options)
        return _response.data

    def cancel_deployment(
        self, id: str, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationsCancelDeploymentResponse:
        """
        Cancel an ongoing deployment associated with the provided application ID and deployment ID.

        Parameters
        ----------
        id : str
            Application id of the application

        deployment_id : str
            Deployment id of the deployment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationsCancelDeploymentResponse
            Deployment cancelled successfully.

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.applications.cancel_deployment(
            id="id",
            deployment_id="deploymentId",
        )
        """
        _response = self._raw_client.cancel_deployment(id, deployment_id, request_options=request_options)
        return _response.data


class AsyncApplicationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplicationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplicationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplicationsClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        limit: typing.Optional[int] = 100,
        offset: typing.Optional[int] = 0,
        application_id: typing.Optional[str] = None,
        workspace_id: typing.Optional[str] = None,
        application_name: typing.Optional[str] = None,
        fqn: typing.Optional[str] = None,
        workspace_fqn: typing.Optional[str] = None,
        application_type: typing.Optional[str] = None,
        name_search_query: typing.Optional[str] = None,
        environment_id: typing.Optional[str] = None,
        cluster_id: typing.Optional[str] = None,
        application_set_id: typing.Optional[str] = None,
        paused: typing.Optional[bool] = None,
        device_type_filter: typing.Optional[ApplicationsListRequestDeviceTypeFilter] = None,
        last_deployed_by_subjects: typing.Optional[str] = None,
        lifecycle_stage: typing.Optional[ApplicationsListRequestLifecycleStage] = None,
        is_recommendation_present_and_visible: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Application]:
        """
        Retrieves a list of all latest applications. Supports filtering by application ID, name, type, and other parameters. Pagination is available based on query parameters.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of items per page

        offset : typing.Optional[int]
            Number of items to skip

        application_id : typing.Optional[str]
            Application id of the application

        workspace_id : typing.Optional[str]
            Workspace id of the application (comma separated for multiple)

        application_name : typing.Optional[str]
            Name of application

        fqn : typing.Optional[str]
            Fully qualified name (FQN) of the application

        workspace_fqn : typing.Optional[str]
            Fully qualified name (FQN) of the workspace

        application_type : typing.Optional[str]
            Type of application (comma separated for multiple). Allowed Values: async-service, service, job, spark-job, helm, notebook, codeserver, rstudio, ssh-server, volume, application, application-set, intercept, workflow

        name_search_query : typing.Optional[str]
            Search query for application name

        environment_id : typing.Optional[str]
            Filter by Environment ids of the application (comma separated for multiple)

        cluster_id : typing.Optional[str]
            Filter by Cluster ids of the application (comma separated for multiple)

        application_set_id : typing.Optional[str]
            Filter by Application Set id of the application

        paused : typing.Optional[bool]
            Filter by Application Paused status

        device_type_filter : typing.Optional[ApplicationsListRequestDeviceTypeFilter]
            Filter by device type of the application. Allowed values: cpu, nvidia_gpu, aws_inferentia, nvidia_mig_gpu, nvidia_timeslicing_gpu, gcp_tpu

        last_deployed_by_subjects : typing.Optional[str]
            Filter by last deployed by specific users

        lifecycle_stage : typing.Optional[ApplicationsListRequestLifecycleStage]
            Filter by application lifecycle state

        is_recommendation_present_and_visible : typing.Optional[bool]
            Filter out applications with recommendations that are allowed to be shown

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Application]
            Retrieve latest applications based on the specified query parameters. If pagination parameters are provided, the response includes paginated data.

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.applications.list(
                limit=10,
                offset=0,
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            limit=limit,
            offset=offset,
            application_id=application_id,
            workspace_id=workspace_id,
            application_name=application_name,
            fqn=fqn,
            workspace_fqn=workspace_fqn,
            application_type=application_type,
            name_search_query=name_search_query,
            environment_id=environment_id,
            cluster_id=cluster_id,
            application_set_id=application_set_id,
            paused=paused,
            device_type_filter=device_type_filter,
            last_deployed_by_subjects=last_deployed_by_subjects,
            lifecycle_stage=lifecycle_stage,
            is_recommendation_present_and_visible=is_recommendation_present_and_visible,
            request_options=request_options,
        )

    async def create_or_update(
        self,
        *,
        manifest: typing.Dict[str, typing.Optional[typing.Any]],
        dry_run: typing.Optional[bool] = OMIT,
        force_deploy: typing.Optional[bool] = OMIT,
        trigger_on_deploy: typing.Optional[bool] = OMIT,
        workspace_id: typing.Optional[str] = OMIT,
        application_id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        application_set_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetApplicationDeploymentResponse:
        """
        Create a new Application Deployment based on the provided manifest.

        Parameters
        ----------
        manifest : typing.Dict[str, typing.Optional[typing.Any]]
            Manifest of application

        dry_run : typing.Optional[bool]
            Dry run

        force_deploy : typing.Optional[bool]
            Cancels any ongoing deployments

        trigger_on_deploy : typing.Optional[bool]
            Trigger on deploy

        workspace_id : typing.Optional[str]
            workspace id of the workspace

        application_id : typing.Optional[str]
            Id of the application

        name : typing.Optional[str]
            Name of application

        application_set_id : typing.Optional[str]
            Application Set Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicationDeploymentResponse
            Returns new deployment on successful creation
                  - It also creates an application if not already present
                  - validates third party requirements
                  - updates application, version

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.create_or_update(
                manifest={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update(
            manifest=manifest,
            dry_run=dry_run,
            force_deploy=force_deploy,
            trigger_on_deploy=trigger_on_deploy,
            workspace_id=workspace_id,
            application_id=application_id,
            name=name,
            application_set_id=application_set_id,
            request_options=request_options,
        )
        return _response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetApplicationResponse:
        """
        Get Application associated with the provided application ID.

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApplicationResponse
            Application details retrieved successfully

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteApplicationResponse:
        """
        Delete Application associated with the provided application ID.

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteApplicationResponse
            Delete application response.

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def scale_to_zero(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Pause a running application by scaling to 0 replicas

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.scale_to_zero(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scale_to_zero(id, request_options=request_options)
        return _response.data

    async def scale_to_original(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Deployment:
        """
        Resume a paused application by scaling back to the original number of replicas

        Parameters
        ----------
        id : str
            Id of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Deployment
            Scales back a paused applicaion to the original number of replicas

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.scale_to_original(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.scale_to_original(id, request_options=request_options)
        return _response.data

    async def cancel_deployment(
        self, id: str, deployment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationsCancelDeploymentResponse:
        """
        Cancel an ongoing deployment associated with the provided application ID and deployment ID.

        Parameters
        ----------
        id : str
            Application id of the application

        deployment_id : str
            Deployment id of the deployment

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationsCancelDeploymentResponse
            Deployment cancelled successfully.

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.applications.cancel_deployment(
                id="id",
                deployment_id="deploymentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_deployment(id, deployment_id, request_options=request_options)
        return _response.data
