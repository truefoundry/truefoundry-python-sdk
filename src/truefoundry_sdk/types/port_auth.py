# This file was auto-generated by Fern from our API Definition.

import typing

from .basic_auth_creds import BasicAuthCreds
from .jwt_auth_config import JwtAuthConfig
from .true_foundry_interactive_login import TrueFoundryInteractiveLogin

PortAuth = typing.Union[BasicAuthCreds, JwtAuthConfig, TrueFoundryInteractiveLogin]
