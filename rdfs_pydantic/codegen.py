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
            # Only add period if line doesn't end with sentence-ending punctuation
            if comment_line and not comment_line[-1] in '.!?。！？':
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


def generate_class_iri_line(class_iri: str, indent: str = "    ") -> str:
    """Generate a class IRI line as ClassVar.
    
    Args:
        class_iri: The IRI of the class
        indent: Indentation string
        
    Returns:
        Class IRI line
    """
    return f'{indent}_class_iri: ClassVar[str] = "{class_iri}"'


def generate_property_line(
    prop_name: str, 
    prop_type: str, 
    indent: str = "    ", 
    prop_iri_for_field: Optional[str] = None,
    prop_iri_for_docstring: Optional[str] = None,
    label: Optional[str] = None, 
    comment: Optional[str] = None
) -> str:
    """Generate a property definition line with optional docstring.
    
    Args:
        prop_name: Name of the property
        prop_type: Type annotation for the property (e.g., "str | list[str] | None")
        indent: Indentation string
        prop_iri_for_field: Optional IRI for the property (used in Field json_schema_extra)
        prop_iri_for_docstring: Optional IRI for the property (used in docstring)
        label: Optional label for the property (used in docstring)
        comment: Optional comment for the property (used in docstring)
        
    Returns:
        Property definition line(s), including docstring if label or comment provided
    """
    lines = []
    
    # Build the base field call if we have a property IRI for field metadata
    if prop_iri_for_field:
        json_schema_extra = f'{{"_property_iri": "{prop_iri_for_field}"}}'
        # Type already includes | None, so use it directly
        lines.append(f"{indent}{prop_name}: {prop_type} = Field(default=None, json_schema_extra={json_schema_extra})")
    else:
        # Original behavior without IRI: type already includes | None, so just use it
        if prop_type.startswith("list["):
            lines.append(f"{indent}{prop_name}: {prop_type} = []")
        else:
            lines.append(f"{indent}{prop_name}: {prop_type} = None")
    
    # Add docstring if label or comment provided
    if label or comment:
        docstring_first = f'{indent}"""'
        if label:
            docstring_first += f'{label}'
        # Include IRI in docstring if available
        if prop_iri_for_docstring:
            if label:
                docstring_first += ' '
            docstring_first += f'<{prop_iri_for_docstring}>.'
        
        if comment:
            lines.append(docstring_first)
            lines.append('')
            for line in str(comment).splitlines():
                comment_line = line.rstrip()
                # Only add period if line doesn't end with sentence-ending punctuation
                if comment_line and not comment_line[-1] in '.!?。！？':
                    comment_line += '.'
                lines.append(f'{indent}{comment_line}')
            lines.append(f'{indent}"""')
        else:
            lines.append(f'{docstring_first}"""')
    
    return '\n'.join(lines)


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
