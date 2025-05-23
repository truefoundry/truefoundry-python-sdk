# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SparkJobScalaEntrypoint(UniversalBaseModel):
    """
    +label=scala
    """

    type: typing.Literal["scala"] = pydantic.Field(default="scala")
    """
    +value=scala
    """

    main_application_file: str = pydantic.Field()
    """
    +label=Main Application File
    +usage=The main application file to be executed by the spark job.
    +message=Filename should have .jar extension
    +sort=5
    +placeholder=For example: local:///path/to/file.jar, s3:///bucket/path/to/file.jar, etc.
    """

    main_class: str = pydantic.Field()
    """
    +label=Main Class
    +usage=The main class to be executed by the spark job.
    +sort=6
    +required=true
    +message=The main class must be a valid Java class name.
    """

    arguments: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Arguments
    +usage=Arguments to be passed to the main application file.
    +sort=7
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
