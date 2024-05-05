# Customer
# Employee
# Admin
from orders import Order
from abc import ABC
class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

#----------------Custormer-----------------#
class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()
    
    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        print(f"{item_name}")
        if item :
            if quantity > item.quantity:
                print("Sorry Item Quantiry Exceeded !!")
            else:
                item.quantity = quantity 
                # print(f"{quantity}")
                #self.cart.add_item(item)
                self.cart.add_item(item)
                print("Item added")
        else:
            print("Item Not Found")

    def view_cart(self):
        print("*--------- View Cart---------")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
    
          # print(f"{item.name}{item.price}{quantity}")
           print(f"{item.name}\t{item.price}\t{item.quantity}")
           
        print(f'Total Price : {self.cart.total_price}')
        

    def payBill(self):
        print(f"Your payment {self.cart.total_price} is successfull")
        self.cart.clear()


#----------------Employee-----------------#
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        self.age = age
        self.designation = designation
        self.salary = salary
        super().__init__(name, phone, email, address)
#----------------Admin-----------------#
class Admin(User):
    def __init__(self, name, phone, email, address):
        
        super().__init__(name, phone, email, address)
    
    def add_employee(self,restaurant,employee):
       restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        print("Name\tPhone\tEmail\tAddress")
        restaurant.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def delete_item(self,restaurent,item):
        restaurent.menu.remove_item(item)
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()


