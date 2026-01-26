# Docstrings

Docstrings are templated using the resource IRI, `rdfs:label` and `rdfs:comment`.

```python
class Example(BaseModel):
    """{{rdfs:label}} {{IRI}}.

    {{rdfs:comment}}.
    """
    ...
```
