#Import the classess from payments, products and policyholder

from policyholder import Policyholder
from payments import Payment
from product import Product_Management

# Testing the functionality in main.py
if __name__ == "__main__":
    # Policyholder operations
    policyholder1 = Policyholder(1, "John", "Doe", "123 Main St")
    policyholder1.register()
    policyholder1.suspend()
    policyholder1.reactivate()

    # Product management operations
    product1 = Product_Management(101, "Laptop", 1500.00)
    product1.create()
    product1.update(new_name="Gaming Laptop", new_price=1800.00)
    product1.remove()

    # Payment operations
    payment1 = Payment(1001, 500, penalty_amount=50, status="Unpaid")
    payment1.send_reminder()
    payment1.apply_penalty()
    payment1.process_payment()

    