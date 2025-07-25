# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_auth import McpServerAuth


class McpServerIntegration(UniversalBaseModel):
    """
    +label=MCP Server
    +icon=puzzle-piece
    """

    type: typing.Literal["integration/mcp-server/hosted-mcp-server"] = pydantic.Field(
        default="integration/mcp-server/hosted-mcp-server"
    )
    """
    +value=integration/mcp-server/hosted-mcp-server
    """

    name: str = pydantic.Field()
    """
    +label=Name
    +usage=The name of the MCP Server.
    +sort=100
    """

    description: str = pydantic.Field()
    """
    +label=Description
    +usage=Provide a brief description of the purpose of this MCP Server.
    +uiType=TextArea
    +message=1 to 1000 characters long, may contain any character except newlines
    +sort=200
    +uiProps={"descriptionInline":true}
    """

    url: str = pydantic.Field()
    """
    +label=URL
    +usage=The endpoint URL for the MCP Server. The system will first try a connection using streamable-http transport on this URL. If that fails, it will attempt a connection using SSE transport on <url>/sse.
    +sort=300
    """

    auth_data: typing.Optional[McpServerAuth] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
