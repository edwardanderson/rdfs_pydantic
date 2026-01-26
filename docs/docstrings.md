# Docstrings

Docstrings are templated using the available values from:
  - IRI
  - `rdfs:label` (optional)
  - `rdfs:comment` (optional)

If `rdfs:comment` is not available, then a single-line docstring is generated.

```python
class Example(BaseModel):
    """{{rdfs:label}} {{IRI}}."""
    ...
```

Otherwise, a multi-line docstring is generated.

```python
class Example(BaseModel):
    """{{rdfs:label}} {{IRI}}.

    {{rdfs:comment}}.
    """
    ...
```
