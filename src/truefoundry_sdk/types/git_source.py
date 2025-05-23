# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GitSource(UniversalBaseModel):
    """
    +docs=Describes that we are using code stored in a git repository to build our image
    +label=Git Source
    +icon=fa-solid fa-code-branch:black
    +sort=300
    """

    type: typing.Literal["git"] = pydantic.Field(default="git")
    """
    +value=git
    """

    repo_url: str = pydantic.Field()
    """
    +label=Repo URL
    +usage=The repository URL.
    +sort=1
    +message=Needs to be a valid Github, Bitbucket, Azure Repos or Gitlab link
    """

    ref: str = pydantic.Field()
    """
    +label=Commit SHA
    +usage=The commit SHA.
    +sort=2
    """

    branch_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    +label=Branch Name
    +usage=Selecting branch will select latest commit SHA of the branch.
    +sort=3
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow")  # type: ignore # Pydantic v2
    else:

        class Config:
            smart_union = True
            extra = pydantic.Extra.allow
