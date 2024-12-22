from pydantic import BaseModel, ConfigDict


class DetailSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product: str
    quantity: int
    unit_price: float


class InvoiceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: str
    details: list[DetailSchema]
