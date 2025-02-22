from models.__init__ import CONN, CURSOR
from models.animal import Animal
from models.habitat import Habitat

def seed_database():
    Animal.drop_table()
    Habitat.drop_table()
    Habitat.create_table()
    Animal.create_table()

    ocean = Habitat.create("Ocean")
    forest = Habitat.create("Forest")
    Animal.create("Dolphin", "Silver", True, ocean.id)
    Animal.create("Turtle", "Green", False, ocean.id)
    Animal.create("Owl", "Brown", True, forest.id)
    Animal.create("Chipmunk", "Brown", False, forest.id)
    Animal.create("Elk", "Brown", False, forest.id)


seed_database()
print("Seeded database")