menu = [
    {
        "name": "double cheeseburger",
        "cost": 5
    },
    {
        "name": "cheeseburger",
        "cost": 4
    },
    {
        "name": "fries",
        "cost": 3
    },
    {
        "name": "soda",
        "cost": 1
    }
]
purchase_list = []
purchase_total = 0
desired_item = "NOTEMPTY"


while desired_item != "":
    desired_item = input("Enter what item you'd like: ")
    
    for item in menu:
        if item["name"] == desired_item:
            purchase_list.append(item)

print("\n\nYou've ordered:")

for item in purchase_list:
    print("    " + item["name"])
    purchase_total += item["cost"]

print("Total: $" + str(purchase_total))