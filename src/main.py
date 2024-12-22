import uvicorn
from fastapi import FastAPI

from invoices.router import invoce_router
from invoices.exceptions import InvoiceTypeNotFound, invoice_type_not_found_handler


app = FastAPI()

# Routes modules
app.include_router(invoce_router)

# Custom exceptions
app.add_exception_handler(InvoiceTypeNotFound, invoice_type_not_found_handler)


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8083)
