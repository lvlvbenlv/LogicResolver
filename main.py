from statement import *
from symbols import *

def welcome_message():
    print("Welcome to Logic Solver v1.0")
    print("Currently supported features:")
    print("\t - Basic propositional logic")
    print("\t - Set theory")
    print("Commands you can use:")
    print("\t - _n: mathematical notation list")
    print()

def wait_for_query():
    while True:
        query = input("> ")
        if query in vars(Commands).values():
            proceed_command(query)
        else:
            statement = Statement(query)
            print(statement.components)
            print(statement.all_pairs())
            print(statement.initialize_bst())

def proceed_command(command):
    if command == Commands.NOTATION:
        print("NOTATION")

if __name__ == '__main__':
    welcome_message()
    wait_for_query()