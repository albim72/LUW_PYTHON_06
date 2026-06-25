from dataclasses import dataclass

@dataclass
class Product:
    name:str
    price:float
    quantity:int

    def __post_init__(self):
        if self.price <= 10:
            raise ValueError("Price cannot be less than 10")
        if self.quantity < 1:
            raise ValueError("Quantity cannot be less than 1")

    def total_value(self):
        return self.price * self.quantity


p1 = Product("Apple Air Macbook",11200,2)
p2 = Product("Apple Pro Macbook",13800,1)
p3 = Product("Apple Mouse",320,3)

print(p1.total_value())
print(p2.total_value())
print(p3.total_value())

# p3 = Product("Apple Pad",7,6)
