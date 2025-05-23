# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Email(UniversalBaseModel):
    """
    +label=Email
    """

    type: typing.Literal["email"] = pydantic.Field(default="email")
    """
    +value=email
    """

    notification_channel: str = pydantic.Field()
    """
    +label=Notification Channel
    +usage=Specify the notification channel to send alerts to
    +uiType=AlertNotificationChannel
    +uiProps={"integrationType":"notification-channel"}
    +sort=660
    """

    to_emails: typing.List[str] = pydantic.Field()
    """
    +label=To Emails
    +usage=List of recipients' email addresses if the notification channel is Email.
    +docs=Specify the emails to send alerts to
    +sort=665
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
