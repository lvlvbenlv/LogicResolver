class Statement:

    def __init__(self, statement):
        self.components = statement.split()
        self.value = False