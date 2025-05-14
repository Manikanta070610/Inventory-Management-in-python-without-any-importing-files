dic={}
try:
    def add_elements(item,item_quantity,item_price):
        dic[item]={"Quantity":float(item_quantity[0]),"Units":item_quantity[1],"Price":item_price}

    def viewitems(dic):
        if len(dic)==0:
            print("There are no elements in your dictionary")
        else:
            print("These are the elements that are currently there in your inventory.")
            print("Item name     Quantity     Price      Total cost")    
            for i, j in dic.items():
                print(f"{i}     {j['Quantity']} {j['Units']}    ₹{j['Price']}      ₹{j['Price']*j['Quantity']}")

    def remove_elements(item):
        if item in dic:
            dic.pop(item)
            print(f"{item} has been successfully removed from the inventory.")
        else:
            print("Item not found")

    def item_update(item,choice,new):
        if item in dic:
            if choice in item:
                dic[item][choice]=new

    while True:
        print("Welcome to the your Warehouse")
        print("1. Adding item's to your warehouse.")
        print("2. Remove an item from your warehouse.")
        print("3. Updating item in your warehouse.")
        print("4. View total items left in the inventory.")
        print("5. Exit the program")
        inp=int(input("Enter your choice: "))

        if inp==1:
            print("Enter the details of the product")
            item=input("Enter the name of the product: ")
            item_quantity=input("Enter the quantity of product and give 3 words of its units at last: ").split()
            item_price=float(input("Enter the price of the product: "))
            add_elements(item,item_quantity,item_price)

        elif inp==2:
            print("These are the items that are there in your inventory currently")
            viewitems(dic)
            item=input("Enter the name of the element you want to remove from the ware house:")
            remove_elements(item)
        
        elif inp==3:
            print("These are the elements that are currently there in your inventory.")
            viewitems(dic)
            item=input("Enter the item you want to update:")
            choice=input("What do you want to update(for Quantity:(Q or q), for Price: (P or p)): ")
            if choice.lower()=='q':
                new=float(input("Enter the new Quantity:"))
            elif choice.lower()=='p':
                new=float(input("Enter new price:"))
            item_update(item,choice,new)

        elif inp==4:
            viewitems(dic)
            
        elif inp==5:
            break

        else:
            print("Invalid choice! Please enter a valid option.")
except:
    print("There has been an error.")