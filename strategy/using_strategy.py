from abc import ABC, abstractmethod
from dataclass import dataclass


@dataclass
class Charge:
    init: bool


class PaymentProvider(ABC):

    @classmethod
    @abstractmethod
    def charge(cls, price: float, description: str) -> Charge:
        pass


@dataclass
class User:
    payment_method: PaymentProvider


@dataclass
class Product:
    price: float
    description: str


class PaymentProcessor:
    def process(self, user: User, product: Product) -> bool:
        charge = user.payment_method.charge(
            price=product.price,
            description=product.description,
        )

        return charge.succeeded
