from models.habitat import Habitat

def main_menu():
    print("Main Menu - Please select an option:")
    print('1: Show listed habitats')
    print("2: Show listed animals")
    print("3: Add an animal")
    print("4: Add a habitat")
    print("0. Exit the program")

def habitat_sub_menu():
    print("Please select an option:")
    print("1: View animals by habitat")
    print("2: Add a habitat")
    print("3: Remove a habitat")
    print("4: Exit to Main Menu")
    print("0. Exit the program")
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
        pass
    else:
        print("Invalid choice") 

def animal_sub_menu():
    print("Please select an option:")
    print("1: View animals by habitat")
    print("2: Add an animal")
    print("3: Remove an animal")
    print("4: Add a habitat")
    print("5: Remove a habitat")
    print("6: Exit to Main Menu")
    print("0. Exit the program")
    
    animal_choice = input("> ")
    if animal_choice == "0":
        exit_program()
    elif animal_choice == "1":
        view_animals_by_habitat()
    elif animal_choice == "2":
        add_animal()
    elif animal_choice == "3":
        remove_animal()
    elif habitat_choice == "4":
        add_habitat()
    elif habitat_choice == "5":
        remove_habitat()
    elif animal_choice == "6":
        pass
    else:
        print("Invalid choice")

def print_full_menu():
    print("Please select an option:")
    print("1: View animals by habitat")
    print("2: Add an animal")
    print("3: Remove an animal")
    print("4: Exit to Main Menu")
    print("0. Exit the program")
    
    animal_choice = input("> ")
    if animal_choice == "0":
        exit_program()
    elif animal_choice == "1":
        view_animals_by_habitat()
    elif animal_choice == "2":
        add_animal()
    elif animal_choice == "3":
        remove_animal()
    elif animal_choice == "4":
        pass
    else:
        print("Invalid choice")

def print_habitats():
    habitats = Habitat.get_all()
    for habitat in habitats:
        print(f"{habitat.id} | {habitat.name}")

def print_animals():
    habitats = Habitat.get_all()
    for habitat in habitats:
        animals_in_habitat = habitat.animals()
        for animal in animals_in_habitat:
            print(f"{animal.id } | {animal.name} | {animal.color} | {animal.predator} | Habitat ID: {animal.habitat_id}")

def exit_program():
    print("Goodbye!")
    exit()
