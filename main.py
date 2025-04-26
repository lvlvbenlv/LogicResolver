from statement import *
from symbols import *
from messages import *

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
        print(ControlMessages.COMMAND_MESSAGE)

if __name__ == '__main__':
    print(ControlMessages.WELCOME_MESSAGE)
    wait_for_query()