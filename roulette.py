import time
import random

class Roulette:

    def __init__(self):
        self.roulette = ["RED", "BLACK"]
        self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                        26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.one_to_eighteen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.nineteen_to_thirtysix = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.total = [self.one_to_eighteen, self.nineteen_to_thirtysix]
        self.one_twelve1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.one_twelve2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        self.one_twelve3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        self.total_one_twelve = [self.one_twelve1, self.one_twelve2, self.one_twelve3]
        self.two_to_one1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        self.two_to_one2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        self.two_to_one3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
        self.total_two_to_one = [self.two_to_one1, self.two_to_one2, self.two_to_one3]

    def play(self, balance):

            print("\n-----WELCOME TO THE GRAND ROULETTE!-----\n")
            time.sleep(1)
            new_bet = int(input("\nHOW MUCH WOULD YOU LIKE TO BET? ENTER 0 TO QUIT: $"))
            if new_bet > balance:
                time.sleep(1)
                print("\nINVALID FUNDS!")
                return balance
            elif new_bet == 0:
                time.sleep(1)
                print("EXITING...")
                return balance
            else:
                time.sleep(1)
                (f"\nYOU ARE BETTING ${new_bet}!\n")

            time.sleep(1)
            choice = input("\nWHAT TO BET ON? 1:COLOR - 2:EVEN/ODD - 3.18/36 - 4.12/12/12 - 5.JACKPOT - 6.2TO1: ")

            if choice == "1":
                time.sleep(1)
                choice = input("\nCHOOSE YOUR COLOR (RED-BLACK): ")
                if choice == "RED":
                    time.sleep(1)
                    print("\nYOU CHOSE COLOR RED!")
                elif choice == "BLACK":
                    time.sleep(1)
                    print("\nYOU CHOSE COLOR BLACK!")
                elif choice == "":
                    print("\nEXITING...")
                    time.sleep(1)
                    return 

                bot_choice = random.choice(self.roulette)
                time.sleep(1)
                print(f"\nBOT HAS CHOSEN: COLOR {bot_choice}!")

                if choice == bot_choice:
                    time.sleep(1)
                    print("\nYOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE IS: {balance}")
                    return balance
                else:
                    time.sleep(1)
                    print("\nYOU LOST!")
                    balance -= new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE IS: {balance}")
                    return balance

            elif choice == "2":
                time.sleep(1)
                choice_of_numbers = input("\nEVEN OR ODD NUMBER: ")
                bot_choice = random.choice(self.numbers)
                time.sleep(1)

                if choice_of_numbers == "EVEN" and bot_choice % 2 == 0:
                    time.sleep(1)
                    print(f"\nBOT HAS CHOSEN EVEN NUMBER: {bot_choice}")
                    time.sleep(1)
                    print("\nYOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                elif choice_of_numbers == "ODD" and bot_choice % 2 == 1:
                    time.sleep(1)
                    print(f"\nBOT HAS CHOSEN ODD NUMBER: {bot_choice}")
                    time.sleep(1)
                    print("\nYOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                else:
                    time.sleep(1)
                    print("\nYOU LOST!")
                    balance -= new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance

            elif choice == "3":
                choice = random.choice(self.total)
                time.sleep(1)
                player_choice = input("\nCHOOSE: 1. 18 - 2. 36: ")

                if choice == self.one_to_eighteen:
                    time.sleep(1)
                    print("\nBOT HAS CHOSEN 1-18!")
                elif choice == self.nineteen_to_thirtysix:
                    time.sleep(1)
                    print("\nBOT HAS CHOSEN 19-36!")

                if choice == self.one_to_eighteen and player_choice == "18":
                    time.sleep(1)
                    print("\nYOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                elif choice == self.nineteen_to_thirtysix and player_choice == "36":
                    time.sleep(1)
                    print("\nYOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                else:
                    print("\nYOU LOSE!")
                    time.sleep(1)
                    balance -= new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance

            elif choice == "4":
                choice_bot = random.choice(self.total_one_twelve)
                time.sleep(1)
                choice_player = input("\nCHOOSE: 1. 1-12 - 2. 13-24 - 3. 25-36: ")

                if choice_bot == self.one_twelve1:
                    time.sleep(1)
                    print("\nBOT HAS CHOSEN 1-12!")
                elif choice_bot == self.one_twelve2:
                    time.sleep(1)
                    print("\nBOT HAS CHOSEN 13-24")
                elif choice_bot == self.one_twelve3:
                    time.sleep(1)
                    print("\nBOT HAS CHOSEN 25-36")

                if choice_player == "1" and choice_bot == self.one_twelve1:
                    time.sleep(1)
                    print("\nYOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                elif choice_player == "2" and choice_bot == self.one_twelve2:
                    time.sleep(1)
                    print("YOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                elif choice_player == "3" and choice_bot == self.one_twelve3:
                    time.sleep(1)
                    print("\nYOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                else:
                    print("\nYOU LOSE!")
                    time.sleep(1)
                    balance -= new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance

            elif choice == "5":
                time.sleep(1)
                print("YOU CHOSE JACKPOT (0)!")
                player_choice = 0
                bot_choice = random.choice(self.numbers)
                print(f"BOT HAS CHOSEN NUMBER: {bot_choice}")
                if player_choice == bot_choice:
                    time.sleep(1)
                    print("YOU WIN JACKPOT!")
                    jackpot = new_bet * 20
                    balance += jackpot
                    time.sleep(1)
                    print(f"NEW BALANCE: {balance}")
                    return balance
                else:
                    time.sleep(1)
                    print("YOU LOST!")
                    balance -= new_bet
                    time.sleep(1)
                    print(f"NEW BALANCE: {balance}")
                    return balance

            elif choice == "6":
                time.sleep(1)
                choice = input("CHOOSE: 1.FIRST 2TO1 - 2.SECOND 2TO1 - 3. THIRD 2TO1: ")
                if choice == "1":
                    time.sleep(1)
                    print("YOU CHOSE FIRST 2TO1!")
                elif choice == "2":
                    time.sleep(1)
                    print("YOU CHOSE SECOND 2TO1!")
                    time.sleep(1)
                elif choice == "3":
                    time.sleep(1)
                    print("YOU CHOSE THIRD 2TO1!")

                bot_choice = random.choice(self.total_two_to_one)

                if choice == "1" and bot_choice == self.two_to_one1:
                    time.sleep(1)
                    print(f"BOT HAS CHOSEN: FIRST 2TO1!")
                    time.sleep(1)
                    print("YOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                elif choice == "2" and bot_choice == self.two_to_one2:
                    time.sleep(1)
                    print(f"BOT HAS CHOSEN: SECOND 2TO1!")
                    time.sleep(1)
                    print("YOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                if choice == "3" and bot_choice == self.two_to_one3:
                    time.sleep(1)
                    print(f"BOT HAS CHOSEN: THIRD 2TO1!")
                    time.sleep(1)
                    print("YOU WIN!")
                    balance += new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance
                else:
                    time.sleep(1)
                    print(f"BOT HAS CHOSEN: {bot_choice}")
                    time.sleep(1)
                    print("YOU LOST!")
                    balance -= new_bet
                    time.sleep(1)
                    print(f"\nNEW BALANCE: {balance}")
                    return balance


            elif choice == "":
                time.sleep(1)
                print("EXITING...")
                return