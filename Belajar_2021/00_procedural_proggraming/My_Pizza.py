

def make_pizza(size, spice="hot", *toppings):
    print(f"\nMake a {spice} {size} cm pizza with the following toppings : ")
    if toppings:
        for topping in toppings:
            print(f"\t-{topping}")
    else:
        print("There is no topping you fat ass.")


make_pizza(12)
make_pizza(15, "extra chili", "Cheese")
make_pizza(18, "not hot", "Cheese", "Mushrooms", "Pepperoni")