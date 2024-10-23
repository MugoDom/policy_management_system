# policyholder.py

class Policyholder:
    def __init__(self, policyholder_id, name, status='Active'):
        self.policyholder_id = policyholder_id
        self.name = name
        self.status = status
        self.products = []
        self.payments = []

    def suspend(self):
        self.status = 'Suspended'

    def reactivate(self):
        self.status = 'Active'

    def add_product(self, product):
        self.products.append(product)

    def add_payment(self, payment):
        self.payments.append(payment)

    def display_details(self):
        product_names = ', '.join([product.name for product in self.products])
        payment_amounts = ', '.join([f"${payment.amount}" for payment in self.payments])
        return {
            'Policyholder': self.name,
            'Status': self.status,
            'Products': product_names,
            'Payments': payment_amounts
        }
