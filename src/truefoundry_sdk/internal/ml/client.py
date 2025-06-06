# This file was auto-generated by Fern from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.apply_ml_entity_response import ApplyMlEntityResponse
from ...types.empty_response import EmptyResponse
from .raw_client import AsyncRawMlClient, RawMlClient
from .types.apply_ml_entity_request_manifest import ApplyMlEntityRequestManifest
from .types.delete_ml_entity_request_manifest import DeleteMlEntityRequestManifest

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMlClient
        """
        return self._raw_client

    def apply(
        self, *, manifest: ApplyMlEntityRequestManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplyMlEntityResponse:
        """
        Parameters
        ----------
        manifest : ApplyMlEntityRequestManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplyMlEntityResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.ml.apply(
            manifest=ModelManifest(
                name="name",
                metadata={"key": "value"},
                ml_repo="ml_repo",
                source=TrueFoundryManagedSource(),
            ),
        )
        """
        _response = self._raw_client.apply(manifest=manifest, request_options=request_options)
        return _response.data

    def delete(
        self, *, manifest: DeleteMlEntityRequestManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Parameters
        ----------
        manifest : DeleteMlEntityRequestManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.ml.delete(
            manifest=ModelManifest(
                name="name",
                metadata={"key": "value"},
                ml_repo="ml_repo",
                source=TrueFoundryManagedSource(),
            ),
        )
        """
        _response = self._raw_client.delete(manifest=manifest, request_options=request_options)
        return _response.data


class AsyncMlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMlClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMlClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMlClient
        """
        return self._raw_client

    async def apply(
        self, *, manifest: ApplyMlEntityRequestManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplyMlEntityResponse:
        """
        Parameters
        ----------
        manifest : ApplyMlEntityRequestManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplyMlEntityResponse
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
            await client.internal.ml.apply(
                manifest=ModelManifest(
                    name="name",
                    metadata={"key": "value"},
                    ml_repo="ml_repo",
                    source=TrueFoundryManagedSource(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.apply(manifest=manifest, request_options=request_options)
        return _response.data

    async def delete(
        self, *, manifest: DeleteMlEntityRequestManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Parameters
        ----------
        manifest : DeleteMlEntityRequestManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
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
            await client.internal.ml.delete(
                manifest=ModelManifest(
                    name="name",
                    metadata={"key": "value"},
                    ml_repo="ml_repo",
                    source=TrueFoundryManagedSource(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(manifest=manifest, request_options=request_options)
        return _response.data
