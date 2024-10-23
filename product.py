### define a policy product class

class Product_Management:
    def __init__(self, product_id, product_name, product_price, status = 'Active'):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.status = status

    
    def create_product(self):
        return {
            "Product ID": self.product_id,
            "Product Name": self.product_name,
            "Product Price": self.product_price,
            "Status": self.status
        }

    def update_product(self, new_name=None, new_price=None):
        if new_name:
            self.product_name = new_name
        if new_price:
            self.product_price = new_price
        print(f"Product {self.product_id} updated: Name - {self.product_name}, Price - {self.product_price}")
    

    def remove_product(self):
        if self.status == 'Active':
            self.status = 'Removed'
            print(f"Product {self.product_name} (ID: {self.product_id}) has been removed.")
        else:
            print(f"Product {self.product_name} is already removed.")

