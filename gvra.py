class CardHand:
    """Class representing a hand of cards"""

    class _Card:
        """Class representing a single card"""
        suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
        ranks= ['Ace','2','3','4','5','6','7','8','9','10','11','Jack', 'Queen', 'King']

        def __init__(self,suit,rank):
            self._suit = suit
            self._rank = rank

        def __str__(self):
            return self._rank + ' ' + self._suit


    def __init__(self):
        self._hand = PositionalList()
        self._size = 0

    def _validate(self,s,r):
        card = self._Card(s,r)
        if not card._suit in s:
            raise ValueError("Such card doesn't exist")
        if not card._rank in r:
            raise ValueError("Invalid card value")
        return card

    def add_card(self,s,r):
            return  self._hand.add_first(self._Card(s,r))
ch = CardHand()
print(CardHand.add_card('ch','s', '4'))