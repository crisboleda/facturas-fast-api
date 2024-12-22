from invoices.schemas import InvoiceSchema
from invoices.utils.invoice_factory import InvoiceFactory
from invoices.exceptions import InvoiceTypeNotFound

from fastapi import APIRouter


invoce_router = APIRouter()


@invoce_router.post("/invoices/")
def create_invoce(invoce_schema: InvoiceSchema):
    invoice = InvoiceFactory.create_invoice(
        type=invoce_schema.type, details=invoce_schema.details
    )
    if invoice:
        pass
    else:
        raise InvoiceTypeNotFound(user_invoice_type=invoce_schema.type)

    return invoice
