# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.create_personal_access_token_response import CreatePersonalAccessTokenResponse
from ..types.delete_personal_access_token_response import DeletePersonalAccessTokenResponse
from ..types.virtual_account import VirtualAccount
from .raw_client import AsyncRawPersonalAccessTokensClient, RawPersonalAccessTokensClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PersonalAccessTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPersonalAccessTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPersonalAccessTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPersonalAccessTokensClient
        """
        return self._raw_client

    def list(
        self,
        *,
        limit: typing.Optional[int] = 100,
        offset: typing.Optional[int] = 0,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[VirtualAccount]:
        """
        List Personal Access Tokens created by the user in the current tenant.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of items per page

        offset : typing.Optional[int]
            Number of items to skip

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[VirtualAccount]
            Returns all Personal Access Tokens created by the user in the current tenant.

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.personal_access_tokens.list(
            limit=10,
            offset=0,
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(limit=limit, offset=offset, request_options=request_options)

    def create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatePersonalAccessTokenResponse:
        """
        Create Personal Access Token

        Parameters
        ----------
        name : str
            serviceaccount name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePersonalAccessTokenResponse
            Personal Access Token created successfully and returned

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.personal_access_tokens.create(
            name="name",
        )
        """
        _response = self._raw_client.create(name=name, request_options=request_options)
        return _response.data

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePersonalAccessTokenResponse:
        """
        Delete Personal Access Token associated with the provided serviceAccountId

        Parameters
        ----------
        id : str
            serviceaccount id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePersonalAccessTokenResponse
            Personal Access Token deleted successfully

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.personal_access_tokens.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data


class AsyncPersonalAccessTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPersonalAccessTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPersonalAccessTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPersonalAccessTokensClient
        """
        return self._raw_client

    async def list(
        self,
        *,
        limit: typing.Optional[int] = 100,
        offset: typing.Optional[int] = 0,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[VirtualAccount]:
        """
        List Personal Access Tokens created by the user in the current tenant.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of items per page

        offset : typing.Optional[int]
            Number of items to skip

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[VirtualAccount]
            Returns all Personal Access Tokens created by the user in the current tenant.

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            response = await client.personal_access_tokens.list(
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
        return await self._raw_client.list(limit=limit, offset=offset, request_options=request_options)

    async def create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CreatePersonalAccessTokenResponse:
        """
        Create Personal Access Token

        Parameters
        ----------
        name : str
            serviceaccount name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePersonalAccessTokenResponse
            Personal Access Token created successfully and returned

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.personal_access_tokens.create(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(name=name, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePersonalAccessTokenResponse:
        """
        Delete Personal Access Token associated with the provided serviceAccountId

        Parameters
        ----------
        id : str
            serviceaccount id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePersonalAccessTokenResponse
            Personal Access Token deleted successfully

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.personal_access_tokens.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data
