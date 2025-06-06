# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class MimeType(str, enum.Enum):
    """
    MIME type of the content
    """

    TEXT_PLAIN = "text/plain"
    APPLICATION_JSON = "application/json"
    IMAGE_PNG = "image/png"
    IMAGE_JPEG = "image/jpeg"
    APPLICATION_X_DIRECTORY = "application/x-directory"

    def visit(
        self,
        text_plain: typing.Callable[[], T_Result],
        application_json: typing.Callable[[], T_Result],
        image_png: typing.Callable[[], T_Result],
        image_jpeg: typing.Callable[[], T_Result],
        application_x_directory: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MimeType.TEXT_PLAIN:
            return text_plain()
        if self is MimeType.APPLICATION_JSON:
            return application_json()
        if self is MimeType.IMAGE_PNG:
            return image_png()
        if self is MimeType.IMAGE_JPEG:
            return image_jpeg()
        if self is MimeType.APPLICATION_X_DIRECTORY:
            return application_x_directory()
