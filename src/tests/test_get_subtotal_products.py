
import unittest

from invoices.models import InvoiceDetail, Invoice
from invoices.utils.calculation_iva_strategy import IvaInvoiceA

class TestSubtotalProduct(unittest.TestCase):

    def setUp(self):
        self.invoice_details = [
            InvoiceDetail(product="Bike", quantity=3, unit_price=15500),
            InvoiceDetail(product="Book", quantity=4, unit_price=1350),
            InvoiceDetail(product="Car", quantity=0, unit_price=34600)
        ]
        self.invoice = Invoice(
            type="A", 
            details=self.invoice_details, 
            calculation_iva_strategy=IvaInvoiceA()
        )

    def test_get_invoice_subtotal_products(self):
        subtotal = self.invoice.get_subtotal_products()
        self.assertEqual(51900.0, subtotal)
