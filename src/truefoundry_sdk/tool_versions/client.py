# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.empty_response import EmptyResponse
from ..types.get_tool_version_response import GetToolVersionResponse
from ..types.tool_version import ToolVersion
from .raw_client import AsyncRawToolVersionsClient, RawToolVersionsClient


class ToolVersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawToolVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawToolVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawToolVersionsClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetToolVersionResponse:
        """
        Get tool version API

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToolVersionResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tool_versions.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Delete tool versions API

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.tool_versions.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        fqn: typing.Optional[str] = None,
        tool_id: typing.Optional[str] = None,
        ml_repo_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        limit: typing.Optional[int] = 100,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ToolVersion]:
        """
        List tool versions API

        Parameters
        ----------
        fqn : typing.Optional[str]

        tool_id : typing.Optional[str]

        ml_repo_id : typing.Optional[str]

        name : typing.Optional[str]

        version : typing.Optional[int]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ToolVersion]
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.tool_versions.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            fqn=fqn,
            tool_id=tool_id,
            ml_repo_id=ml_repo_id,
            name=name,
            version=version,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )


class AsyncToolVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawToolVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawToolVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawToolVersionsClient
        """
        return self._raw_client

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetToolVersionResponse:
        """
        Get tool version API

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetToolVersionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tool_versions.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Delete tool versions API

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful Response

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.tool_versions.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def list(
        self,
        *,
        fqn: typing.Optional[str] = None,
        tool_id: typing.Optional[str] = None,
        ml_repo_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        offset: typing.Optional[int] = 0,
        limit: typing.Optional[int] = 100,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ToolVersion]:
        """
        List tool versions API

        Parameters
        ----------
        fqn : typing.Optional[str]

        tool_id : typing.Optional[str]

        ml_repo_id : typing.Optional[str]

        name : typing.Optional[str]

        version : typing.Optional[int]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ToolVersion]
            Successful Response

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.tool_versions.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            fqn=fqn,
            tool_id=tool_id,
            ml_repo_id=ml_repo_id,
            name=name,
            version=version,
            offset=offset,
            limit=limit,
            request_options=request_options,
        )
