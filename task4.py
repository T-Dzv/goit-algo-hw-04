def main():
    contact_book = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        try:
            if command in ["close", "exit"]:
                print("Good bye!")
                break
            elif command == "hello":
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contact_book))
            elif command == "change":
                print(change_contact(args, contact_book))
            elif command == "phone":
                print(show_phone(args, contact_book))
            elif command == "all":
                print(show_all(contact_book))
            else:
                print("Invalid command.")
        except ValueError:
            print("Invalid command.")

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contact_book: dict):
    name, phone = args
    if name in contact_book:
        return f"{name} is already in contact book"
    else:
        contact_book[name] = phone
        return "Contact added."

def change_contact(args: list, contact_book: dict):
    name, phone = args
    if name in contact_book:
        contact_book[name] = phone
        return "Contact updated."
    else:
        return f"There is no {name} in contact book"

def show_phone(args: list, contact_book: dict):
    name = args[0]
    if name in contact_book:
        return contact_book[name]
    else:
        return f"There is no {name} in contact book"

def show_all(contact_book):
    if contact_book: 
        contact_book_str = ""
        for name, phone in contact_book.items():
            contact_book_str += f"{name}: {phone}\n"
        return contact_book_str
    else:
        return "Contact book is empty"

if __name__ == "__main__":
    main()
