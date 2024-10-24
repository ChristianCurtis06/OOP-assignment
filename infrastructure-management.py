# Task 1: Vehicle Registration System
import re

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Owner for vehicle '{self.reg_num}' updated to '{new_owner}'.")

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added to event '{self.name}'.")

    def get_participant_count(self):
        print(f"Event: {self.name} - Participants: {self.participant_count}")

# Task 2: Event Management System Enhancement
vehicles = {}
events = {}

print("Welcome to the City Infrastructure Management System!")

while True:
    print("\n1. Register new vehicle\n2. Update vehicle owner\n3. Create new event\n4. Add event participant\n5. Display event participant count\n6. Exit")
    user_input = input("Enter your choice: ")
    
    try:
        if user_input == '1':
            reg_num_input = int(input("Enter the new vehicle's registration number: ").strip())
            if reg_num_input not in vehicles:
                type_input = input("Enter the new vehicle's type: ").strip().title()
                owner_input = input("Enter the new vehicle's owner: ").strip().title()
                vehicles[reg_num_input] = Vehicle(reg_num_input, type_input, owner_input)
                print(f"New vehicle '{reg_num_input}' registered.")
            else:
                print(f"Vehicle '{reg_num_input}' already exists.")
        elif user_input == '2':
            reg_num_input = int(input("Enter the new vehicle's registration number: "))
            if reg_num_input in vehicles:
                new_owner_input = input("Enter the vehicle's new owner: ").strip().title()
                vehicles[reg_num_input].update_owner(new_owner_input)
            else:
                print(f"Vehicle '{reg_num_input}' not found.")
        elif user_input == '3':
            name_input = input("Enter the new event's name: ").strip().title()
            if name_input not in events:
                date_input = input("Enter the new event's date (MM/DD/YYYY): ").strip()
                if re.search(r'\b\d{2}/\d{2}/\d{4}\b', date_input):
                    events[name_input] = Event(name_input, date_input)
                    print(f"New event '{name_input}' created.")
                else:
                    print("Invalid input. Please enter date in 'MM/DD/YYYY' format.")
            else:
                print(f"Event '{name_input}' already exists.")
        elif user_input == '4':
            name_input = input("Enter the event's name: ").strip().title()
            if name_input in events:
                events[name_input].add_participant()
            else:
                print(f"Event '{name_input}' not found.")
        elif user_input == '5':
            name_input = input("Enter the event's name: ").strip().title()
            if name_input in events:
                events[name_input].get_participant_count()
            else:
                print(f"Event '{name_input}' not found.")
        elif user_input == '6':
            print("Exiting the system...")
            break
        else:
            print("Invalid input. Please try again.")
    except ValueError:
        print("ValueError: Invalid input. Please enter an integer.")
    except Exception as e:
        print(f"An error occurred: {e}")