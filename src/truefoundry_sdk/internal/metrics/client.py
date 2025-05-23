# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.get_charts_response import GetChartsResponse
from .raw_client import AsyncRawMetricsClient, RawMetricsClient
from .types.metrics_get_charts_request_filter_entity import MetricsGetChartsRequestFilterEntity


class MetricsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetricsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetricsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetricsClient
        """
        return self._raw_client

    def get_charts(
        self,
        workspace_id: str,
        *,
        application_id: str,
        filter_entity: MetricsGetChartsRequestFilterEntity,
        start_ts: typing.Optional[str] = None,
        end_ts: typing.Optional[str] = None,
        filter_query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChartsResponse:
        """
        List charts for a given Application based on parameters passed in the query.

        Parameters
        ----------
        workspace_id : str

        application_id : str

        filter_entity : MetricsGetChartsRequestFilterEntity

        start_ts : typing.Optional[str]
            Start Timestamp

        end_ts : typing.Optional[str]
            End Timestamp

        filter_query : typing.Optional[str]
            Query params to filter metrics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChartsResponse
            Charts have been successfully retrieved.

        Examples
        --------
        from truefoundry_sdk import TrueFoundry
        from truefoundry_sdk.internal.metrics import MetricsGetChartsRequestFilterEntity

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.metrics.get_charts(
            workspace_id="workspaceId",
            application_id="applicationId",
            filter_entity=MetricsGetChartsRequestFilterEntity.APPLICATION,
        )
        """
        _response = self._raw_client.get_charts(
            workspace_id,
            application_id=application_id,
            filter_entity=filter_entity,
            start_ts=start_ts,
            end_ts=end_ts,
            filter_query=filter_query,
            request_options=request_options,
        )
        return _response.data


class AsyncMetricsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetricsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetricsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetricsClient
        """
        return self._raw_client

    async def get_charts(
        self,
        workspace_id: str,
        *,
        application_id: str,
        filter_entity: MetricsGetChartsRequestFilterEntity,
        start_ts: typing.Optional[str] = None,
        end_ts: typing.Optional[str] = None,
        filter_query: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetChartsResponse:
        """
        List charts for a given Application based on parameters passed in the query.

        Parameters
        ----------
        workspace_id : str

        application_id : str

        filter_entity : MetricsGetChartsRequestFilterEntity

        start_ts : typing.Optional[str]
            Start Timestamp

        end_ts : typing.Optional[str]
            End Timestamp

        filter_query : typing.Optional[str]
            Query params to filter metrics

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChartsResponse
            Charts have been successfully retrieved.

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry
        from truefoundry_sdk.internal.metrics import MetricsGetChartsRequestFilterEntity

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.metrics.get_charts(
                workspace_id="workspaceId",
                application_id="applicationId",
                filter_entity=MetricsGetChartsRequestFilterEntity.APPLICATION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_charts(
            workspace_id,
            application_id=application_id,
            filter_entity=filter_entity,
            start_ts=start_ts,
            end_ts=end_ts,
            filter_query=filter_query,
            request_options=request_options,
        )
        return _response.data
