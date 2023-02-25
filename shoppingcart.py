def add(items,name,price=0):
    items[name] = price
    return items

if __name__ == '__main__':
    items = {}
    no_of_items = int(input("Enter number of items: "))
    print(no_of_items)
    for additem in range(no_of_items):
        name, price = input("Enter name and price: ").split()
        items = add(items,name,int(price))
    print(items)
    count = 0
    total = 0
    cart = {}
    no_of_calls = int(input("Enter number of calls: "))
    for oper in range(no_of_calls):
        method = input("Enter operation: ")
        if method == 'add':
            name = input("Enter name: ")
            cart = add(cart, name)
        if method == 'total':
            for item in cart:
                count += 1
            print("Total shopping cart items:%d" % count)
        if method == 'len':
            for item in cart:
                total = total + cart[item]
            print("Total :%d" % total)

