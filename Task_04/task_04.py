from pathlib import Path

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args
    
    for key, value in contacts.items():
        if key == name:
            return f'{name} {value}'
             
def show_all(contacts):
    result = []
    for key, value in contacts.items():
        result.append(f'{key} {value}')
    return '\n'.join(result)

def main():
    contacts ={}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args[0], contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")
    print(contacts) 
if __name__ == "__main__":
    main()
    
 