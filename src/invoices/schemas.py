from pydantic import BaseModel, ConfigDict


class InvoiceDetailSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product: str
    quantity: int
    unit_price: float


class InvoiceSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    type: str
    details: list[InvoiceDetailSchema]


class InvoiceResponseSchema(BaseModel):
    type: str
    subtotal: float
    applied_tax: dict
    total: float
    details: list[InvoiceDetailSchema]
