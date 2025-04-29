class Commands:
    HEAD = "_"
    SYNTAX = "_s"
    NOTATION = "_n"
    EXAMPLE = "_e"

class Delimiters:
    L_PAREN = "("
    R_PAREN = ")"
    L_BRACE = "{"
    R_BRACE = "}"

    @classmethod
    def is_delimiter(cls, ch):
        return ch in {value for name, value in cls.__dict__.items() if
                      not name.startswith("__") and not callable(value)}

class Symbols:
    HEAD = "\\"

class Connectives(Symbols):
    NOT = "\\not"
    AND = "\\and"
    OR = "\\or"
    IMPLY = "\\imply"
    IFF = "\\iff"
    PRIORITY = [IFF, IMPLY, OR, AND, NOT]

class Quantifiers(Symbols):
    FORALL = "\\forall"
    EXISTS = "\\exists"

class SetSymbols(Symbols):
    MID = "\\mid"
    IN = "\\in"
    SUBSET = "\\subset"
    INTERSECT = "\\intersect"
    UNION = "\\union"
    DIFFERENCE = "\\difference"
