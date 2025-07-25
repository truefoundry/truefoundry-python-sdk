# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .aws_parameter_store_auth_data import AwsParameterStoreAuthData
from .aws_region import AwsRegion


class AwsParameterStore(UniversalBaseModel):
    """
    +label=AWS Parameter Store
    +icon=aws-ssm
    """

    type: typing.Literal["integration/secret-store/aws/parameter-store"] = pydantic.Field(
        default="integration/secret-store/aws/parameter-store"
    )
    """
    +value=integration/secret-store/aws/parameter-store
    """

    name: str = pydantic.Field()
    """
    +label=Display Name
    +usage=The name of the integration that will be displayed in the TrueFoundry UI.
    +sort=150
    +message=3 to 32 lower case characters long alphanumeric word, may contain - in between, cannot start with a number
    """

    region: AwsRegion
    auth_data: typing.Optional[AwsParameterStoreAuthData] = pydantic.Field(default=None)
    """
    +label=Auth Data
    +usage=Custom authentication data for the integration.
    +sort=300
    """

    authorized_subjects: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    +label=Access Control
    +usage=List of subjects that are authorized to access this integration. List of user fqn in format <user_type>:<username>.
    +sort=600
    +uiType=AuthorizedSubjects
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
