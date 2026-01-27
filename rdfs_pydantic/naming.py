"""Naming strategies for converting RDF IRIs to Python identifiers.

This module provides a strategy pattern for handling IRI-to-identifier conversion,
with support for JSON-LD context aliasing.
"""

from abc import ABC, abstractmethod
from .utils import sanitise_identifier
from .models import IriComponents


class NamingStrategy(ABC):
    """Abstract base class for IRI naming strategies."""

    @abstractmethod
    def get_local_name(self, iri: str) -> str:
        """Convert an IRI to a Python-safe identifier.
        
        Args:
            iri: The IRI string to convert
            
        Returns:
            A sanitized Python identifier
        """
        pass


class DefaultNamingStrategy(NamingStrategy):
    """Default strategy: extract local name from IRI by splitting on / or #."""

    def get_local_name(self, iri: str) -> str:
        """Extract local name from IRI using IriComponents parser.
        
        Args:
            iri: The IRI string
            
        Returns:
            Sanitized local name
        """
        components = IriComponents.parse(iri)
        return sanitise_identifier(components.local_name)


class ContextAwareNamingStrategy(NamingStrategy):
    """Strategy that uses JSON-LD context for aliasing, with default fallback."""

    def __init__(self, alias_map: dict[str, str]):
        """Initialize with a pre-built alias map.
        
        Args:
            alias_map: Mapping of IRI -> alias from JSON-LD contexts
        """
        self.alias_map = alias_map
        self._default_strategy = DefaultNamingStrategy()

    def get_local_name(self, iri: str) -> str:
        """Get local name using context alias if available, otherwise default logic.
        
        Args:
            iri: The IRI string
            
        Returns:
            Sanitized alias or local name
        """
        if iri in self.alias_map:
            return sanitise_identifier(self.alias_map[iri])
        return self._default_strategy.get_local_name(iri)
