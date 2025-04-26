class ControlMessages:
    WELCOME_MESSAGE = (
        "Welcome to Logic Solver v1.0\n"
        "Currently supported features:\n"
        "\t - Verify if a statement form is a tautology\n"
        "Commands you can use:\n"
        "\t - _s: input syntax\n"
        "\t - _n: mathematical notation list\n"
        "\t - _e: some examples\n"
    )
    SYNTAX_MESSAGE = (
        "A statement form always consists of logic variables, connectives and parentheses\n"
        "A logic variable should start with a uppercase letter followed by letters, numbers and underscores\n"
        "All components should be separated by a space\n"
        "The input statement and all sub-statements are expected to be properly included in parentheses\n"
    )
    COMMAND_MESSAGE = (
        "Logic connectives:\n"
        "\t Negation: \\not\n"
        "\t Conjunction: \\and\n"
        "\t Disjunction: \\or\n"
        "\t Implication: \\imply\n"
        "\t Bicondition: \\iff\n"
        "\n"
        "Logic quantifiers:\n"
        "\t For all: \\forall\n"
        "\t Exists: \\exists\n"
    )
    EXAMPLE_MESSAGE = (
        "> ( ( ( B \\or C ) \\and ( C \\and D ) ) \\imply ( B \\or C ) )\n"
        "True\n"
    )