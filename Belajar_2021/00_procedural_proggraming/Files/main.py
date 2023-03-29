with open("data.txt", "r") as Files:
    fruits = Files.readlines()

clean_fruits = []
for fruit in fruits:
    clean_fruits.append(fruit.strip())
print(clean_fruits)