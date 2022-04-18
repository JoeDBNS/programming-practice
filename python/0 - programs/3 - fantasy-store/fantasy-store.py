
# Define globals

items = {
    0: {
        "type": "weapon",
        "name": "Sword",
        "damage": 20,
        "speed": 2
    },
    1: {
        "type": "weapon",
        "name": "Dagger",
        "damage": 10,
        "speed": 3
    },
    2: {
        "type": "weapon",
        "name": "Mallet",
        "damage": 30,
        "speed": 1
    },
    3: {
        "type": "weapon",
        "name": "Sword of Destiny",
        "damage": 40,
        "speed": 2
    },
    4: {
        "type": "tool",
        "name": "Torch"
    },
    5: {
        "type": "tool",
        "name": "Ration"
    },
    6: {
        "type": "other",
        "name": "Magic Spoon"
    },
    7: {
        "type": "other",
        "name": "Cow Dung"
    }
}

user = {
    "name": "Flargen Barger",
    "money": 1200,
    "inventory": items
}

for item_key in user["inventory"].keys():
    user["inventory"][item_key]["amount"] = 0

store_stock = [
    {
        "item_id": 0,
        "cost": 20,
        "amount": 3,
        "hidden": False
    },
    {
        "item_id": 1,
        "cost": 15,
        "amount": 4,
        "hidden": False
    },
    {
        "item_id": 4,
        "cost": 4,
        "amount": 12,
        "hidden": False
    },
    {
        "item_id": 5,
        "cost": 6,
        "amount": 20,
        "hidden": False
    },
    {
        "item_id": 6,
        "cost": 500,
        "amount": 1,
        "hidden": True
    },
    {
        "item_id": 3,
        "cost": 1500,
        "amount": 1,
        "hidden": False
    }
]



def PrintStock():
    print("Here is the current stock:")

    for store_item in store_stock:
        if store_item["hidden"] == False:
            print(items[store_item["item_id"]]["name"] + "\t$" + str(store_item["cost"]) + "\tx" + str(store_item["amount"]))



print("\n\n\n\n\n\n\n\n\n\n\n\n")

PrintStock()

next_purchase = input("\nWhat would you like to purchase? ")

while next_purchase != "":
    item_found = False

    for store_item in store_stock:
        if items[store_item["item_id"]]["name"].lower() == next_purchase.lower():
            item_found = True

            if store_item["amount"] < 1:
                print("\nThe " + items[store_item["item_id"]]["name"] + " is out of stock.")
            else:
                if user["money"] < store_item["cost"]:
                    print("\nYou cannot afford the " + items[store_item["item_id"]]["name"] + ". You need " + str(store_item["cost"] - user["money"]) + " more money to purchase this item.")
                else:
                    user["money"] -= store_item["cost"]
                    user["inventory"][store_item["item_id"]]["amount"] += 1
                    store_item["amount"] -= 1
    
    if item_found == False:
        print("\nThat item was not found in the shop.")

    print()
    PrintStock()

    print("\nYour remaining money:", user["money"])
    next_purchase = input("What would you like to purchase?\n")

print("This is your inventory:")

for item in user["inventory"].values():
    if item["amount"] > 0:
        print(item["name"], "\tx" + str(item["amount"]))


