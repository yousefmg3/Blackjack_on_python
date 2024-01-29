class Game:
    def __init__(self, player_credits):
        self.player_credits = player_credits
        self.deck = self.generate_deck()

    def generate_deck(self) -> dict:
            cards = ["Ace","King","Queen","Jack",10,9,8,7,6,5,4,3,2]
            value = [11,10,10,10,10,9,8,7,6,5,4,3,2]*4
            suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

            deck = {}
            
            for suit in suits:
                for i, card in enumerate(cards):
                    card_name = f'{card} of {suit}'
                    deck[card_name] = value[i]

            return deck

            
    