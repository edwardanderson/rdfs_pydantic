"""RDFS Pydantic - Create Pydantic models from RDFS ontologies."""

from .module_generator import create_module
from .package_generator import create_package

__all__ = ["create_module", "create_package"]
