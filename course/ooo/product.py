class Product:
    def __init__(self, qty):
        self.qty = qty

    def add(self, units):
        self.qty += units

    def remove(self, units):
        self.qty -= units

    def get_stock(self):
        return self.qty

    def __str__(self):
        return f"Current stock is {self.qty}"

    def __repr__(self):
        return f"Product(qty={self.qty})"


prod = Product(0)
prod.add(10)
prod.remove(5)
print(prod.get_stock())  # Output: 5
print(prod)  # Output: Product(qty=5)
print(repr(prod))
