
def display_receipt(items, total):
    print("===================================")
    print("              RECEIPT              ")
    print("             Mini Store            ")
    print("===================================")
    print("{:<20} {:<10} {:<10}".format("Product", "Quantity", "Price"))
    
    for item, details in items.items():
        quantity = details['quantity']
        price = details['price']
        print("{:<20} {:<10} ${:<10.2f}".format(item, quantity, price * quantity))  
    
    print("-----------------------------------")
    print("{:<20} {:<10} ${:<10.2f}".format("Total Amount:", "", total))

    print("===================================")
    print(" Thank your for shopping with us!  ")
    print("===================================")


