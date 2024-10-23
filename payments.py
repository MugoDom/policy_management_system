class Payment():
    def __init__(self, payment_id, payment_amount, penalty_amount = 0, status = "Paid"):
        self.payment_id = payment_id
        self.paymment_amount = payment_amount
        self.status = status

    def process_payment(self):
        if self.status == "Unpaid":
            self.status = "Paid"
            print(f"Payment ID: {self.payment_id} has been processed. Status: {self.status}")
        else:
            print(f"Payment ID: {self.payment_id} is already marked as {self.status}.")

    def reminder(self):
        if self.status == "Unpaid":
            print(f"Reminder: Payment ID: {self.payment_id} of amount ${self.payment_amount} is due.")
        else:
            print(f"No reminder necessary. Payment ID: {self.payment_id} is already {self.status}.")

    def penalty(self):
        if self.status == "Unpaid":
            self.payment_amount += self.penalty_amount
            print(f"A penalty of ${self.penalty_amount} has been applied to Payment ID: {self.payment_id}. New amount: ${self.payment_amount}")
        else:
            print(f"Cannot apply a penalty. Payment ID: {self.payment_id} is {self.status}.")