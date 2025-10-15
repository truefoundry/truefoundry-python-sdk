# Truefoundry Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Ftruefoundry%2Ftruefoundry-python-sdk)
[![pypi](https://img.shields.io/pypi/v/truefoundry-sdk)](https://pypi.python.org/pypi/truefoundry-sdk)

This library provides convenient access to the TrueFoundry API.

> [!tip]
> You can ask questions about this SDK using DeepWiki
> - Python: [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/truefoundry/truefoundry-python-sdk)
> - TypeScript: [![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/truefoundry/truefoundry-typescript-sdk)


## Installation

```sh
pip install truefoundry-sdk
```

## Reference

A full reference for this library is available [here](https://github.com/truefoundry/truefoundry-python-sdk/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from truefoundry_sdk import TrueFoundry
from truefoundry_sdk.applications import (
    ApplicationsListRequestDeviceTypeFilter,
    ApplicationsListRequestLifecycleStage,
)

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.applications.list(
    limit=10,
    offset=0,
    application_id="applicationId",
    workspace_id="workspaceId",
    application_name="applicationName",
    fqn="fqn",
    workspace_fqn="workspaceFqn",
    application_type="applicationType",
    name_search_query="nameSearchQuery",
    environment_id="environmentId",
    cluster_id="clusterId",
    application_set_id="applicationSetId",
    paused=True,
    device_type_filter=ApplicationsListRequestDeviceTypeFilter.CPU,
    last_deployed_by_subjects="lastDeployedBySubjects",
    lifecycle_stage=ApplicationsListRequestLifecycleStage.ACTIVE,
    is_recommendation_present_and_visible=True,
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API. Note that if you are constructing an Async httpx client class to pass into this client, use `httpx.AsyncClient()` instead of `httpx.Client()` (e.g. for the `httpx_client` parameter of this client).

```python
import asyncio

from truefoundry_sdk import AsyncTrueFoundry
from truefoundry_sdk.applications import (
    ApplicationsListRequestDeviceTypeFilter,
    ApplicationsListRequestLifecycleStage,
)

client = AsyncTrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)


async def main() -> None:
    response = await client.applications.list(
        limit=10,
        offset=0,
        application_id="applicationId",
        workspace_id="workspaceId",
        application_name="applicationName",
        fqn="fqn",
        workspace_fqn="workspaceFqn",
        application_type="applicationType",
        name_search_query="nameSearchQuery",
        environment_id="environmentId",
        cluster_id="clusterId",
        application_set_id="applicationSetId",
        paused=True,
        device_type_filter=ApplicationsListRequestDeviceTypeFilter.CPU,
        last_deployed_by_subjects="lastDeployedBySubjects",
        lifecycle_stage=ApplicationsListRequestLifecycleStage.ACTIVE,
        is_recommendation_present_and_visible=True,
    )
    async for item in response:
        yield item

    # alternatively, you can paginate page-by-page
    async for page in response.iter_pages():
        yield page


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from truefoundry_sdk.core.api_error import ApiError

try:
    client.applications.list(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    api_key="YOUR_API_KEY",
    base_url="https://yourhost.com/path/to/api",
)
response = client.users.list(
    limit=10,
    offset=0,
    query="query",
    show_invalid_users=True,
    include_virtual_accounts="includeVirtualAccounts",
)
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    ...,
)
response = client.applications.with_raw_response.list(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
pager = client.users.list(...)
print(pager.response.headers)  # access the response headers for the first page
for item in pager:
    print(item)  # access the underlying object(s)
for page in pager.iter_pages():
    print(page.response.headers)  # access the response headers for each page
    for item in page:
        print(item)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.applications.list(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.applications.list(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from truefoundry_sdk import TrueFoundry

client = TrueFoundry(
    ...,
    httpx_client=httpx.Client(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
