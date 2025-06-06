# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata


class SecretVersion(UniversalBaseModel):
    id: str
    fqn: str
    value: typing.Optional[str] = None
    version: typing.Optional[float] = None
    secret: typing.Optional["Secret"] = None
    secret_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="secretId")] = None
    created_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="createdAt")] = None
    updated_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="updatedAt")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


from .secret import Secret  # noqa: E402, F401, I001

update_forward_refs(SecretVersion)
