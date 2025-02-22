from models.habitat import Habitat

def main_menu():
    print("Main Menu - Please select an option:")
    print('1: Show listed habitats')
    print("2: Show listed animals")
    print("0. Exit the program")

def habitat_sub_menu():
    print("Please select an option:")
    print("1: View animals by habitat")
    print("2: Add a habitat")
    print("3: Remove a habitat")
    print("4: Update a habitat")
    print("5: Exit to Main Menu")
    print("0. Exit the program")

    from cli import (
    view_animals_by_habitat,
    add_habitat,
    remove_habitat,
    update_habitat
    )

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
        update_habitat()
    elif habitat_choice == "5":
        main_menu()
    else:
        print("Invalid choice") 

def animal_sub_menu():
    print("Please select an option:")
    print("1: View animals by habitat")
    print("2: Select an animal by its ID")
    print("3: Add an animal")
    print("4: Remove an animal")
    print("5: Update an animal")
    print("6: Exit to Main Menu")
    print("0. Exit the program")
    
    animal_choice = input("> ")
    from cli import (
    view_animals_by_habitat,
    add_animal,
    remove_animal,
    choose_animal_by_id,
    update_animal
    )

    if animal_choice == "0":
        exit_program()
    elif animal_choice == "1":
        view_animals_by_habitat()
    elif animal_choice == "2":
        choose_animal_by_id()
    elif animal_choice == "3":
        add_animal()
    elif animal_choice == "4":
        remove_animal()
    elif animal_choice == "5":
        update_animal()
    elif animal_choice == "6":
        main_menu()
    else:
        print("Invalid choice")

def print_full_menu():
    print("Please select an option:")
    print("1: View animals by habitat")
    print("2: Add an animal")
    print("3: Select an animal by its ID")
    print("4: Remove an animal")
    print("5: Add a habitat")
    print("6: Remove a habitat")
    print("7: Exit to Main Menu")
    print("0. Exit the program")

    from cli import (
    view_animals_by_habitat,
    add_habitat,
    remove_habitat,
    add_animal,
    remove_animal,
    choose_animal_by_id
    )
    
    choice = input("> ")
    if choice == "0":
        exit_program()
    elif choice == "1":
        view_animals_by_habitat()
    elif choice == "2":
        add_animal()
    elif choice == "3":
        choose_animal_by_id()
    elif choice == "4":
        remove_animal()
    elif choice == "5":
        add_habitat()
    elif choice == "6":
        remove_habitat()
    elif choice == "7":
        main_menu()
    else:
        print("Invalid choice")

def print_habitats():
    habitats = Habitat.get_all()
    for habitat in habitats:
        print(f"Habitat ID: {habitat.id} | {habitat.name}")

def print_animals():
    habitats = Habitat.get_all()
    for habitat in habitats:
        animals_in_habitat = habitat.animals()
        for animal in animals_in_habitat:
            print(f"Animal ID: {animal.id } | {animal.name}")

def exit_program():
    print("Goodbye!")
    exit()
