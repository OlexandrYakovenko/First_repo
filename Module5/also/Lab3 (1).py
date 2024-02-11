import sys
# print(__file__)
# print(sys.argv[0])
# if len(sys.argv)==2:
#     fname=sys.argv[1]
#     with open(fname,"r") as file:
#         print(file.read())
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def show_phone(args, contacts):
    name=args[0]
    if name in contacts:
        return contacts[name]
    return 'Not found'
    


def main():
    contacts = {'John':"123", 'Jane':"234", 'Steve':"555"}  #    [{'name':'John Doe', 'phone':'+380988858880'},
                        #{'name':'Alice Cooper', 'phone':'+48880884215'}]
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()