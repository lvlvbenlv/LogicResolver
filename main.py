from first_order_logic.statement import *
from utils.tokens import *
from utils.messages import *

def wait_for_query():
    while True:
        query = input("> ")
        if query in vars(Commands).values():
            proceed_command(query)
        else:
            statement = StatementForm(query)
            print(statement.is_tautology())

def proceed_command(command):
    if command == Commands.SYNTAX:
        print(ControlMessages.SYNTAX_MESSAGE)
    elif command == Commands.NOTATION:
        print(ControlMessages.COMMAND_MESSAGE)
    elif command == Commands.EXAMPLE:
        print(ControlMessages.EXAMPLE_MESSAGE)

if __name__ == '__main__':
    print(ControlMessages.WELCOME_MESSAGE)
    wait_for_query()