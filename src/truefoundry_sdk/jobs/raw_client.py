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
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.expectation_failed_error import ExpectationFailedError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.delete_job_run_response import DeleteJobRunResponse
from ..types.get_job_run_response import GetJobRunResponse
from ..types.http_error import HttpError
from ..types.job_run import JobRun
from ..types.job_run_status import JobRunStatus
from ..types.job_runs_sort_by import JobRunsSortBy
from ..types.job_runs_sort_direction import JobRunsSortDirection
from ..types.list_job_run_response import ListJobRunResponse
from ..types.terminate_job_response import TerminateJobResponse
from ..types.trigger_job_run_response import TriggerJobRunResponse
from .types.trigger_job_request_input import TriggerJobRequestInput

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawJobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_runs(
        self,
        job_id: str,
        *,
        limit: typing.Optional[int] = 100,
        offset: typing.Optional[int] = 0,
        search_prefix: typing.Optional[str] = None,
        sort_by: typing.Optional[JobRunsSortBy] = None,
        order: typing.Optional[JobRunsSortDirection] = None,
        triggered_by: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[typing.Union[JobRunStatus, typing.Sequence[JobRunStatus]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncPager[JobRun]:
        """
        List Job Runs for provided Job Id. Filter the data based on parameters passed in the query

        Parameters
        ----------
        job_id : str
            Job id of the application

        limit : typing.Optional[int]
            Number of items per page

        offset : typing.Optional[int]
            Number of items to skip

        search_prefix : typing.Optional[str]
            Prefix used to search for job runs by name or identifier

        sort_by : typing.Optional[JobRunsSortBy]
            Attribute to sort by

        order : typing.Optional[JobRunsSortDirection]
            Sorting order

        triggered_by : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of subject slugs

        status : typing.Optional[typing.Union[JobRunStatus, typing.Sequence[JobRunStatus]]]
            Status of the job run

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncPager[JobRun]
            Returns all runs of a Job sorted by creation date in "data" key and total count in "totalCount" key
        """
        offset = offset if offset is not None else 0

        _response = self._client_wrapper.httpx_client.request(
            f"api/svc/v1/jobs/{jsonable_encoder(job_id)}/runs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "searchPrefix": search_prefix,
                "sortBy": sort_by,
                "order": order,
                "triggeredBy": triggered_by,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListJobRunResponse,
                    parse_obj_as(
                        type_=ListJobRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = True
                _get_next = lambda: self.list_runs(
                    job_id,
                    limit=limit,
                    offset=offset + len(_items),
                    search_prefix=search_prefix,
                    sort_by=sort_by,
                    order=order,
                    triggered_by=triggered_by,
                    status=status,
                    request_options=request_options,
                )
                return SyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_run(
        self, job_id: str, job_run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetJobRunResponse]:
        """
        Get Job Run for provided jobRunName and jobId

        Parameters
        ----------
        job_id : str
            Application Id of JOB

        job_run_name : str
            Job run name of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetJobRunResponse]
            Return JobRun details of the provided jobRunName
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/svc/v1/jobs/{jsonable_encoder(job_id)}/runs/{jsonable_encoder(job_run_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJobRunResponse,
                    parse_obj_as(
                        type_=GetJobRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_run(
        self, job_id: str, job_run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteJobRunResponse]:
        """
        Delete Job Run for provided jobRunName and jobId

        Parameters
        ----------
        job_id : str
            Application Id of JOB

        job_run_name : str
            Job run name of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteJobRunResponse]
            Job Run deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/svc/v1/jobs/{jsonable_encoder(job_id)}/runs/{jsonable_encoder(job_run_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteJobRunResponse,
                    parse_obj_as(
                        type_=DeleteJobRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def trigger(
        self,
        *,
        deployment_id: typing.Optional[str] = OMIT,
        application_id: typing.Optional[str] = OMIT,
        input: typing.Optional[TriggerJobRequestInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TriggerJobRunResponse]:
        """
        Trigger Job for provided deploymentId or applicationId

        Parameters
        ----------
        deployment_id : typing.Optional[str]
            Deployment Id of the job

        application_id : typing.Optional[str]
            Application Id of the job

        input : typing.Optional[TriggerJobRequestInput]
            Job trigger input

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TriggerJobRunResponse]
            Returns object with message, JobRun Name And Job Details on successful creation of Job
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/svc/v1/jobs/trigger",
            method="POST",
            json={
                "deploymentId": deployment_id,
                "applicationId": application_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=TriggerJobRequestInput, direction="write"
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
                    TriggerJobRunResponse,
                    parse_obj_as(
                        type_=TriggerJobRunResponse,  # type: ignore
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def terminate(
        self, *, deployment_id: str, job_run_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TerminateJobResponse]:
        """
        Terminate Job for provided deploymentId and jobRunName

        Parameters
        ----------
        deployment_id : str
            Deployment Id of the Deployment

        job_run_name : str
            Job Run name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TerminateJobResponse]
            Returns object with message and JobRun Status on successful termination of Job
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/svc/v1/jobs/terminate",
            method="POST",
            params={
                "deploymentId": deployment_id,
                "jobRunName": job_run_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TerminateJobResponse,
                    parse_obj_as(
                        type_=TerminateJobResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 417:
                raise ExpectationFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
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


class AsyncRawJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_runs(
        self,
        job_id: str,
        *,
        limit: typing.Optional[int] = 100,
        offset: typing.Optional[int] = 0,
        search_prefix: typing.Optional[str] = None,
        sort_by: typing.Optional[JobRunsSortBy] = None,
        order: typing.Optional[JobRunsSortDirection] = None,
        triggered_by: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        status: typing.Optional[typing.Union[JobRunStatus, typing.Sequence[JobRunStatus]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncPager[JobRun]:
        """
        List Job Runs for provided Job Id. Filter the data based on parameters passed in the query

        Parameters
        ----------
        job_id : str
            Job id of the application

        limit : typing.Optional[int]
            Number of items per page

        offset : typing.Optional[int]
            Number of items to skip

        search_prefix : typing.Optional[str]
            Prefix used to search for job runs by name or identifier

        sort_by : typing.Optional[JobRunsSortBy]
            Attribute to sort by

        order : typing.Optional[JobRunsSortDirection]
            Sorting order

        triggered_by : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Array of subject slugs

        status : typing.Optional[typing.Union[JobRunStatus, typing.Sequence[JobRunStatus]]]
            Status of the job run

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncPager[JobRun]
            Returns all runs of a Job sorted by creation date in "data" key and total count in "totalCount" key
        """
        offset = offset if offset is not None else 0

        _response = await self._client_wrapper.httpx_client.request(
            f"api/svc/v1/jobs/{jsonable_encoder(job_id)}/runs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "searchPrefix": search_prefix,
                "sortBy": sort_by,
                "order": order,
                "triggeredBy": triggered_by,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _parsed_response = typing.cast(
                    ListJobRunResponse,
                    parse_obj_as(
                        type_=ListJobRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                _items = _parsed_response.data
                _has_next = True

                async def _get_next():
                    return await self.list_runs(
                        job_id,
                        limit=limit,
                        offset=offset + len(_items),
                        search_prefix=search_prefix,
                        sort_by=sort_by,
                        order=order,
                        triggered_by=triggered_by,
                        status=status,
                        request_options=request_options,
                    )

                return AsyncPager(
                    has_next=_has_next, items=_items, get_next=_get_next, response=BaseHttpResponse(response=_response)
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_run(
        self, job_id: str, job_run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetJobRunResponse]:
        """
        Get Job Run for provided jobRunName and jobId

        Parameters
        ----------
        job_id : str
            Application Id of JOB

        job_run_name : str
            Job run name of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetJobRunResponse]
            Return JobRun details of the provided jobRunName
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/svc/v1/jobs/{jsonable_encoder(job_id)}/runs/{jsonable_encoder(job_run_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetJobRunResponse,
                    parse_obj_as(
                        type_=GetJobRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_run(
        self, job_id: str, job_run_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteJobRunResponse]:
        """
        Delete Job Run for provided jobRunName and jobId

        Parameters
        ----------
        job_id : str
            Application Id of JOB

        job_run_name : str
            Job run name of the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteJobRunResponse]
            Job Run deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/svc/v1/jobs/{jsonable_encoder(job_id)}/runs/{jsonable_encoder(job_run_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteJobRunResponse,
                    parse_obj_as(
                        type_=DeleteJobRunResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def trigger(
        self,
        *,
        deployment_id: typing.Optional[str] = OMIT,
        application_id: typing.Optional[str] = OMIT,
        input: typing.Optional[TriggerJobRequestInput] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TriggerJobRunResponse]:
        """
        Trigger Job for provided deploymentId or applicationId

        Parameters
        ----------
        deployment_id : typing.Optional[str]
            Deployment Id of the job

        application_id : typing.Optional[str]
            Application Id of the job

        input : typing.Optional[TriggerJobRequestInput]
            Job trigger input

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TriggerJobRunResponse]
            Returns object with message, JobRun Name And Job Details on successful creation of Job
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/svc/v1/jobs/trigger",
            method="POST",
            json={
                "deploymentId": deployment_id,
                "applicationId": application_id,
                "input": convert_and_respect_annotation_metadata(
                    object_=input, annotation=TriggerJobRequestInput, direction="write"
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
                    TriggerJobRunResponse,
                    parse_obj_as(
                        type_=TriggerJobRunResponse,  # type: ignore
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
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def terminate(
        self, *, deployment_id: str, job_run_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TerminateJobResponse]:
        """
        Terminate Job for provided deploymentId and jobRunName

        Parameters
        ----------
        deployment_id : str
            Deployment Id of the Deployment

        job_run_name : str
            Job Run name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TerminateJobResponse]
            Returns object with message and JobRun Status on successful termination of Job
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/svc/v1/jobs/terminate",
            method="POST",
            params={
                "deploymentId": deployment_id,
                "jobRunName": job_run_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TerminateJobResponse,
                    parse_obj_as(
                        type_=TerminateJobResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
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
            if _response.status_code == 417:
                raise ExpectationFailedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpError,
                        parse_obj_as(
                            type_=HttpError,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
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
