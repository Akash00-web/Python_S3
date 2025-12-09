"""
You own a pizzeria named Olly’s Pizzas and want to create a Python program to handle the customers and revenue.
Create the following classes with the following methods:
Class Pizza containing

1.init method:      to iniƟalize the size (small, medium, large), toppings (corn, tomato, onion, capsicum, mushroom, olives,
broccoli), cheese (mozzarella, feta, cheddar). 
Note: One pizza can have only one size but many toppings and cheese. (1.5
marks)
Throw custom exceptions if the selects toppings or cheese not available in lists given above. (1 mark)

2.price method:      to calculate the prize of the pizza in the following way:

small = 50, medium = 100, large = 200
Each topping costs 20 rupees extra, except broccoli, olives and mushroom, which are exotic and so cost 50 rupees each.
Each type of cheese costs an extra 50 rupees. (1.5 marks)
 Class Order containing

1.init method: to iniƟalize the name, customerid of the customer who placed the order (0.5 marks)

2.order method: to allow the customer to select pizzas with choice of toppings and cheese (1 mark)

3.bill method: to generate details about each pizza ordered by the customer and the total cost of the order. (2 marks)
*Note: A customer can get multiple pizzas in one order.

1.5 marks for creating appropriate objects of these classes and writing correct output.

"""

class InvalidToppings(Exception):
    pass

class InvalidCheese(Exception):
    pass


class Pizza:

    valid_size = ["small", "medium", "large"]
    valid_toppings = ["corn", "tomato", "onion", "capsicum", "mushroom", "olives", "broccoli"]
    valid_cheese = ["mozzarella", "feta", "cheddar"]
    base_price = {"small": 50, "medium": 100, "large": 200}
    exotic_toppings = ["broccoli","Olives","mushroom"]  

    def __init__(self, size, toppings, cheese):
        # validate size
        if size not in self.valid_size:
            raise ValueError(f"Invalid size: {size}")

        # validate toppings
        for topping in toppings:
            if topping not in self.valid_toppings:
                raise InvalidToppings(f"Invalid topping: {topping}")

        # validate cheese
        for ch in cheese:
            
            if ch not in self.valid_cheese:
                raise InvalidCheese(f"Invalid cheese: {ch}")

        self.size = size
        self.toppings = toppings
        self.cheese = cheese

    def price(self):
        base_price = self.base_price[self.size]
       
        topping_cost = sum(
            50 if t in self.exotic_toppings else 20
            for t in self.toppings
        )
        cheese_cost = len(self.cheese) * 50
        return base_price + topping_cost + cheese_cost


class Order:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.pizzas = []

    def order(self, pizza):
        self.pizzas.append(pizza)

    def bill(self):
        print(f"\n{'='*50}")
        print(f"Order Bill - {self.name} (ID: {self.customer_id})")
        print(f"{'='*50}")
        total = 0
        for i, pizza in enumerate(self.pizzas, 1):
            pizza_price = pizza.price()
            print(f"Pizza {i}: {pizza.size.capitalize()}")
            print(f"  Toppings: {', '.join(pizza.toppings)}")
            print(f"  Cheese: {', '.join(pizza.cheese)}")
            print(f"  Price: ₹{pizza_price}")
            total += pizza_price
        print(f"{'-'*50}")
        print(f"Total Cost: ₹{total}")
        print(f"{'='*50}\n")


#  Example
if __name__ == "__main__":
    order1 = Order("John", 101)
    order1.order(Pizza("small", ["corn", "tomato"], ["mozzarella"]))
    order1.order(Pizza("large", ["mushroom", "olives", "broccoli"], ["feta", "cheddar"]))
    order1.bill()

