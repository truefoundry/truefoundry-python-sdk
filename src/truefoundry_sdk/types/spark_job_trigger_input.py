# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SparkJobTriggerInput(UniversalBaseModel):
    main_class: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="mainClass")] = pydantic.Field(
        default=None
    )
    """
    Main Class for Spark Job
    """

    main_application_file: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mainApplicationFile")
    ] = pydantic.Field(default=None)
    """
    Main Application File for Spark Job
    """

    arguments: typing.Optional[str] = pydantic.Field(default=None)
    """
    Arguments to pass to the main application file
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
