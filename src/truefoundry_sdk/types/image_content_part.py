# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .image_url import ImageUrl


class ImageContentPart(UniversalBaseModel):
    """
    Image content for the message
    """

    type: typing.Literal["image_url"] = pydantic.Field(default="image_url")
    """
    Type of the content part
    """

    image_url: ImageUrl = pydantic.Field()
    """
    Image URL linking to the image
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
