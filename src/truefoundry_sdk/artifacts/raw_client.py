# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pagination import AsyncPager, BaseHttpResponse, SyncPager
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.artifact import Artifact
from ..types.artifact_manifest import ArtifactManifest
from ..types.empty_response import EmptyResponse
from ..types.get_artifact_response import GetArtifactResponse
from ..types.get_artifact_version_response import GetArtifactVersionResponse
from ..types.list_artifacts_response import ListArtifactsResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawArtifactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetArtifactResponse]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetArtifactResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/v1/artifacts/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetArtifactResponse,
                    parse_obj_as(
                        type_=GetArtifactResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/v1/artifacts/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> SyncPager[Artifact]:
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
        SyncPager[Artifact]
            Successful Response
        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "api/ml/v1/artifacts",
            method="GET",
            params={
                "fqn": fqn,
                "ml_repo_id": ml_repo_id,
                "name": name,
                "offset": offset,
                "limit": limit,
                "run_id": run_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListArtifactsResponse,
                    parse_obj_as(
                        type_=ListArtifactsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = True
                _get_next = lambda: self.list(
                    fqn=fqn,
                    ml_repo_id=ml_repo_id,
                    name=name,
                    offset=offset + len(_items),
                    limit=limit,
                    run_id=run_id,
                    request_options=request_options,
                )
                return SyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_or_update(
        self, *, manifest: ArtifactManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetArtifactVersionResponse]:
        """
        Parameters
        ----------
        manifest : ArtifactManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetArtifactVersionResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ml/v1/artifact-versions",
            method="PUT",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=ArtifactManifest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetArtifactVersionResponse,
                    parse_obj_as(
                        type_=GetArtifactVersionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawArtifactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetArtifactResponse]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetArtifactResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/v1/artifacts/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetArtifactResponse,
                    parse_obj_as(
                        type_=GetArtifactResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/v1/artifacts/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncPager[Artifact]:
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
        AsyncPager[Artifact]
            Successful Response
        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "api/ml/v1/artifacts",
            method="GET",
            params={
                "fqn": fqn,
                "ml_repo_id": ml_repo_id,
                "name": name,
                "offset": offset,
                "limit": limit,
                "run_id": run_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListArtifactsResponse,
                    parse_obj_as(
                        type_=ListArtifactsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = True

                async def _get_next():
                    return await self.list(
                        fqn=fqn,
                        ml_repo_id=ml_repo_id,
                        name=name,
                        offset=offset + len(_items),
                        limit=limit,
                        run_id=run_id,
                        request_options=request_options,
                    )

                return AsyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_or_update(
        self, *, manifest: ArtifactManifest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetArtifactVersionResponse]:
        """
        Parameters
        ----------
        manifest : ArtifactManifest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetArtifactVersionResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ml/v1/artifact-versions",
            method="PUT",
            json={
                "manifest": convert_and_respect_annotation_metadata(
                    object_=manifest, annotation=ArtifactManifest, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetArtifactVersionResponse,
                    parse_obj_as(
                        type_=GetArtifactVersionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
