from board import Board

class dealer():
    def __init__(self,board_size):
        self.board_size  = board_size
        self.board=Board(board_size)

    def play(self):
        turns = 0
        pairs_found = 0

        while pairs_found < self.board_size // 2:
            self.display_board()
            
            card1, card2 = self.get_card()
            self.isvalid_card(card1,card2)

            self.flip_card(card1,card2)

            self.display_board()

            self.check_cards(card1,card2,pairs_found)

            turns += 1

        print(f"Congratulations! You completed the game in {turns} turns.")

    def get_card(self):
        index1 = int(input("Enter the index of the first card: "))
        index2 = int(input("Enter the index of the second card: "))
        return index1,index2
    
    def isvalid_card(self,card1,card2):
        if card1 >= self.board_size or card2 >= self.board_size :
            raise IndexError(f"Card index is out of range. Valid indices are 0 to {self.board_size - 1}.")


    def flip_card(self,index1,index2):
        self.board.cards[index1].flip()
        self.board.cards[index2].flip()
    
    def check_cards(self,card1,card2,pairs_found):
        if self.board.cards[card1].value == self.board.cards[card2].value:
            print("Match found!")
            pairs_found += 1
        else:
            print("No match. Try again.")
            self.flip_card(card1,card2)

    def display_board(self):
        self.board.display_board()