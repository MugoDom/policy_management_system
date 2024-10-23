### define a policy product class

class Product_Management:
    def __init__(self, product_id, product_name, product_price, status = 'Active'):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    @classmethod
    def create_product(cls, product_id, product_name, product_price, status = 'Active'):
        """""
        class method to create a new product for a policyholder
        """""
        return cls(product_id, name, price)

    def update_product(self):
        pass
    

    def remove_product(self):
        pass

