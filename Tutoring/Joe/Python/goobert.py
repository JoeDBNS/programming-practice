from random import randint, choice

items = {
    0: {
        "type": "weapon",
        "name": "Sword",
        "damage": 20,
        "damage_type": "slash",
        "speed": 2
    },
    1: {
        "type": "weapon",
        "name": "Dagger",
        "damage_type": "stab",
        "damage": 10,
        "speed": 3
    },
    2: {
        "type": "weapon",
        "name": "Mallet",
        "damage_type": "blunt",
        "damage": 30,
        "speed": 1
    },
    3: {
        "type": "consumable",
        "name": "Health Potion"
    },
    4: {
        "type": "consumable",
        "name": "Mana Potion"
    },
    5: {
        "type": "other",
        "name": "Dung"
    },
    6: {
        "type": "key",
        "name": "Silver Key"
    }
}

player = {
    "name": "Flargen Barger",
    "max_health": 100,
    "active_health": 100,
    "money": 200,
    "inventory": items
}

for item_key in player["inventory"].keys():
    player["inventory"][item_key]["amount"] = 0




# Inventory
def GiveEntityItem(entity, item_id):
    entity["inventory"][item_id]["amount"] += 1


# Health
def GetEntityHealth(entity):
    health_info = {
        "max_health": entity["max_health"],
        "active_health": entity["active_health"],
        "health_as_percentage": (entity["active_health"] / entity["max_health"]) * 100
    }
    return health_info

def AlterEntityActiveHealth(entity, change_amount):
    entity["active_health"] += change_amount





# Ideas for things game should have:
# Slot machings
# Buying from vendors
# Fight randomly generated enemies

# Story

#   The realm of Goobert has been safe and peaceful for decades now, however, recently
#   monsters have been seen prowling the dense forest surrounding the land and attacking
#   the people and animals of Goobert.

#   As investigations were underway to verify the increase in monsters and identify the
#   cause of the attacks, the royal guards noticed that the princess had been kidnapped.

#   Word spread of a mysterious figure with plans to unravel the governing bodies of the
#   land, bringing it to a restless chaos where someone could swoop in and overtake
#   with little to no resistance.


# funny name: lerm






def AssignRandomRace(entity):
    entity["race"] = choice(races)


def AssignAge(entity, age=-1):
    if age != -1:
        entity["age"] = age

    else:
        if entity["race"] == "elf":
            entity["age"] = randint(1, 300)

        elif entity["race"] == "orc":
            entity["age"] = randint(1, 20)

        elif entity["race"] == "goblin":
            entity["age"] = randint(1, 20)

        else:
            entity["age"] = randint(1, 100)


def GenerateAge(entity):
    if entity["type"] == "player":
        set_age = int(input("what is ur age"))
        entity["age"] = set_age

    if entity["race"] == "elf":
        entity["age"] = randint(1, 300)

    elif entity["race"] == "orc":
        entity["age"] = randint(1, 20)

    elif entity["race"] == "goblin":
        entity["age"] = randint(1, 20)

    else:
        entity["age"] = randint(1, 100)


    # if entity["boss"] == True:
    #     entity["age"] += 10



player["race"] = "human"

AssignRandomRace(enemy1)
AssignRandomRace(enemy2)

AssignAge(player, 34)
AssignAge(enemy1)
AssignAge(enemy2)


print(player)
print(enemy1)
print(enemy2)
