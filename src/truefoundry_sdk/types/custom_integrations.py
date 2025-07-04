# This file was auto-generated by Fern from our API Definition.

import typing

from .custom_blob_storage import CustomBlobStorage
from .custom_helm_repo import CustomHelmRepo
from .custom_jwt_auth_integration import CustomJwtAuthIntegration
from .custom_mcp_server_integration import CustomMcpServerIntegration
from .custom_model import CustomModel
from .custom_username_password_artifacts_registry import CustomUsernamePasswordArtifactsRegistry
from .email_notification_channel import EmailNotificationChannel

CustomIntegrations = typing.Union[
    CustomUsernamePasswordArtifactsRegistry,
    CustomModel,
    EmailNotificationChannel,
    CustomHelmRepo,
    CustomBlobStorage,
    CustomJwtAuthIntegration,
    CustomMcpServerIntegration,
]
