import time
import random

class Machine:
    
    def __init__(self) -> None:
        # Symbols for the game.
        self.symbols= ["🍇","🍉","🍒","🍊"]
                            
    def play(self,balance: int) -> int:
        """
        Run a game of 4 Fruits slot machine.
        Accepts player's current balance and returns the updated balance.
        """
        time.sleep(1)
        print("\n-----WELCOME TO 4 FRUITS!-----\n")
        time.sleep(1)
        while True:
            new_bet = int(input("\nHOW MUCH TO BET?: "))
            if new_bet > balance:
                print("\nINVALID FUNDS!")
                return balance
            elif new_bet == 0:
                print("EXITING 4 FRUITS...")
                return balance
            else:
                (f"\nYOU ARE BETTING ${new_bet}!\n")

            # Generate 3x3 symbols.
            random_symbol_row_one = [random.choice(self.symbols) for _ in range(3)]
            random_symbol_row_two = [random.choice(self.symbols) for _ in range(3)]
            random_symbol_row_three = [random.choice(self.symbols) for _ in range(3)]
        
            # Display slot machine.
            print(" | ".join(random_symbol_row_one))
            print(" | ".join(random_symbol_row_two))
            print(" | ".join(random_symbol_row_three))
            
            # Check win conditions: rows and diagonals
            if random_symbol_row_one[0] == random_symbol_row_one[1] == random_symbol_row_one[2] or random_symbol_row_two[0] == random_symbol_row_two[1] == random_symbol_row_two[2] or random_symbol_row_three[0] == random_symbol_row_three[1] == random_symbol_row_three[2]:
                print("\nYOU WIN!\n")
                win = new_bet * 3
                balance += win
                print(f"NEW BALANCE: {balance}")
            elif random_symbol_row_one[0] == random_symbol_row_two[1] == random_symbol_row_three[2] or random_symbol_row_three[0] == random_symbol_row_two[1] == random_symbol_row_one[2]:
                print("\nYOU WIN!\n")
                win = new_bet * 3
                balance += win
                print(f"NEW BALANCE: {balance}")
            else:
                print("\nYOU LOSE!\n")
                balance -= new_bet
                print(f"NEW BALANCE: {balance}")