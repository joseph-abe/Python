def add(itemsdict,name,price=0):
    itemsdict[name] = price
    return itemsdict

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
    cart = 0
    method = []
    no_of_calls = int(input("Enter number of calls: "))
    for oper in range(no_of_calls):
        method.append(list(input("Enter multiple values: ").split()))
        print("List of methods: ", method)
    for oper in method:
        if 'add' in oper:
            count += 1
        if 'total' in oper:
            print("Total shopping cart:%d" % count)
        if 'len' in oper:
            for calc in method:
                if 'add' in calc[0]:
                    for item in items:
                        if calc[1] == item:
                            cart = cart + items[item]
            print("Total shopping cart items:",cart)




