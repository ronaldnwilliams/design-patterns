from strategy.lib import stripe, btcpay, paypal, apple_pay, affirm


class User:
    payment_method: str


class Product:
    price: float
    description: str


class PaymentProcessor:
    def charge(self, user: User, product: Product) -> bool:
        payment_method = user.payment_method

        if payment_method == 'STRIPE':
            charge = stripe.make_charge(product.price, product.description)
            success = charge.success
        elif payment_method == 'BITCOIN':
            charge = btcpay.make_charge(product.price, product.description)
            success = charge.received
        elif payment_method == 'PAYPAL':
            charge = paypal.make_charge(product.price, product.description)
            success = charge.is_successful
        elif payment_method == 'APPLE PAY':
            charge = apple_pay.make_charge(product.price, product.description)
            success = charge.processed
        elif payment_method == 'AFFIRM':
            charge = affirm.make_charge(product.price, product.description)
            success = charge.succeeded
        else:
            success = False

        return success
