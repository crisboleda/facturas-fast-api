from abc import ABC, abstractmethod


class IvaStrategy(ABC):
    @abstractmethod
    def calculate_iva(self, subtotal: float):
        pass


class IvaInvoiceA(IvaStrategy):
    def calculate_iva(self, subtotal):
        return subtotal * 0.21  # 21% IVA


class IvaInvoiceB(IvaStrategy):
    def calculate_iva(self, subtotal):
        return subtotal * 0.105  # 10.5% IVA


class IvaInvoiceC(IvaStrategy):
    def calculate_iva(self, subtotal):
        return 0  # Sin IVA
