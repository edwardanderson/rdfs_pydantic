"""Generate Python code for Pydantic models."""

from typing import Optional
from pydantic import BaseModel


def generate_docstring(label: Optional[str], iri: Optional[str], comment: Optional[str], indent: str = "    ") -> str:
    """Generate a docstring for a class.
    
    Args:
        label: Optional label for the class
        iri: Optional IRI for the class
        comment: Optional comment for the class
        indent: Indentation string to use
        
    Returns:
        Docstring lines as a single string, or empty string if no content
    """
    if not (label or iri or comment):
        return ""
    
    docstring_first = f'{indent}"""'
    if label:
        docstring_first += f'{label} '
    if iri:
        docstring_first += f'<{iri}>.'
    
    if comment:
        docstring_lines = [docstring_first, '']
        for line in str(comment).splitlines():
            comment_line = line.rstrip()
            if comment_line and not comment_line.endswith('.'):
                comment_line += '.'
            docstring_lines.append(f'{indent}{comment_line}')
        docstring_lines.append(f'{indent}"""')
        return '\n'.join(docstring_lines)
    else:
        return f'{docstring_first}"""'


def generate_class_definition(
    class_name: str,
    parent_names: Optional[list[str]] = None,
    indent: str = "",
    base_cls: type[BaseModel] | None = None,
) -> str:
    """Generate a class definition line.
    
    Args:
        class_name: Name of the class
        parent_names: Optional list of parent class names
        indent: Indentation string
        base_cls: Base class type to inherit from (default: None, uses BaseModel)
        
    Returns:
        Class definition line
    """
    if parent_names:
        parents_str = ", ".join(parent_names)
        return f"{indent}class {class_name}({parents_str}):"
    else:
        base_class_name = base_cls.__name__ if base_cls is not None else "BaseModel"
        return f"{indent}class {class_name}({base_class_name}):"


def generate_property_line(prop_name: str, prop_type: str, indent: str = "    ") -> str:
    """Generate a property definition line.
    
    Args:
        prop_name: Name of the property
        prop_type: Type annotation for the property
        indent: Indentation string
        
    Returns:
        Property definition line
    """
    return f"{indent}{prop_name}: {prop_type}"


def generate_ellipsis_line(indent: str = "    ") -> str:
    """Generate an ellipsis line for empty classes.
    
    Args:
        indent: Indentation string
        
    Returns:
        Ellipsis line
    """
    return f"{indent}..."


def generate_model_config(indent: str = "    ", exclude_empty_defaults: bool = True) -> list[str]:
    """Generate Pydantic model_config lines for serialization optimization.
    
    Args:
        indent: Indentation string
        exclude_empty_defaults: Whether to exclude None/empty values from serialization
        
    Returns:
        List of code lines defining model_config
    """
    lines = [f'{indent}model_config = {{"exclude_none": True}}']
    return lines
