from abc import ABC, abstractmethod
from typing import Type


class Charge:
    def __init__(self, succeeded: bool):
        self.succeeded = succeeded


class PaymentProvider(ABC):

    @classmethod
    @abstractmethod
    def charge(cls, price: float, description: str) -> Charge:
        pass


class User:
    payment_method: Type[PaymentProvider]


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
