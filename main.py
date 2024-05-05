from food_item import FoodItem
from menu import Menu
from user import Customer, Admin,Employee
from restaurent import Restaurent
from orders import Order
#class Customer(User):
    #def __init__(self, name, phone, email, address):
coders_adda = Restaurent("Coders Adda")
def customer_menu():
    name = input("Enter your name : ")
    phone = input("Enter your phone : ")
    email = input("Enter your email : ")
    address = input("Enter your address : ")
    customer = Customer(name=name,phone = phone,email=email,address=address)
    while True:
        print(f"-----Welcome {customer.name}----")
        print("1 : View Menu")
        print("2 : Add Item To Cart")
        print("3 : View Cart")
        print("4 : PayBill")
        print("5 : Exit")

        choice = int(input("Enter your choice : "))
        if choice ==1:
            customer.view_menu(coders_adda)
        elif choice ==2:
            item_name = input("Select an item : ")
            item_quantity = int(input("How meny product do you want to buy : "))
            customer.add_to_cart(coders_adda,item_name=item_name,quantity=item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4 :
            customer.payBill()
        elif choice == 5:
            break
        else:
            print("Sorry!! Enter value from given option")


def admin_menu():
    name = input("Enter your name : ")
    phone = input("Enter your phone : ")
    email = input("Enter your email : ")
    address = input("Enter your address : ")
    admin = Admin(name=name,phone = phone,email=email,address=address)
    
    while True:
        print(f"-----Welcome {admin.name}----")
        print("1 : Add New Item")
        print("2 : Add New Employee")
        print("3 : View Employee")
        print("4 : View Item")
        print("5 : Delete Item")
        print("6 : Exit")


        choice = int(input("Enter your choice : "))
        if choice ==1:
            item_name = input("Enter item name : ")
            item_price = int (input("Enter item price : "))
            item_quantity = int(input("Enter item quantiry : "))
            item = FoodItem(name=item_name,price=item_price,quantity=item_quantity)
            admin.add_new_item(coders_adda,item)
        elif choice == 2:
            name = input("Enter employee name : ")
            phone = input("Enter employee phone : ")
            email = input("Enter employee email : ")
            address = input("Enter employee address : ")
            age = input("Enter employee age : ")
            designation = input("Enter employee designation : ")
            salary = input("Enter employee salary : ")
            
            employee = Employee(name,phone,email,address,age,designation,salary)
            admin.add_employee(coders_adda,employee)

        elif choice == 3:
            admin.view_employee(coders_adda)
        elif choice == 4 :
            admin.view_menu(coders_adda)
        elif choice == 5:
            item_name = input("Enter item name : ")
            admin.delete_item(coders_adda,item_name)
        elif choice == 6:
            break
        else:
            print("Sorry!! Enter value from given option")

while True:
    print(" ------Welcome To Coders Adda-----")
    print("1 : Customer")
    print("2 : Admin")
    print("3 : Exit")
    choice = int(input("Enter you choice : "))
    if choice == 1:
        customer_menu()
    elif choice ==2 :
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input")