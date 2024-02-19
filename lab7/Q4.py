class Card:
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
       
        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, opponent_card):
        return self.attack - opponent_card.defense
