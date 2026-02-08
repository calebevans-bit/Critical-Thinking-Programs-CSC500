class ItemToPurchase:
    def __init__(self, name="none", price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity
        self.item_description = description
    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${total_cost:.2f}')
    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")
def get_item_input():
    new_item = ItemToPurchase()
    new_item.item_name = input('Enter the item name:   ')
    new_item.item_description = input('Enter the item description:   ')
    new_item.item_price = float(input('Enter the item price:   '))
    new_item.item_quantity = int(input('Enter the item quantity:   '))
    return new_item

class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print(f'The item was not found in the cart. Nothing removed.')

    def modify_item(self, item_to_modify):
        for item in self.cart_items:
            if item.item_name == item_to_modify.item_name:
                if item_to_modify.item_description != 'none':
                    item.item_description = item_to_modify.item_description
                if item_to_modify.item_price != 0:
                    item.item_price = item_to_modify.item_price
                if item_to_modify.item_quantity != 0:
                    item.item_quantity = item_to_modify.item_quantity
                return
    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if len(self.cart_items) > 0:
            for item in self.cart_items:
                item.print_item_cost()
        else:
            print('Shopping Cart is empty')
        print(f"Total cost: ${self.get_cost_of_cart()}")
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()

if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")

    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    menu_running = True
    while menu_running:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")

        user_choice = input("\nChoose an option: ")

        if user_choice == 'a':
            print("\nADD ITEM TO CART")
            new_item = get_item_input()
            cart.add_item(new_item)

        elif user_choice == 'r':
            print("\nREMOVE ITEM FROM CART")
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif user_choice == 'c':
            print("\nCHANGE ITEM QUANTITY")
            item_name = input("Enter the item name: ")
            new_qty = int(input("Enter the new quantity: "))
            modified_item = ItemToPurchase(item_name, 0, new_qty, '')
            cart.modify_item(modified_item)

        elif user_choice == 'i':
            print("\nOUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()

        elif user_choice == 'o':
            print("\nOUTPUT SHOPPING CART")
            cart.print_total()

        elif user_choice == 'q':
            menu_running = False