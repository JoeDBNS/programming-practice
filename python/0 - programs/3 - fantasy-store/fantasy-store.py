
# Define globals

user = {
    "name": "Flargen Barger",
    "money": 1200,
    "inventory": {}
}

store_stock = [
    {
        "name": "Sword",
        "cost": 20,
        "amount": 3,
        "hidden": False
    },
    {
        "name": "Dagger",
        "cost": 15,
        "amount": 4,
        "hidden": False
    },
    {
        "name": "Torch",
        "cost": 4,
        "amount": 12,
        "hidden": False
    },
    {
        "name": "Ration",
        "cost": 6,
        "amount": 20,
        "hidden": False
    },
    {
        "name": "Magic Spoon",
        "cost": 500,
        "amount": 1,
        "hidden": True
    },
    {
        "name": "Sword of Destiny",
        "cost": 1500,
        "amount": 1,
        "hidden": False
    }
]



def PrintStock():
    print("Here is the current stock:")

    for item in store_stock:
        if item["hidden"] == False:
            print(item["name"] + "\t$" + str(item["cost"]) + "\tx" + str(item["amount"]))



print("\n\n\n\n\n\n\n\n\n\n\n\n")

PrintStock()

next_purchase = input("\nWhat would you like to purchase? ")

while next_purchase != "":
    item_found = False

    for item in store_stock:
        if item["name"].lower() == next_purchase.lower():
            item_found = True

            if item["amount"] < 1:
                print("\nThe " + item["name"] + " is out of stock.")
            else:
                if user["money"] < item["cost"]:
                    print("\nYou cannot afford the " + item["name"] + ". You need " + str(item["cost"] - user["money"]) + " more money to purchase this item.")
                else:
                    user["money"] -= item["cost"]
                    if item["name"] in user["inventory"].keys():
                        user["inventory"][item["name"]] += 1
                    else:
                        user["inventory"][item["name"]] = 1
                    item["amount"] -= 1
    
    if item_found == False:
        print("\nThat item was not found in the shop.")

    print()
    PrintStock()

    print("\nYour remaining money:", user["money"])
    next_purchase = input("What would you like to purchase?\n")

print("This is your inventory:")

for item_key, item_value in user["inventory"].items():
    print(item_key + "\tx" + str(item_value))


