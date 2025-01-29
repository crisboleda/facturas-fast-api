
import unittest

from invoices.models import InvoiceDetail, Invoice
from invoices.utils.calculation_iva_strategy import IvaInvoiceA, IvaInvoiceB


class TestInvoiceFactory(unittest.TestCase):

    def setUp(self):
        self.invoice_details = [
            InvoiceDetail(product="Bike", quantity=3, unit_price=15500),
            InvoiceDetail(product="Book", quantity=4, unit_price=1350),
            InvoiceDetail(product="Car", quantity=0, unit_price=34600)
        ]
        self.invoice_type_A = Invoice(
            type="A", 
            details=self.invoice_details, 
            calculation_iva_strategy=IvaInvoiceA()
        )
        self.invoice_type_B = Invoice(
            type="B", 
            details=self.invoice_details, 
            calculation_iva_strategy=IvaInvoiceB()
        )

    def test_calculate_iva_invoice_type_A(self):
        total_iva_invoice_A = self.invoice_type_A.get_iva_products()
        self.assertEqual(10899.0, total_iva_invoice_A)

    def test_calculate_iva_invoice_type_B(self):
        total_iva_invoice_B = self.invoice_type_B.get_iva_products()
        self.assertEqual(5449.5, total_iva_invoice_B)
