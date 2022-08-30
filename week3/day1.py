# Ecommerce using functions, dictionaries, lists, loops

my_shop = {}

def create_products_container():
    # create a dictionary to store products
    # check if container exists
    if 'products' in my_shop:
        print("Products container already exists")
        return my_shop['products']
    else:
        my_shop['products'] = {}
        print('Products container created')
        return my_shop['products']


def create_product(products, product_name, product_price):
    # create a product
    # check if product exists
    if product_name in products:
        print("Product already exists")
        return products
    else:
        products[product_name] = product_price
        print("Product created")
        return products


def update_product(products, product_name, product_price):
    if product_name in products:
        products[product_name] = product_price
        print("Product has been updated")
        return products
    else:
        print("Product does not exist")
        return products


def delete_product(products, product_name):
    if not product_name in products:
        print("Product not found")
        return products

    del products[product_name]
    return products

def show_products(products):
    print(products)


def show_product(products, product_name):
    print(f"{product_name}:{products[product_name]}")


def main():
    # create products container
    products = create_products_container()

    while True:
        print('1. Create a product')
        print('2. Update a product')
        print('3. Delete a product')
        print('4. Show all products')
        print('5. Show a product')
        print('6. Exit')

        choice = input("Enter your choice: ")
        if choice == "1":
            product_name = input("Enter product name: ")
            product_price = input("Enter product price: ")
            products = create_product(products, product_name, product_price)
        elif choice == "2":
            product_name = input("Enter product name: ")
            product_price = input("Enter product price: ")
            products = update_product(products, product_name, product_price)
        elif choice == "3":
            product_name = input("Enter product name to be deleted: ")
            products = delete_product(products, product_name)
        elif choice == "4":#show all products
            show_products(products)
        elif choice == "5":#show a product
            product_name = input("Enter product name: ")
            show_product(products, product_name)
        elif choice == "6":#exit
            break
        else:
            print("Invalid option")



main()
