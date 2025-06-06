# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .subject import Subject


class SecretGroup(UniversalBaseModel):
    id: typing.Optional[str] = None
    fqn: typing.Optional[str] = None
    name: str
    tenant_name: typing_extensions.Annotated[str, FieldMetadata(alias="tenantName")]
    created_by_subject: typing_extensions.Annotated[Subject, FieldMetadata(alias="createdBySubject")]
    associated_secrets: typing_extensions.Annotated[typing.List["Secret"], FieldMetadata(alias="associatedSecrets")]
    integration_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="integrationId")] = None
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]
    created_by: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="createdBy")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow


from .secret import Secret  # noqa: E402, F401, I001
from .secret_version import SecretVersion  # noqa: E402, F401, I001

update_forward_refs(SecretGroup)
