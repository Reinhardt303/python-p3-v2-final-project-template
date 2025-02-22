from models.animal import Animal
from models.habitat import Habitat

from helpers import (
    exit_program,
    habitat_sub_menu,
    print_habitats,
    print_animals,
    animal_sub_menu,
    print_full_menu,
    main_menu,
)

def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            show_listed_habitats()        
        elif choice == "2":
            show_listed_animals()
        else:
            print("Invalid choice")

def view_animals_by_habitat():
    print_habitats()

    print("Please enter a habitat ID number: ")
    selection = input("> ")
    habitat = Habitat.find_by_id(int(selection))  
    if habitat:
        animals = habitat.animals()      
        if animals:
            for animal in animals:
                print(f"{animal.id} | {animal.name} | Habitat ID: {animal.habitat_id}")
        else:
            print(f"No animals found in that habitat")
    else:
        print(f"No habitat found with that ID")
    
    print_full_menu()

def choose_animal_by_id():
    search_id = input("Enter an animal's ID: ")
    animal = Animal.find_by_id(search_id)
    print(f"{animal.id } | {animal.name} | {animal.color} | {animal.predator} | Habitat ID: {animal.habitat_id}")
    animal_sub_menu()

def show_listed_habitats():
    print_habitats()   
    habitat_sub_menu()
    habitat_sub_menu_select()
    
def habitat_sub_menu_select():
    habitat_choice = input("> ")
    if habitat_choice == "0":
        exit_program()
    elif habitat_choice == "1":
        view_animals_by_habitat()
    elif habitat_choice == "2":
        add_habitat()
    elif habitat_choice == "3":
        remove_habitat()
    elif habitat_choice == "4":
        main_menu()
    else:
        print("Invalid choice") 
def show_listed_animals():
    print_animals()
    animal_sub_menu()
           
def add_animal():
    name = input("Enter a common name for the animal: ")
    color = input("Enter a color for the animal: ")
    predator = bool(input("Enter True or False for predator status: "))
    habitats = Habitat.get_all()
    for habitat in habitats:
        print(f"{habitat.id} | {habitat.name}")
    habitat_id = int(input("Enter a habitat ID: "))
    Animal.create(name, color, predator, habitat_id)
    print_animals()
    animal_sub_menu()

def add_habitat():
    name = input("Enter a name for the habitat: ")
    Habitat.create(name)
    print_habitats()   
    habitat_sub_menu()

def remove_habitat():
    habitat_id = input("Enter a habitat ID to delete: ")
    habitat = Habitat.find_by_id(int(habitat_id))
    Habitat.delete(habitat)
    print_habitats()   
    habitat_sub_menu()

def remove_animal():
    animal_id = input("Enter a animal ID to delete: ")
    animal = Animal.find_by_id(int(animal_id))
    Animal.delete(animal)
    print_animals()
    animal_sub_menu()

if __name__ == "__main__":
    main()
