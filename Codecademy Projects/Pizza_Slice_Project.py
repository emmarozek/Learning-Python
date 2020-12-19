toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)

print("We sell " +str(num_pizzas)+ " different kinds of pizza!")

pizzas = list(zip(prices, toppings))
pizzas.sort()

print("\n")
print(pizzas)

cheapest_pizza = pizzas[0]
priciest_pizza = pizzas[-1]
three_cheapest = pizzas[:3]

print("\n")
print(three_cheapest)

num_two_dollar_slices = prices.count(2)

print("\n")
print(num_two_dollar_slices)