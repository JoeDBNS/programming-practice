# Boss Fight
# -----------------------------------------
# Build your player stats and then fight a randomly generated enemy, original
# pokemon battle style.


# Requirements
# -------------
#     - Build your fighters stats
#     - Generate a "random" enemy
#     - Choose whether to attack or defend
#     - Enemy will attack or defend "randomly"
#     - Player attacks have a "telegraph" value that represents whether it"d be better for the enemy to attack or defend. Based on this value and the 
#     - perception stat of the enemy, they might make the smarter choice against you.





# To Create A Character:
#   - Name
#   - Race
#   - Stats
#       - Level
#       - Max Health
#       - Intelligence
#       - Perception
#       - Strength
#       - Defence
#       - Speed
#   - Gear
#   - Money / Prize / Inventory












from math import floor
from random import choice, randint




entity_races = ["human", "elf", "goblin", "orc"]

entity_first_names = {
    "human": [
        "John", "Steve", "Frank", "Kevin"
    ],
    "elf": [
        "Buddy", "Dobby", "Hermey", "Bing"
    ],
    "goblin": [
        "Iomysb", "Kreesz", "Sreakt", "Ur"
    ],
    "orc": [
        "Irt", "Hork", "Grig", "Lugz"
    ]
}
entity_last_names = {
    "human": [
        "Smith", "Martinez", "Foster", "Robinson"
    ],
    "elf": [
        "Celeborn", "Aestra", "Sauron", "Tobin"
    ],
    "goblin": [
        "Striediarx", "Wrehact", "Zresb", "Xakx"
    ],
    "orc": [
        "Whar", "Krugz", "Figg", "Quark"
    ]
}

# Overall Base Stat Boundries:
#   - Level         : 1-20
#   - Intelligence  : 1-10
#   - Perception    : 1-10
#   - Strength      : 1-10
#   - Defence       : 1-10
#   - Speed         : 1-10

entity_stats_base = {
    "human": {
        "max_health": 100,
        "intelligence": 8,
        "perception": 8,
        "strength": 6,
        "defence": 6,
        "speed": 6,
    },
    "elf": {
        "max_health": 80,
        "intelligence": 10,
        "perception": 10,
        "strength": 6,
        "defence": 6,
        "speed": 8,
    },
    "goblin": {
        "max_health": 60,
        "intelligence": 6,
        "perception": 4,
        "strength": 4,
        "defence": 4,
        "speed": 8,
    },
    "orc": {
        "max_health": 120,
        "intelligence": 4,
        "perception": 6,
        "strength": 10,
        "defence": 10,
        "speed": 4,
    }
}





# Character Management
# -------------------------------------------------------------

def GenerateEntity(presets = {}):
    new_entity = {}

    if ("level" in presets.keys()):
        new_entity["level"] = presets["level"]
    else:
        new_entity["level"] = 1

    if ("race" in presets.keys()):
        new_entity["race"] = presets["race"]
    else:
        AssignRandomEntityRace(new_entity)

    if ("name" in presets.keys()):
        new_entity["name"] = presets["name"]
    else:
        AssignRandomEntityName(new_entity)

    if ("stats" in presets.keys()):
        new_entity["stats"] = presets["stats"]
    else:
        AssignEntityDefaultStats(new_entity)

    return new_entity


def AssignRandomEntityRace(entity):
    entity["race"] = choice(entity_races)


def AssignRandomEntityName(entity):
    entity["name"] = {}
    entity["name"]["first"] = choice(entity_first_names[entity["race"]])
    entity["name"]["last"] = choice(entity_last_names[entity["race"]])


def AssignEntityDefaultStats(entity):
    entity["max_health"] = entity_stats_base[entity["race"]]["max_health"]
    entity["active_health"] = entity_stats_base[entity["race"]]["max_health"]

    entity["stats"] = {}
    entity["stats"]["intelligence"] = entity_stats_base[entity["race"]]["intelligence"] + randint(-1, floor(entity["level"] / 2))
    entity["stats"]["perception"] = entity_stats_base[entity["race"]]["perception"] + randint(-1, floor(entity["level"] / 2))
    entity["stats"]["strength"] = entity_stats_base[entity["race"]]["strength"] + randint(-1, floor(entity["level"] / 2))
    entity["stats"]["defence"] = entity_stats_base[entity["race"]]["defence"] + randint(-1, floor(entity["level"] / 2))
    entity["stats"]["speed"] = entity_stats_base[entity["race"]]["speed"] + randint(-1, floor(entity["level"] / 2))


def PrintEntityDetails(entity):
    print("Name:   " + entity["name"]["first"] + " " + entity["name"]["last"])
    print("Race:   " + entity["race"][0].upper() + entity["race"][1:])
    print("Level:  " + str(entity["level"]))
    print("Health: " + str(entity["active_health"]) + "/" + str(entity["max_health"]))
    print("Stats:")
    print("     Intelligence: " + str(entity["stats"]["intelligence"]))
    print("     Perception:   " + str(entity["stats"]["perception"]))
    print("     Strength:     " + str(entity["stats"]["strength"]))
    print("     Defence:      " + str(entity["stats"]["defence"]))
    print("     Speed:        " + str(entity["stats"]["speed"]))





# Health Management
# -------------------------------------------------------------

def GetEntityHealth(entity):
    health_info = {
        "max_health": entity["max_health"],
        "active_health": entity["active_health"],
        "health_as_percentage": (entity["active_health"] / entity["max_health"]) * 100
    }
    return health_info


def AlterEntityActiveHealth(entity, change_amount):
    entity["active_health"] += change_amount












player = GenerateEntity({
    "name": {
        "first": "Flargen",
        "last": "Barger"
    },
    "race": "human",
    "level": 1
})

super_goblin = GenerateEntity({
    "name": {
        "first": "Gobladonix",
        "last": "Supreme"
    },
    "race": "goblin",
    "level": 100
})

new_enemy_1 = GenerateEntity()
new_enemy_2 = GenerateEntity({"level": 5})
new_enemy_3 = GenerateEntity({"race": "orc"})



print()
print()
PrintEntityDetails(player)
print()
print()
PrintEntityDetails(new_enemy_1)
print()
print()
PrintEntityDetails(new_enemy_2)
print()
print()
PrintEntityDetails(new_enemy_3)
print()
print()
PrintEntityDetails(super_goblin)
