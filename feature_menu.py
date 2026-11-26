products = {
    1: ["Burger", 50],
    2: ["Fries", 35],
    3: ["Soft Drink", 25]
}

orders = []

print("===== PRODUCT MENU =====")

for number, product in products.items():
    print(number, "-", product[0], "P", product[1])

while True:
    choice = int(input("Select a product (1-3): "))

