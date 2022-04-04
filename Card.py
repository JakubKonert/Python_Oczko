class Card:
    def __init__(self, value, shape, cost):
        self.value = value
        self.shape = shape
        self.cost = cost


    def show(self):
        print('┌───────┐')
        print(f'| {self.value}    |')
        print('|       |')
        print(f'|   {self.shape}   |')
        print('|       |')
        print(f'|    {self.value} |')
        print('└───────┘') 