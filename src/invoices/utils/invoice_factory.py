from invoices.models import InvoiceDetail, Invoice
from invoices.utils.calculation_iva_strategy import (
    IvaInvoiceA,
    IvaInvoiceB,
    IvaInvoiceC,
)


class InvoiceFactory:

    __calculation_invoice_iva_strategy = {
        "A": IvaInvoiceA(),
        "B": IvaInvoiceB(),
        "C": IvaInvoiceC(),
    }

    @staticmethod
    def create_invoice(type: str, details: list[InvoiceDetail]) -> Invoice:
        calculation_invoice_iva_strategy = (
            InvoiceFactory.__calculation_invoice_iva_strategy.get(type)
        )
        if calculation_invoice_iva_strategy:
            return Invoice(
                type=type,
                details=details,
                calculation_iva_strategy=calculation_invoice_iva_strategy,
            )
        return None
