import unittest

from invoices.utils.invoice_factory import InvoiceFactory
from invoices.models import Invoice


class TestInvoiceFactory(unittest.TestCase):

    def test_create_invoice_type_A(self):
        invoice = InvoiceFactory.create_invoice(
            type="A",
            details=[],
        )
        self.assertIsInstance(invoice, Invoice)
        self.assertEqual(invoice.type, "A")

    def test_create_invoice_type_B(self):
        invoice = InvoiceFactory.create_invoice(
            type="B",
            details=[],
        )
        self.assertIsInstance(invoice, Invoice)
        self.assertEqual(invoice.type, "B")

    def test_create_invoice_type_C(self):
        invoice = InvoiceFactory.create_invoice(
            type="C",
            details=[],
        )
        self.assertIsInstance(invoice, Invoice)
        self.assertEqual(invoice.type, "C")

    def test_create_invoice_type_D(self):
        invoice = InvoiceFactory.create_invoice(
            type="D",
            details=[],
        )
        self.assertIsNone(invoice)
