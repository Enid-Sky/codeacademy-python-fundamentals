# Review of lists. You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.

# Make a list of pizza toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
print(toppings)

# To keep track of how much each kind of pizza slice costs, create a list called prices that holds the following integer values:
prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)

# How many items are 2 bucks?
num_two_dollar_slices = prices.count(2)
print(f"There are {num_two_dollar_slices} menu items costing $2")

num_of_pizzas = len(toppings)
print(f"We sell {num_of_pizzas} different kinds of pizza!")


pizza_and_prices = [
  [2, "pepperoni"],
  [6, "pineapple"],
  [1, "cheese"],
  [3, "sausage"],
  [2, "olives"],
  [7, "anchovies"],
  [2, "mushrooms"]
]

print(pizza_and_prices)

# Sort pizza prices by cheapest to most expensive
pizza_and_prices.sort()

print(pizza_and_prices)

# Find the cheapest pizza
cheapest_pizza = pizza_and_prices[0][1]
print(f"The cheapest pizza is {cheapest_pizza}")

# A man walks in and asks for our most priciest pizza!
priciest_pizza = pizza_and_prices[-1][1]
print(f"The priciest pizza is {priciest_pizza}")

# That's it, we're out of anchovies, remove it from the list
pizza_and_prices.pop(-1)
print(pizza_and_prices)

# Add new topping for peppers
pizza_and_prices.insert(-2, [2.5, "peppers"])
print(f"The new menu is {pizza_and_prices}")

# Store three cheapest pizzas in a list
three_cheapest = pizza_and_prices[:3]
print(f"The three cheapest pizzas are {three_cheapest}")

