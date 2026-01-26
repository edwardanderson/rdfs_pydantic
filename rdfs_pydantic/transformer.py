"""RDFS to Pydantic transformation - delegates to specialized modules."""

from .model_generator import create_model
from .package_generator import create_package

__all__ = ["create_model", "create_package"]
