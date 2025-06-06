# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_events_response import GetEventsResponse
from .raw_client import AsyncRawEventsClient, RawEventsClient


class EventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEventsClient
        """
        return self._raw_client

    def get(
        self,
        *,
        start_ts: typing.Optional[str] = None,
        end_ts: typing.Optional[str] = None,
        application_id: typing.Optional[str] = None,
        application_fqn: typing.Optional[str] = None,
        pod_names: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        job_run_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEventsResponse:
        """
        Get Events for Pod, Job Run, Application. The events are sourced from Kubernetes as well as events captured by truefoundry. Optional query parameters include startTs, endTs for filtering.

        Parameters
        ----------
        start_ts : typing.Optional[str]
            Start timestamp (ISO format) for querying events

        end_ts : typing.Optional[str]
            End timestamp (ISO format) for querying events

        application_id : typing.Optional[str]
            Application ID

        application_fqn : typing.Optional[str]
            Application FQN

        pod_names : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Name of the pods

        job_run_name : typing.Optional[str]
            Job run name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsResponse
            Returns a list of events matching the query parameters.

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.events.get()
        """
        _response = self._raw_client.get(
            start_ts=start_ts,
            end_ts=end_ts,
            application_id=application_id,
            application_fqn=application_fqn,
            pod_names=pod_names,
            job_run_name=job_run_name,
            request_options=request_options,
        )
        return _response.data


class AsyncEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEventsClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        start_ts: typing.Optional[str] = None,
        end_ts: typing.Optional[str] = None,
        application_id: typing.Optional[str] = None,
        application_fqn: typing.Optional[str] = None,
        pod_names: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        job_run_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetEventsResponse:
        """
        Get Events for Pod, Job Run, Application. The events are sourced from Kubernetes as well as events captured by truefoundry. Optional query parameters include startTs, endTs for filtering.

        Parameters
        ----------
        start_ts : typing.Optional[str]
            Start timestamp (ISO format) for querying events

        end_ts : typing.Optional[str]
            End timestamp (ISO format) for querying events

        application_id : typing.Optional[str]
            Application ID

        application_fqn : typing.Optional[str]
            Application FQN

        pod_names : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Name of the pods

        job_run_name : typing.Optional[str]
            Job run name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEventsResponse
            Returns a list of events matching the query parameters.

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.events.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            start_ts=start_ts,
            end_ts=end_ts,
            application_id=application_id,
            application_fqn=application_fqn,
            pod_names=pod_names,
            job_run_name=job_run_name,
            request_options=request_options,
        )
        return _response.data
