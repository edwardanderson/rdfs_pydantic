from pydantic import BaseModel, ConfigDict

__all__ = ['OptimizedBaseModel']

class OptimizedBaseModel(BaseModel):
    """BaseModel with optimized serialization."""
    model_config = ConfigDict(
        ser_json_schema=False,
        exclude_none=True,
    )
