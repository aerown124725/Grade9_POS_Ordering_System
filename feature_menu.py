products = {
    1: ["Burger", 50],
    2: ["Fries", 35],
    3: ["Soft Drink", 25]
}

orders = []

print("===== PRODUCT MENU =====")

orders = []

# Display the product menu
print("=" * 45)
print("PRODUCT MENU")
print("-" * 35)

for number, product in products.items():
    print(f"[{number}] {product[0]} - PHP {product[1]:.2f}")

print("-" * 35)

# Repeat the ordering process
while True:

    # Ask for product number
    choice = int(input("Enter product number (1-3): "))

    # Check if the product number is valid
    if choice in products:

        # Ask for quantity
        quantity = int(input("Enter quantity: "))

        # Get product details
        name = products[choice][0]
        price = products[choice][1]

        # Calculate subtotal
        subtotal = price * quantity

        # Save order details
        orders.append([name, quantity, price, subtotal])

        # Display order confirmation
        print(f"Added: {name} x {quantity}")

    else:
        print("Invalid product number.")

    # Ask if the customer wants another product
    again = input("Order another product? (yes/no): ")

    # Stop only when the customer enters no
    if again.lower() == "no":
        break