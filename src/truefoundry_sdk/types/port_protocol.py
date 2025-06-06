# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PortProtocol(str, enum.Enum):
    """
    +usage=Protocol for the port.
    """

    TCP = "TCP"
    UDP = "UDP"

    def visit(self, tcp: typing.Callable[[], T_Result], udp: typing.Callable[[], T_Result]) -> T_Result:
        if self is PortProtocol.TCP:
            return tcp()
        if self is PortProtocol.UDP:
            return udp()
