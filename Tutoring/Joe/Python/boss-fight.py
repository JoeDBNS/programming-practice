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
#   - Max Health
#   - Stats
#       - Level
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
    "other": [
        "placeholder"
    ],
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
    "other": [
        "placeholder"
    ],
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

entity_stats_base = {
    "other": {
        "max_health": 99,
        "intelligence": 7,
        "perception": 6,
        "strength": 7,
        "defence": 7,
        "speed": 7
    },
    "human": {
        "max_health": 100,
        "intelligence": 8,
        "perception": 8,
        "strength": 6,
        "defence": 6,
        "speed": 6
    },
    "elf": {
        "max_health": 80,
        "intelligence": 10,
        "perception": 10,
        "strength": 6,
        "defence": 6,
        "speed": 8
    },
    "goblin": {
        "max_health": 60,
        "intelligence": 6,
        "perception": 4,
        "strength": 4,
        "defence": 4,
        "speed": 8
    },
    "orc": {
        "max_health": 120,
        "intelligence": 4,
        "perception": 6,
        "strength": 10,
        "defence": 10,
        "speed": 4
    }
}





# Character Management
# -------------------------------------------------------------

def GenerateEntity(presets = {}):
    new_entity = {}

    if ("level" in presets):
        new_entity["level"] = presets["level"]
    else:
        new_entity["level"] = 1

    if ("race" in presets):
        new_entity["race"] = presets["race"]
    else:
        AssignRandomEntityRace(new_entity)

    if ("name" in presets):
        new_entity["name"] = presets["name"]
    else:
        AssignRandomEntityName(new_entity)

    if ("max_health" in presets):
        new_entity["max_health"] = presets["max_health"]
        new_entity["active_health"] = presets["max_health"]
    else:
        AssignEntityDefaultHealth(new_entity)

    if ("stats" in presets):
        new_entity["stats"] = presets["stats"]
    else:
        AssignEntityDefaultStats(new_entity)

    return new_entity


def AssignRandomEntityRace(entity):
    entity["race"] = choice(entity_races)


def AssignRandomEntityName(entity):
    entity["name"] = {}
    if entity["race"] in entity_races:
        entity["name"]["first"] = choice(entity_first_names[entity["race"]])
        entity["name"]["last"] = choice(entity_last_names[entity["race"]])
    else:
        entity["name"]["first"] = choice(entity_first_names["other"])
        entity["name"]["last"] = choice(entity_last_names["other"])


def AssignEntityDefaultHealth(entity):
    if entity["race"] in entity_races:
        entity["max_health"] = entity_stats_base[entity["race"]]["max_health"]
        entity["active_health"] = entity_stats_base[entity["race"]]["max_health"]
    else:
        entity["max_health"] = entity_stats_base["other"]["max_health"]
        entity["active_health"] = entity_stats_base["other"]["max_health"]


def AssignEntityDefaultStats(entity):
    entity["stats"] = {}
    
    if entity["race"] in entity_races:
        entity["stats"]["intelligence"] = entity_stats_base[entity["race"]]["intelligence"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["perception"] = entity_stats_base[entity["race"]]["perception"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["strength"] = entity_stats_base[entity["race"]]["strength"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["defence"] = entity_stats_base[entity["race"]]["defence"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["speed"] = entity_stats_base[entity["race"]]["speed"] + randint(-1, floor(entity["level"] / 2))
    else:
        entity["stats"]["intelligence"] = entity_stats_base["other"]["intelligence"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["perception"] = entity_stats_base["other"]["perception"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["strength"] = entity_stats_base["other"]["strength"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["defence"] = entity_stats_base["other"]["defence"] + randint(-1, floor(entity["level"] / 2))
        entity["stats"]["speed"] = entity_stats_base["other"]["speed"] + randint(-1, floor(entity["level"] / 2))


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





# Fight Management
# -------------------------------------------------------------

def Fight(player, enemy):
    while player["active_health"] > 0 and enemy["active_health"] > 0:
        PlayRound(player, enemy)

        print()
        print("Your Remaining Health: " + str(GetEntityHealth(player)["health_as_percentage"]) + "%")
        print("Enemy Remaining Health: " + str(GetEntityHealth(enemy)["health_as_percentage"]) + "%")
        print()

    ConcludeFight()


def PlayRound(player, enemy):
    player_move_choice = input("Attack or Defend? (A/D)").lower()
    enemy_move_choice = choice(["a", "d"])

    if player["stats"]["speed"] > enemy["stats"]["speed"]:
        print("player goes first....")
        PlayAttack(player, enemy, player_move_choice, enemy_move_choice)

        if enemy["active_health"] > 0:
            print("enemy goes second....")
            PlayAttack(enemy, player, enemy_move_choice, player_move_choice)

    else:
        print("enemy goes first....")
        PlayAttack(enemy, player, enemy_move_choice, player_move_choice)

        if player["active_health"] > 0:
            print("player goes second....")
            PlayAttack(player, enemy, player_move_choice, enemy_move_choice)


def PlayAttack(entity_attacker, entity_attackee, move_attacker, move_attackee):
    print(entity_attacker["name"]["first"] + " " + entity_attacker["name"]["last"] + " -- " + move_attacker + " / " + move_attackee + " -- " + entity_attackee["name"]["first"] + " " + entity_attackee["name"]["last"])

    attack_power = 0

    if move_attacker == "a":
        attack_power += 10

        if move_attackee == "d":
            attack_power = floor(attack_power / 2)
        
        AlterEntityActiveHealth(entity_attackee, -attack_power)


def ConcludeFight():
    if player["active_health"] <= 0:
        print("You've Lost.")
    else:
        print("You've Won!")





# Player Creation
# -------------------------------------------------------------

def CreatePlayerCharacter():
    create_player_manually = input("Would you like to manually create your playey? (Y/N)\n").lower()

    if create_player_manually == "y":
        remaining_stat_points = 34

        print("\n\n\nCreate your player character...")

        player_first_name = input("First Name: ")
        player_last_name = input("Last Name: ")
        player_race = input("Race: ").lower()

        print("\nNow for your stats.... (Intelligence, Perception, Strength, Defence, Speed)\n")

        print("Total Stat Points Available:", remaining_stat_points)
        player_stat_intelligence = int(input("\nIntelligence: "))
        remaining_stat_points -= player_stat_intelligence

        if remaining_stat_points > 0:
            print("Total Stat Points Remaining:", remaining_stat_points)
            player_stat_perception = int(input("\nPerception: "))
            remaining_stat_points -= player_stat_perception
        else:
            player_stat_perception = 0

        if remaining_stat_points > 0:
            print("Total Stat Points Remaining:", remaining_stat_points)
            player_stat_strength = int(input("\nStrength: "))
            remaining_stat_points -= player_stat_strength
        else:
            player_stat_strength = 0

        if remaining_stat_points > 0:
            print("Total Stat Points Remaining:", remaining_stat_points)
            player_stat_defence = int(input("\nDefence: "))
            remaining_stat_points -= player_stat_defence
        else:
            player_stat_defence = 0

        if remaining_stat_points > 0:
            player_stat_speed = remaining_stat_points
        else:
            player_stat_speed = 0


        return GenerateEntity({
            "name": {
                "first": player_first_name,
                "last": player_last_name
            },
            "race": player_race,
            "stats": {
                "intelligence": player_stat_intelligence,
                "perception": player_stat_perception,
                "strength": player_stat_strength,
                "defence": player_stat_defence,
                "speed": player_stat_speed,
            }
        })

    else:
        return GenerateEntity({
            "name": {
                "first": "Flargen",
                "last": "Barger"
            },
            "race": "human"
        })











player = CreatePlayerCharacter()


super_goblin = GenerateEntity({
    "name": {
        "first": "Gobladonix",
        "last": "Supreme"
    },
    "race": "goblin",
    "level": 100
})

new_enemy_1 = GenerateEntity()
new_enemy_2 = GenerateEntity({
    "name": {
        "first": "Unga",
        "last": "Boonga"
    },
    "level": 5
})
new_enemy_3 = GenerateEntity({"race": "orc"})



print()
print()
PrintEntityDetails(player)
# print()
# print()
# PrintEntityDetails(new_enemy_1)
# print()
# print()
# PrintEntityDetails(new_enemy_2)
# print()
# print()
# PrintEntityDetails(new_enemy_3)
print()
print()
PrintEntityDetails(super_goblin)


print()
print()
print()
print()


Fight(player, super_goblin)