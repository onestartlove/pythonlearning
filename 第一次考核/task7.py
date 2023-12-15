class Commodity:
    def __init__(self, product_number, product_name, unit_price, total_quantity):
        self.__product_number = product_number
        self.__product_name = product_name
        self.__unit_price = unit_price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = total_quantity
    def display(self):
        print("Product Number:", self.__product_number)
        print("Product Name:", self.__product_name)
        print("Unit Price:", self.__unit_price)
        print("Total Quantity:", self.__total_quantity)
        print("Remaining Quantity:", self.__remaining_quantity)
    def income(self, sold_quantity):
        return sold_quantity * self.__unit_price
    def setdata(self, product_number, product_name, unit_price, total_quantity):
        self.__product_number = product_number
        self.__product_name = product_name
        self.__unit_price = unit_price
        self.__total_quantity = total_quantity
        self.__remaining_quantity = total_quantity
