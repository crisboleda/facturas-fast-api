from fastapi import Request, status
from fastapi.responses import JSONResponse


class InvoiceTypeNotFound(Exception):

    def __init__(self, user_invoice_type: str):
        self.user_invoice_type = user_invoice_type


async def invoice_type_not_found_handler(request: Request, exc: InvoiceTypeNotFound):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"Invoice type: '{exc.user_invoice_type}' is not allowed."},
    )
