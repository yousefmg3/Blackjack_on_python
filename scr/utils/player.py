class Player:

    def __init__(self, name:str) -> None:
        self.name = name
        self.cards: dict = {}
        self.score = 0

    def add_cards(self, cards:dict):

        self.cards = self.cards|cards

        self.score = sum(self.cards.values())

        

        


