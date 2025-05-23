# This file was auto-generated by Fern from our API Definition.

import typing

from .agent_version import AgentVersion
from .artifact_version import ArtifactVersion
from .data_directory import DataDirectory
from .model_version import ModelVersion
from .prompt_version import PromptVersion
from .tool_version import ToolVersion
from .tracing_project import TracingProject

ApplyMlEntityResponseData = typing.Union[
    ModelVersion, PromptVersion, ToolVersion, AgentVersion, ArtifactVersion, DataDirectory, TracingProject
]
