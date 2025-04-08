from typing import Optional, Protocol, TypeVar

from truefoundry_sdk.core.api_error import ApiError
from truefoundry_sdk.core.pagination import AsyncPager, SyncPager

T = TypeVar("T")

class HasListMethod(Protocol[T]):
    def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs) -> SyncPager[T]:
        ...


class HasAsyncListMethod(Protocol[T]):
    async def list(self, *, fqn: str, limit: Optional[int] = None, **kwargs) -> AsyncPager[T]:
        ...

def get_by_fqn(client: HasListMethod[T], *, fqn: str) -> T:
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


async def aget_by_fqn(client: HasAsyncListMethod[T], *, fqn: str) -> T:
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
