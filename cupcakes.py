from abc import ABC, abstractmethod
from pprint import pprint
import csv

class Cupcake(ABC):
    size = "regular"
    def __init__(self, name, price, flavor, frosting, filling):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprinkle in args:
            self.sprinkles.append(sprinkle)

    @abstractmethod
    def price_calculator(self, quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"

    def __init__(self, name, price, flavor, frosting):
        self.name = name
        self.price = price
        self.flavor = flavor
        self.frosting = frosting
        self.sprinkles = []


    
class Regular(Cupcake):
    size = "regular"



class Large(Cupcake):
    size = "large"


def read_csv(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            pprint(row)

read_csv("sample.csv")

def add_cupcake_to_csv(file, cupcakes):
    with open(file, "w", newline="\n") as csvfile:
        fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})


cupcake1 = Regular("Stars and Stripes", 2.99, "Vanilla", "Vanilla", "Chocolate")
cupcake1.add_sprinkles("Red", "White", "Blue")
cupcake2 = Mini("Oreo", .99, "Chocolate", "Cookies and Cream")
cupcake2.add_sprinkles("Oreo pieces")
cupcake3 = Large("Red Velvet", 3.99, "Red Velvet", "Cream Cheese", None)

cupcake_list = [
    cupcake1,
    cupcake2,
    cupcake3
]

def get_cupcakes(file):
    with open(file) as csvfile:
        read = csv.DictReader(csvfile)
        read = list(read)
        return read
    
def find_cupcake(file, name):
    for cupcake in get_cupcakes(file):
        if cupcake['name'] == name:
            return cupcake
    return None

# def write_new_csv(file, cupcakes):
#     with open(file, "w", newline="\n") as csvfile:
#         fieldnames = ["size", "name", "price", "flavor", "frosting", "sprinkles", "filling"]
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#         writer.writeheader()
        
#         for cupcake in cupcakes:
#             if hasattr(cupcake, "filling"):
#                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
#             else:
#                 writer.writerow({"size": cupcake.size, "name": cupcake.name, "price": cupcake.price, "flavor": cupcake.flavor, "frosting": cupcake.frosting, "sprinkles": cupcake.sprinkles})



my_cupcake = Cupcake("Cookies and Cream", 2.99, "Chocolate", "Oreo", "Vanilla")

my_cupcake.add_sprinkles("Oreo crumbs", "Chocolate", "Vanilla")

print(my_cupcake.sprinkles)

my_cupcake_mini = Mini("Chocolate", 1.99, "Chocolate", "White")

print(my_cupcake_mini.name)
print(my_cupcake_mini.price)
print(my_cupcake_mini.size)