from invoices.utils.calculation_iva_strategy import IvaStrategy


class InvoiceDetail:

    def __init__(self, product: str, quantity: int, unit_price: float):
        self.product = product
        self.quantity = quantity
        self.unit_price = unit_price


class Invoice:

    def __init__(
        self,
        type: str,
        details: list[InvoiceDetail],
        calculation_iva_strategy: IvaStrategy,
    ):
        self.type = type
        self.details = details
        self.calculation_iva_strategy = calculation_iva_strategy

    def get_subtotal_products(self) -> float:
        subtotal = 0.0
        for product in self.details:
            subtotal += product.get("quantity", 0) * product.get("unit_price", 0)
        return subtotal

    def get_iva_products(self) -> float:
        subtotal = self.get_subtotal_products()
        return self.calculation_iva_strategy.calculate_iva(subtotal=subtotal)

    def get_total_products(self) -> float:
        return self.get_subtotal_products() + self.get_products_iva()
