foods = []
prices = []
total = 0

while True:
    food = input("Enter a Food To Buy (Q to Quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter The Price of a {food.capitalize()}: $"))
        foods.append(food)
        prices.append(price)


print("----- YOUR CART -----")
for food in foods:
    print(food.capitalize(), end= " ")

for price in prices:
    total += price

print()
print(f"Your Total is: ${total:.2f}")

