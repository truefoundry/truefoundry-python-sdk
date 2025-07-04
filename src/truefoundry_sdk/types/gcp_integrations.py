# This file was auto-generated by Fern from our API Definition.

import typing

from .gcp_gcr import GcpGcr
from .gcp_gcs import GcpGcs
from .gcp_gke_integration import GcpGkeIntegration
from .gcp_gsm import GcpGsm
from .google_model import GoogleModel
from .vertex_model import VertexModel

GcpIntegrations = typing.Union[GcpGcr, GcpGcs, GcpGsm, GcpGkeIntegration, VertexModel, GoogleModel]
