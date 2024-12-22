from invoices.schemas import InvoiceSchema, InvoiceResponseSchema
from invoices.utils.invoice_factory import InvoiceFactory
from invoices.exceptions import InvoiceTypeNotFound
from invoices.models import InvoiceDetail

from fastapi import APIRouter


invoce_router = APIRouter()


@invoce_router.post("/invoices/")
def create_invoce(invoce_schema: InvoiceSchema) -> InvoiceResponseSchema:
    invoice_details = [
        InvoiceDetail(**instance.model_dump()) for instance in invoce_schema.details
    ]
    invoice = InvoiceFactory.create_invoice(
        type=invoce_schema.type,
        details=invoice_details,
    )
    if invoice:
        invoice_calculated = {
            "type": invoice.type,
            "subtotal": invoice.get_subtotal_products(),
            "applied_tax": {
                "percentage": invoice.calculation_iva_strategy.iva_percentage * 100,
                "amount": invoice.get_iva_products(),
            },
            "total": invoice.get_total_products(),
            "details": invoice.details,
        }
        invoice_response = InvoiceResponseSchema.model_validate(invoice_calculated)
        return invoice_response
    else:
        raise InvoiceTypeNotFound(user_invoice_type=invoce_schema.type)
