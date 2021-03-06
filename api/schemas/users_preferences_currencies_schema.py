from typing import Optional
from pydantic import BaseModel


class PreferencesCurrenciesModel(BaseModel):
    id: Optional[int]
    id_user: int
    id_currency: str
