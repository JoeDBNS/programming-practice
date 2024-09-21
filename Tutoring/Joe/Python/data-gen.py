import random
import json

# Define lists for fake data generation
first_names = ["John", "Emily", "Alex", "Sophia", "Michael", "Sarah", "David", "Olivia", "James", "Ava", "Robert", "Isabella", "William", "Mia", "Daniel", "Amelia", "Joseph", "Grace", "Charles", "Chloe"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Moore", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson", "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall"]
positive_traits = ["brave", "loyal", "honest", "kind", "intelligent", "resourceful", "compassionate", "resilient", "determined", "curious", "charismatic", "humble", "generous", "creative", "patient", "diligent", "empathetic", "adventurous", "trustworthy"]
fears = ["heights", "darkness", "failure", "spiders", "snakes", "drowning", "public speaking", "death", "confined spaces", "fire", "flying", "ghosts", "blood", "abandonment", "thunderstorms", "insects", "needles", "germs", "clowns", "loneliness"]
weapons = ["stick", "axe", "baseball bat", "pistol", "shotgun", "rifle", "bow and arrow", "crossbow", "machete", "knife", "spear", "sledgehammer", "sword", "hammer", "crowbar", "chainsaw"]

fake_data = []
for i in range(50):
    friend_id = (i + 17) % 50

    entry = {
        "id": i,
        "first_name": random.choice(first_names),
        "last_name": random.choice(last_names),
        "age": random.randint(18, 80),
        "positive_trait": random.choice(positive_traits),
        "fear": random.choice(fears),
        "weapon": random.choice(weapons),
        "sanity": random.randint(0, 100),
        "friend": friend_id
    }
    fake_data.append(entry)

# Convert to JSON format
fake_data_json = json.dumps(fake_data, indent=4)
# fake_data_json

print(fake_data_json)