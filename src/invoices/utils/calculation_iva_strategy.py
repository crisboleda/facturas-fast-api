from abc import ABC, abstractmethod


class IvaStrategy(ABC):
    @property
    @abstractmethod
    def iva_percentage(self) -> float:
        pass

    @abstractmethod
    def calculate_iva(self, subtotal: float):
        pass


class IvaInvoiceA(IvaStrategy):
    @property
    def iva_percentage(self) -> float:
        return 0.21

    def calculate_iva(self, subtotal):
        return subtotal * self.iva_percentage


class IvaInvoiceB(IvaStrategy):
    @property
    def iva_percentage(self) -> float:
        return 0.105

    def calculate_iva(self, subtotal):
        return subtotal * self.iva_percentage


class IvaInvoiceC(IvaStrategy):
    @property
    def iva_percentage(self) -> float:
        return 0.0

    def calculate_iva(self, subtotal):
        return 0
