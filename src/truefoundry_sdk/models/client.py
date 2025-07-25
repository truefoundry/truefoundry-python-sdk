# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.empty_response import EmptyResponse
from ..types.get_model_response import GetModelResponse
from ..types.get_model_version_response import GetModelVersionResponse
from ..types.model import Model
from ..types.model_manifest import ModelManifest
from .raw_client import AsyncRawModelsClient, RawModelsClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawModelsClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetModelResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.models.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
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
        client.models.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        fqn: typing.Optional[str] = None,
        ml_repo_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        offset: typing.Optional[int] = 0,
        limit: typing.Optional[int] = 100,
        run_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[Model]:
        """
        Parameters
        ----------
        fqn : typing.Optional[str]

        ml_repo_id : typing.Optional[str]

        name : typing.Optional[str]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[Model]
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.models.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            fqn=fqn,
            ml_repo_id=ml_repo_id,
            name=name,
            offset=offset,
            limit=limit,
            run_id=run_id,
            request_options=request_options,
        )

    def create_or_update(
        self, *, manifest: ModelManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetModelVersionResponse:
        """
        Parameters
        ----------
        manifest : ModelManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelVersionResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.models.create_or_update(
            manifest=ModelManifest(
                name="name",
                metadata={"key": "value"},
                ml_repo="ml_repo",
                source=TrueFoundryManagedSource(),
            ),
        )
        """
        _response = self._raw_client.create_or_update(manifest=manifest, request_options=request_options)
        return _response.data


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawModelsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawModelsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawModelsClient
        """
        return self._raw_client

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetModelResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelResponse
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
            await client.models.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
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
            await client.models.delete(
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
        ml_repo_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        offset: typing.Optional[int] = 0,
        limit: typing.Optional[int] = 100,
        run_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[Model]:
        """
        Parameters
        ----------
        fqn : typing.Optional[str]

        ml_repo_id : typing.Optional[str]

        name : typing.Optional[str]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        run_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[Model]
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
            response = await client.models.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            fqn=fqn,
            ml_repo_id=ml_repo_id,
            name=name,
            offset=offset,
            limit=limit,
            run_id=run_id,
            request_options=request_options,
        )

    async def create_or_update(
        self, *, manifest: ModelManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> GetModelVersionResponse:
        """
        Parameters
        ----------
        manifest : ModelManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetModelVersionResponse
            Successful Response

        Examples
        --------
        import asyncio

        from truefoundry_sdk import (
            AsyncTrueFoundry,
            ModelManifest,
            TrueFoundryManagedSource,
        )

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.models.create_or_update(
                manifest=ModelManifest(
                    name="name",
                    metadata={"key": "value"},
                    ml_repo="ml_repo",
                    source=TrueFoundryManagedSource(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_update(manifest=manifest, request_options=request_options)
        return _response.data
