# This file was auto-generated by Fern from our API Definition.

import typing

from .refusal_content_part import RefusalContentPart
from .text_content_part import TextContentPart

AssistantMessageContentItem = typing.Union[TextContentPart, RefusalContentPart]
