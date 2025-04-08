from typing import Any, Optional, Protocol, TypeVar

from pydantic import BaseModel

from truefoundry_sdk.core.api_error import ApiError
from truefoundry_sdk.core.pagination import AsyncPager, SyncPager
from truefoundry_sdk.v1.prompt_versions.client import PromptVersionsClient, AsyncPromptVersionsClient
from truefoundry_sdk.types.get_prompt_version_response import GetPromptVersionResponse

T = TypeVar("T", bound=BaseModel)

class HasListMethod(Protocol[T]):
    def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs: Any) -> SyncPager[T]:
        ...


class HasAsyncListMethod(Protocol[T]):
    async def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs) -> AsyncPager[T]:
        ...


def _get_by_fqn(client: HasListMethod[T], *, fqn: str) -> T:
    result = None
    for item in client.list(fqn=fqn, limit=1):
        result = item
        break
    if not result:
        raise ApiError(
            body=f"No entity found with fqn {fqn}",
            status_code=404,
        )
    return result


async def _aget_by_fqn(client: HasAsyncListMethod[T], *, fqn: str) -> T:
    result = None
    pager = await client.list(fqn=fqn, limit=1)
    async for item in pager:
        result = item
        break
    
    if not result:
        raise ApiError(
            body=f"No entity found with fqn {fqn}",
            status_code=404,
        )
    return result


class WrappedPromptVersionsClient(PromptVersionsClient):
    def get_by_fqn(self, *, fqn: str) -> GetPromptVersionResponse:
        item = _get_by_fqn(self, fqn=fqn)
        return GetPromptVersionResponse.model_validate({"data": item})


class WrappedAsyncPromptVersionsClient(AsyncPromptVersionsClient):
    async def get_by_fqn(self, *, fqn: str) -> GetPromptVersionResponse:
        item = await _aget_by_fqn(self, fqn=fqn)
        return GetPromptVersionResponse.model_validate({"data": item})
