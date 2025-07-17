import random
import time

class Blackjack:

    def __init__(self) -> None:
        # All possible card values, 10 appears 4x (10, J, Q, K), 11 is Ace.
        self.random_numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        # Starting 2 cards for player and bot.
        self.player_cards = [random.choice(self.random_numbers) for _ in range(2)]
        self.bot_cards = [random.choice(self.random_numbers) for _ in range(2)]
        # 3rd card if player or bot chooses to.
        self.player_third_card = [random.choice(self.random_numbers)]
        self.bot_third_card = [random.choice(self.random_numbers)]
        # Random pick if bot wants 3rd card or not.
        self.bot_choices = [self.bot_third_card, 0]

    def play(self, balance: int) -> int | None:
        """
        Runs a single round of Blackjack game.
        Returns new balance or None if player quits.
        """
        time.sleep(1)
        print("\n-----WELCOME TO BLACKYJACKY!-----\n")
        time.sleep(1)
        
        # Get players bet. If 0 game quits.
        new_bet = int(input("\nHOW MUCH WOULD YOU LIKE TO BET? ENTER 0 TO QUIT: $"))
        if new_bet > balance:
            time.sleep(1)
            print("\nINVALID FUNDS!")
            return balance
        elif new_bet == 0:
            time.sleep(1)
            print("EXITING...")
            return
        else:
            time.sleep(1)
            (f"\nYOU ARE BETTING ${new_bet}!\n")

        # Show player cards and sum of two cards.
        time.sleep(1)
        print(f"\nPLAYER CARDS: {self.player_cards}")
        time.sleep(1)
        print(f"\nSUM: {sum(self.player_cards)}")

        # Show bot cards and sum of the first card that is visible. Second card is not visible only after game is finished.
        time.sleep(1)
        print(f"\nBOT CARDS: {self.bot_cards[0]} [?]")
        time.sleep(1)
        print(f"SUM: {self.bot_cards[0]}")

        # Choice for player if they want 3rd card.
        time.sleep(1)
        choice_third = input("\n3rd CARD?: (YES/NO): ").upper()

        if choice_third == "YES":
            final_two_player = [sum(self.player_cards)]
            final_player = list(map(lambda x, y: x + y, final_two_player, self.player_third_card))
            time.sleep(1)
            print(f"\nFINAL PLAYER CARDS: {sum(final_player)}")
        elif choice_third == "NO":
            final_two_player = [sum(self.player_cards)]
            final_player = list(map(lambda x, y: x + y, final_two_player, [0]))
            time.sleep(1)
            print(f"\nFINAL PLAYER CARDS: {sum(final_player)}")

        # Bot decision on third card
        bot_choice = random.choice(self.bot_choices)

        time.sleep(1)
        print(f"\nBOT CARDS: {self.bot_cards}\n")

        # Game outcome logic
        if bot_choice == self.bot_third_card:
            print(f"BOT HAS CHOSEN TO PICK 3rd CARD WITH VALUE OF: {self.bot_third_card}\n")
            final_two_bot = [sum(self.bot_cards)]
            final_bot = list(map(lambda x, y: x + y, final_two_bot, self.bot_third_card))
            time.sleep(1)
            print(f"\fFINAL BOT CARDS: {sum(final_bot)}")
        elif bot_choice == 0:
            final_two_bot = [sum(self.bot_cards)]
            final_bot = list(map(lambda x, y: x + y, final_two_bot, [0]))
            time.sleep(1)
            print(f"\nFINAL BOT CARDS: {sum(final_bot)}")

        if sum(final_player) > sum(final_bot) and sum(final_player) < 21:
            time.sleep(1)
            print("\nYOU WIN!")
            balance += new_bet
            time.sleep(1)
            print(f"\n{final_player} : {final_bot}")
            time.sleep(1)
            print(f"\nNEW BALANCE: {balance}")
            return balance
        elif sum(final_bot) > sum(final_player) and sum(final_bot) < 21:
            time.sleep(1)
            print("\nYOU LOST!")
            balance -= new_bet
            time.sleep(1)
            print(f"\n{sum(final_player)} : {sum(final_bot)}")
            time.sleep(1)
            print(f"\nNEW BALANCE: {balance}")
            return balance
        elif sum(final_player) and sum(final_bot) == 21:
            time.sleep(1)
            print("\nDOUBLE BLACKJACK!! TIE.")
        elif sum(final_player) == 21:
            time.sleep(1)
            print("\nPLAYER BLACKJACK! PLAYER WINS!")
            balance += new_bet
            time.sleep(1)
            print(f"\nNEW BALANCE: {balance}")
            return balance
        elif sum(final_bot) == 21:
            time.sleep(1)
            print("\nBOT BLACKJACK! BOT WINS!")
            balance -= new_bet
            time.sleep(1)
            print(f"\nNEW BALANCE: {balance}")
            return balance
        elif sum(final_player) > 21:
            time.sleep(1)
            print("\nMORE THAN 21! YOU LOSE!")
            balance -= new_bet
            time.sleep(1)
            print(f"\nNEW BALANCE: {balance}")
            return balance
        elif sum(final_bot) > 21:
            time.sleep(1)
            print("\nMORE THAN 21! YOU WIN!")
            balance += new_bet
            time.sleep(1)
            print(f"\nNEW BALANCE: {balance}")
            return balance
        elif sum(final_player) == sum(final_bot):
            time.sleep(1)
            print("TIE!")
