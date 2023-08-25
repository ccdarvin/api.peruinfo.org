from ninja import ModelSchema, FilterSchema, Field
from typing import Optional

from peruinfo.utils import to_camel
from .models import Padron


class PadronOutSchema(ModelSchema):
    
    class Config:
        model = Padron
        model_fields = "__all__"
        model_exclude = ["search_vector"]
        alias_generator = to_camel
        allow_population_by_field_name = True


class PadronFilterSchema(FilterSchema):
    q: Optional[str] = Field(q=['search_vector'])
 