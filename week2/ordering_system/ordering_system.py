menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}



def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    subtotal = 0

    prices = []

    prices = [ i["price"] for i in order ]

    for x in prices:
        float(x)
        subtotal = subtotal + x
    


    # subtotal_price = subtotal_price + [order[i]["price"]
    return subtotal
    raise NotImplementedError()



def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE

    tax = float(subtotal * 15 / 100)
    round(tax, 2)
    return tax
    
    raise NotImplementedError()

def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total

    """
    ### WRITE SOLUTION HERE


    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)

    total = round(float(subtotal + tax), 2)    

    print("\n")
    print("\nSubtotal for the order is: " + str(subtotal))

    print("Tax for the order is: " + str(tax))

    names = []
    names = [ r["name"] for r in order ]

    print(f"{names} => {total}")

    # float(total)

    # names = ["name" for i in order]

    return names, total

    raise NotImplementedError()

# This function is provided for you, and will print out the items in an order
def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order, items

# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order
'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print("\n")

    print_order(order)

    summarize_order(order)

    # items, subtotal = summarize_order(order, subtotal_price, tax_price)

    # total = summarize_order(order)
    # print("\nTotal price is: " + str(total))

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # print(f"Subtotal for the order is: {str(subtotal_price)}")

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # print(f"Tax for the order is: {str(tax_price)}")

    # items, subtotal = summarize_order(order)

    # print(f"Total price is: {str(total)}")


if __name__ == "__main__":
    main()
