# This file was auto-generated by Fern from our API Definition.

import typing

from .flyte_launch_plan import FlyteLaunchPlan
from .flyte_task import FlyteTask
from .flyte_workflow import FlyteWorkflow

WorkflowFlyteEntitiesItem = typing.Union[FlyteTask, FlyteWorkflow, FlyteLaunchPlan]
