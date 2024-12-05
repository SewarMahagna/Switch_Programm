import random
from card import Card


class Board:
    def __init__(self, size):
        self.size = size
        self.cards = [Card(i) for i in range(size//2) for _ in range(2)]
        random.shuffle(self.cards)

    def display_board(self):
        for i, card in enumerate(self.cards):
            if card.face_up:
                print(f"{card.value:2}", end=" ")
            else:
                print(" *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()
