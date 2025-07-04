# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_auth import McpServerAuth


class CustomMcpServerIntegration(UniversalBaseModel):
    """
    +label=Custom MCP Server
    +icon=puzzle-piece
    """

    type: typing.Literal["integration/mcp-server/custom"] = pydantic.Field(default="integration/mcp-server/custom")
    """
    +value=integration/mcp-server/custom
    """

    name: str = pydantic.Field()
    """
    +label=Name
    +usage=The name of the integration that will be displayed in the TrueFoundry UI.
    +sort=100
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Description
    +uiType=TextArea
    +usage=The Description of the integration that will be displayed in the TrueFoundry UI.
    +sort=200
    +uiProps={"descriptionInline":true}
    """

    url: str = pydantic.Field()
    """
    +label=URL
    +usage=The endpoint URL for the MCP server.
    +sort=300
    """

    auth: typing.Optional[McpServerAuth] = None
    authorized_subjects: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    +label=Access Control
    +usage=List of subjects that are authorized to access this integration. List of user fqn in format <user_type>:<username>.
    +sort=500
    +uiType=AuthorizedSubjects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
