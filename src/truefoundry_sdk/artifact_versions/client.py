# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.pagination import AsyncPager, SyncPager
from ..core.request_options import RequestOptions
from ..types.artifact_version import ArtifactVersion
from ..types.empty_response import EmptyResponse
from ..types.file_info import FileInfo
from ..types.get_artifact_version_response import GetArtifactVersionResponse
from ..types.get_signed_ur_ls_response import GetSignedUrLsResponse
from ..types.multi_part_upload_response import MultiPartUploadResponse
from ..types.operation import Operation
from ..types.stage_artifact_response import StageArtifactResponse
from .raw_client import AsyncRawArtifactVersionsClient, RawArtifactVersionsClient
from .types.stage_artifact_request_manifest import StageArtifactRequestManifest

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ArtifactVersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArtifactVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArtifactVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArtifactVersionsClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetArtifactVersionResponse:
        """
        Get artifact version API

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArtifactVersionResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifact_versions.get(
            id="id",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Delete artifact versions API

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
        client.artifact_versions.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def list(
        self,
        *,
        fqn: typing.Optional[str] = None,
        artifact_id: typing.Optional[str] = None,
        ml_repo_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        run_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        run_steps: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        offset: typing.Optional[int] = 0,
        limit: typing.Optional[int] = 100,
        include_internal_metadata: typing.Optional[bool] = False,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[ArtifactVersion]:
        """
        List artifact version API

        Parameters
        ----------
        fqn : typing.Optional[str]

        artifact_id : typing.Optional[str]

        ml_repo_id : typing.Optional[str]

        name : typing.Optional[str]

        version : typing.Optional[int]

        run_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        run_steps : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        include_internal_metadata : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[ArtifactVersion]
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.artifact_versions.list()
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list(
            fqn=fqn,
            artifact_id=artifact_id,
            ml_repo_id=ml_repo_id,
            name=name,
            version=version,
            run_ids=run_ids,
            run_steps=run_steps,
            offset=offset,
            limit=limit,
            include_internal_metadata=include_internal_metadata,
            request_options=request_options,
        )

    def get_signed_urls(
        self,
        *,
        id: str,
        paths: typing.Sequence[str],
        operation: Operation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSignedUrLsResponse:
        """
        Parameters
        ----------
        id : str

        paths : typing.Sequence[str]

        operation : Operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSignedUrLsResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import Operation, TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifact_versions.get_signed_urls(
            id="id",
            paths=["paths"],
            operation=Operation.READ,
        )
        """
        _response = self._raw_client.get_signed_urls(
            id=id, paths=paths, operation=operation, request_options=request_options
        )
        return _response.data

    def create_multi_part_upload(
        self, *, id: str, path: str, num_parts: int, request_options: typing.Optional[RequestOptions] = None
    ) -> MultiPartUploadResponse:
        """
        Parameters
        ----------
        id : str

        path : str

        num_parts : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPartUploadResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifact_versions.create_multi_part_upload(
            id="id",
            path="path",
            num_parts=1,
        )
        """
        _response = self._raw_client.create_multi_part_upload(
            id=id, path=path, num_parts=num_parts, request_options=request_options
        )
        return _response.data

    def stage(
        self, *, manifest: StageArtifactRequestManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> StageArtifactResponse:
        """
        Parameters
        ----------
        manifest : StageArtifactRequestManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageArtifactResponse
            Successful Response

        Examples
        --------
        from truefoundry_sdk import ModelManifest, TrueFoundry, TrueFoundryManagedSource

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artifact_versions.stage(
            manifest=ModelManifest(
                name="name",
                metadata={"key": "value"},
                ml_repo="ml_repo",
                source=TrueFoundryManagedSource(),
            ),
        )
        """
        _response = self._raw_client.stage(manifest=manifest, request_options=request_options)
        return _response.data

    def list_files(
        self,
        *,
        id: str,
        path: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[FileInfo]:
        """
        Parameters
        ----------
        id : str

        path : typing.Optional[str]

        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[FileInfo]
            Successful Response

        Examples
        --------
        from truefoundry_sdk import TrueFoundry

        client = TrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        response = client.artifact_versions.list_files(
            id="id",
        )
        for item in response:
            yield item
        # alternatively, you can paginate page-by-page
        for page in response.iter_pages():
            yield page
        """
        return self._raw_client.list_files(
            id=id, path=path, limit=limit, page_token=page_token, request_options=request_options
        )

    def mark_stage_failure(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
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
        client.artifact_versions.mark_stage_failure(
            id="id",
        )
        """
        _response = self._raw_client.mark_stage_failure(id=id, request_options=request_options)
        return _response.data


class AsyncArtifactVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArtifactVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArtifactVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArtifactVersionsClient
        """
        return self._raw_client

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetArtifactVersionResponse:
        """
        Get artifact version API

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetArtifactVersionResponse
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
            await client.artifact_versions.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> EmptyResponse:
        """
        Delete artifact versions API

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
            await client.artifact_versions.delete(
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
        artifact_id: typing.Optional[str] = None,
        ml_repo_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        run_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        run_steps: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        offset: typing.Optional[int] = 0,
        limit: typing.Optional[int] = 100,
        include_internal_metadata: typing.Optional[bool] = False,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[ArtifactVersion]:
        """
        List artifact version API

        Parameters
        ----------
        fqn : typing.Optional[str]

        artifact_id : typing.Optional[str]

        ml_repo_id : typing.Optional[str]

        name : typing.Optional[str]

        version : typing.Optional[int]

        run_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        run_steps : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        include_internal_metadata : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[ArtifactVersion]
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
            response = await client.artifact_versions.list()
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list(
            fqn=fqn,
            artifact_id=artifact_id,
            ml_repo_id=ml_repo_id,
            name=name,
            version=version,
            run_ids=run_ids,
            run_steps=run_steps,
            offset=offset,
            limit=limit,
            include_internal_metadata=include_internal_metadata,
            request_options=request_options,
        )

    async def get_signed_urls(
        self,
        *,
        id: str,
        paths: typing.Sequence[str],
        operation: Operation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSignedUrLsResponse:
        """
        Parameters
        ----------
        id : str

        paths : typing.Sequence[str]

        operation : Operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSignedUrLsResponse
            Successful Response

        Examples
        --------
        import asyncio

        from truefoundry_sdk import AsyncTrueFoundry, Operation

        client = AsyncTrueFoundry(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artifact_versions.get_signed_urls(
                id="id",
                paths=["paths"],
                operation=Operation.READ,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_signed_urls(
            id=id, paths=paths, operation=operation, request_options=request_options
        )
        return _response.data

    async def create_multi_part_upload(
        self, *, id: str, path: str, num_parts: int, request_options: typing.Optional[RequestOptions] = None
    ) -> MultiPartUploadResponse:
        """
        Parameters
        ----------
        id : str

        path : str

        num_parts : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPartUploadResponse
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
            await client.artifact_versions.create_multi_part_upload(
                id="id",
                path="path",
                num_parts=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_multi_part_upload(
            id=id, path=path, num_parts=num_parts, request_options=request_options
        )
        return _response.data

    async def stage(
        self, *, manifest: StageArtifactRequestManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> StageArtifactResponse:
        """
        Parameters
        ----------
        manifest : StageArtifactRequestManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageArtifactResponse
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
            await client.artifact_versions.stage(
                manifest=ModelManifest(
                    name="name",
                    metadata={"key": "value"},
                    ml_repo="ml_repo",
                    source=TrueFoundryManagedSource(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stage(manifest=manifest, request_options=request_options)
        return _response.data

    async def list_files(
        self,
        *,
        id: str,
        path: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        page_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[FileInfo]:
        """
        Parameters
        ----------
        id : str

        path : typing.Optional[str]

        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[FileInfo]
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
            response = await client.artifact_versions.list_files(
                id="id",
            )
            async for item in response:
                yield item

            # alternatively, you can paginate page-by-page
            async for page in response.iter_pages():
                yield page


        asyncio.run(main())
        """
        return await self._raw_client.list_files(
            id=id, path=path, limit=limit, page_token=page_token, request_options=request_options
        )

    async def mark_stage_failure(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
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
            await client.artifact_versions.mark_stage_failure(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_stage_failure(id=id, request_options=request_options)
        return _response.data
