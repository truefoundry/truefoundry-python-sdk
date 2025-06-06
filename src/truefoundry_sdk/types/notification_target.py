# This file was auto-generated by Fern from our API Definition.

import typing

from .email import Email
from .slack_bot import SlackBot
from .slack_webhook import SlackWebhook

NotificationTarget = typing.Union[Email, SlackWebhook, SlackBot]
