def add(itemsdict,name,price=0):
    '''
    This function to used to add items to the inventory

    :param itemsdict: dict which contains the items
    :param name: Name of the item to be added
    :param price: Price of the item to be added
    :return:dict
    '''
    itemsdict[name] = price
    return itemsdict

if __name__ == '__main__':
    '''
    Perform the below Shopping cart operations:
    add: Add items to Shopping Cart
    len: Calculate the Total number of items added in cart
    total: Calculate the Total value of cart
    '''
    items = {}
    count = 0
    cart = 0
    method = []

    # Enter the no of items along with name and price of each item
    no_of_items = int(input("Enter number of items: "))
    for additem in range(no_of_items):
        name, price = input("Enter name and price: ").split()
        items = add(items,name,int(price))

    # Add items to cart and calculate total no of items and value of cart
    no_of_calls = int(input("Enter number of calls: "))
    for call in range(no_of_calls):
        method.append(list(input("Enter multiple values: ").split()))
        for oper in method[call]:
            if 'add' in oper:
                # Calculate total no of items added to cart
                count += 1
            if 'len' in oper:
                print("Total shopping cart items:%d" % count)
            if 'total' in oper:
                # Calculate the Shopping cart value
                for oper_name in method:
                    if 'add' in oper_name[0]:
                        for item in items:
                            if oper_name[1] == item:
                                cart = cart + items[item]
                print("Total shopping cart:",cart)
                cart = 0





