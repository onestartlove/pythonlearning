from task7 import Commodity

commodity1 = Commodity(1, "Product A", 10, 100)
commodity1.display()
sold_quantity = 50
income = commodity1.income(sold_quantity)
print("Income:", income)

commodity1.setdata(1, "Updated Product A", 15, 200)


commodity1.display()
