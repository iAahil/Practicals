total = 0
items = int(input("Enter Number of Items: "))
while items <= 0:
    print("Invalid Number! Try Again!")
    items = int(input("Enter Number of Items: "))
for i in range(items):
    price = float(input("Enter the Price of the item: "))
    total = total + price
if total >= 100:
    total = total - ((total * 10) / 100)
print("Total Price for", items, "items is $", total, )
