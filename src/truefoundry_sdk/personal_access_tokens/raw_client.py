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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..types.create_personal_access_token_response import CreatePersonalAccessTokenResponse
from ..types.delete_personal_access_token_response import DeletePersonalAccessTokenResponse
from ..types.http_error import HttpError
from ..types.list_personal_access_token_response import ListPersonalAccessTokenResponse
from ..types.virtual_account import VirtualAccount

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawPersonalAccessTokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            "api/svc/v1/personal-access-tokens",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListPersonalAccessTokenResponse,
                    parse_obj_as(
                        type_=ListPersonalAccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = True
                _get_next = lambda: self.list(
                    limit=limit,
                    offset=offset + len(_items),
                    request_options=request_options,
                )
                return SyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreatePersonalAccessTokenResponse]:
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
        HttpResponse[CreatePersonalAccessTokenResponse]
            Personal Access Token created successfully and returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/svc/v1/personal-access-tokens",
            method="POST",
            json={
                "name": name,
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
                    CreatePersonalAccessTokenResponse,
                    parse_obj_as(
                        type_=CreatePersonalAccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
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
    ) -> HttpResponse[DeletePersonalAccessTokenResponse]:
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
        HttpResponse[DeletePersonalAccessTokenResponse]
            Personal Access Token deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/svc/v1/personal-access-tokens/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePersonalAccessTokenResponse,
                    parse_obj_as(
                        type_=DeletePersonalAccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawPersonalAccessTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            "api/svc/v1/personal-access-tokens",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListPersonalAccessTokenResponse,
                    parse_obj_as(
                        type_=ListPersonalAccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = True

                async def _get_next():
                    return await self.list(
                        limit=limit,
                        offset=offset + len(_items),
                        request_options=request_options,
                    )

                return AsyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreatePersonalAccessTokenResponse]:
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
        AsyncHttpResponse[CreatePersonalAccessTokenResponse]
            Personal Access Token created successfully and returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/svc/v1/personal-access-tokens",
            method="POST",
            json={
                "name": name,
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
                    CreatePersonalAccessTokenResponse,
                    parse_obj_as(
                        type_=CreatePersonalAccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
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
    ) -> AsyncHttpResponse[DeletePersonalAccessTokenResponse]:
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
        AsyncHttpResponse[DeletePersonalAccessTokenResponse]
            Personal Access Token deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/svc/v1/personal-access-tokens/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeletePersonalAccessTokenResponse,
                    parse_obj_as(
                        type_=DeletePersonalAccessTokenResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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
