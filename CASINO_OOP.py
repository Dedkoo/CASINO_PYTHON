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


class Blackjack:

    def __init__(self):
        self.random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.player_cards = [random.choice(self.random_numbers) for _ in range(2)]
        self.bot_cards = [random.choice(self.random_numbers) for _ in range(2)]
        self.player_third_card = [random.choice(self.random_numbers)]
        self.bot_third_card = [random.choice(self.random_numbers)]
        self.bot_choices = [self.bot_third_card, 0]

    def play(self, balance):
        time.sleep(1)
        print("\n-----WELCOME TO BLACKYJACKY!-----\n")
        time.sleep(1)
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

        time.sleep(1)
        print(f"\nPLAYER CARDS: {self.player_cards}")
        time.sleep(1)
        print(f"\nSUM: {sum(self.player_cards)}")

        time.sleep(1)
        print(f"\nBOT CARDS: {self.bot_cards[0]} [?]")
        time.sleep(1)
        print(f"SUM: {self.bot_cards[0]}")

        time.sleep(1)
        choice_third = input("\n3rd CARD?: (YES/NO): ")

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

        bot_choice = random.choice(self.bot_choices)

        time.sleep(1)
        print(f"\nBOT CARDS: {self.bot_cards}\n")

        if bot_choice == self.bot_third_card:
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


class Machine:
    
    def __init__(self):
        self.symbols = ["🍇","🍉","🍒","🍊"]
                            
    def play(self,balance):
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
                
            random_symbol_row_one = [random.choice(self.symbols) for _ in range(3)]
            random_symbol_row_two = [random.choice(self.symbols) for _ in range(3)]
            random_symbol_row_three = [random.choice(self.symbols) for _ in range(3)]
        
            print(" | ".join(random_symbol_row_one))
            print(" | ".join(random_symbol_row_two))
            print(" | ".join(random_symbol_row_three))

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
            
class Football:

    def __init__(self):
        self.team_1 = ["MANCHESTER CITY","CHELSEA","BARCELONA"]
        self.team_2 = ["MANCHESTER UNITED","ARSENAL","REAL MADRID"]
        self.is_goal = 1
        self.not_goal = 0
        self.random_team_1 = random.choice(self.team_1)
        self.random_team_2 = random.choice(self.team_2)
        self.goals_1 = 0
        self.goals_2 = 0
        self.team_to_bet = ""
        self.attack_random = [self.team_1_match, self.team_2_match]

    def menu(self):
        print("\n-----WELCOME TO THE BETTING ARENA!-----\n")
        time.sleep(0.5)
        print("\nMATCH BEGINS!")
        print(f"\n| {self.random_team_1} - {self.goals_1} || {self.goals_2} - {self.random_team_2}|")
        choice_team = input("\nWHAT TEAM TO BET ON?: ")
        if choice_team == self.random_team_1:
            print(f"\nYOU ARE BETTING ON: {self.random_team_1}")
            self.team_to_bet = self.random_team_1
        elif choice_team == self.random_team_2:
             print(f"\nYOU ARE BETTING ON: {self.random_team_2}")
             self.team_to_bet = self.random_team_2
        
        self.choice_bet = int(input("\nHOW MUCH TO BET?: $"))

        print(f"\nYOU ARE BETTING ${self.choice_bet} ON {self.team_to_bet}")
        return self.team_to_bet, self.choice_bet
        

    def team_1_match(self):
        time.sleep(1)
        print(f"\n{self.random_team_1} IS ATTACKING!")
        if random.choice([self.is_goal, self.not_goal]) == self.is_goal:
            time.sleep(1)
            print(f"\n{self.random_team_1} HAS SCOOORED!")
            self.goals_1 += self.is_goal
            time.sleep(1)
            print(f"\nNEW SCORE: {self.goals_1}:{self.goals_2}")
        else:
            time.sleep(1)
            print(f"\n{self.random_team_1} HAS MISSED THE CHANGE!")
            time.sleep(1)
            print(f"\nSCORE REMAINS THE SAME!")    

    def team_2_match(self):
        time.sleep(1)
        print(f"\n{self.random_team_2} IS ATTACKING!")
        if random.choice([self.is_goal, self.not_goal]) == self.is_goal:
            time.sleep(1)
            print(f"\n{self.random_team_2} HAS SCOOORED!")
            self.goals_2 += self.is_goal
            time.sleep(1)
            print(f"\nNEW SCORE: {self.goals_1}:{self.goals_2}")
        else:
            time.sleep(1)
            print(f"\n{self.random_team_2} HAS MISSED THE CHANGE!")
            time.sleep(1)
            print(f"\nSCORE REMAINS THE SAME!")      
        
    def result(self):
        if self.goals_1 > self.goals_2:
            time.sleep(1)
            print(f"\n{self.random_team_1} HAS WON THE MATCH!")
            time.sleep(1)
            print(f"\nWITH SCORE OF {self.goals_1} : {self.goals_2}")
        elif self.goals_1 == self.goals_2:
            time.sleep(1)
            print(f"\nITS A TIE!")
            time.sleep(1)
            print(f"\nWITH SCORE OF {self.goals_1} : {self.goals_2}")
        else:
            time.sleep(1)
            print(f"\n{self.random_team_2} HAS WON THE MATCH!")
            time.sleep(1)
            print(f"\nWITH SCORE OF {self.goals_1} : {self.goals_2}")

    def attack(self):
        random_choice = random.choice(self.attack_random)
        if random_choice == self.team_1_match:
            self.team_1_match()
        else:
            self.team_2_match()

    def play(self,balance):
        self.menu()
        time.sleep(1)
        self.attack()
        time.sleep(1)
        self.attack()
        time.sleep(1)
        self.attack()
        time.sleep(1)
        self.attack()
        time.sleep(1)
        self.attack()
        time.sleep(1)
        self.attack()
        time.sleep(1)
        self.result()
        time.sleep(1)
        if self.team_to_bet == self.random_team_1 and self.goals_1 > self.goals_2:
            print("\nYOU WIN!")
            balance += self.choice_bet
        elif self.team_to_bet == self.random_team_1 and self.goals_1 == self.goals_2:
            print("\nTIE!")
            balance -= self.choice_bet
        elif self.team_to_bet == self.random_team_2 and self.goals_1 == self.goals_2:
            print("\nTIE!")
            balance -= self.choice_bet
        elif self.team_to_bet == self.random_team_1 and self.goals_1 < self.goals_2:
            print("\nYOU LOSE!")
            balance -= self.choice_bet
        elif self.team_to_bet == self.random_team_2 and self.goals_2 > self.goals_1:
            print("\nYOU WIN!")
            balance += self.choice_bet
        elif self.team_to_bet == self.random_team_1 and self.goals_2 < self.goals_1:
            print("\nYOU LOSE!")
            balance -= self.choice_bet
        
        print(f"\nYOUR NEW BALANCE IS ${balance}")
        return balance


        
    
class Casino:

    def __init__(self):
        self.account = 5000
        self.balance = 1000

    def show_account(self):
        time.sleep(1)
        print(f"\nYOUR BALANCE ON YOUR ACCOUNT IS: ${self.account}.")
        time.sleep(1)
        self.exiting_msg()
        time.sleep(1)
    
    def show_balance(self):
        time.sleep(1)
        print(f"\nYOUR CURRENT BALANCE IS: ${self.balance}.")
        time.sleep(1)
        self.exiting_msg()
        time.sleep(1)
    
    def show_credits(self):
        print("\n-----------------------------")
        time.sleep(1)
        print("-THIS CASINO WAS CREATED BY:-")
        time.sleep(1)
        print("----DAVID DROBNAK - DEDE-----")
        time.sleep(1)
        print("-----THANKS FOR PLAYING!-----")
        time.sleep(1)
        print("------------2025-------------")
        time.sleep(1)
        print("-----------------------------")
        time.sleep(1)
        self.exiting_msg()
        time.sleep(1)

    def exiting_msg(self):
        print("\nRETURNING TO MENU...")
        time.sleep(1)

    def deposit_func(self):
        time.sleep(1)
        deposit = int(input("\nHOW MUCH WOULD YOU LIKE TO DEPOSIT?: $"))
        if deposit > self.account:
            time.sleep(1)
            print("\nNOT ENOUGHT FUNDS!")
            time.sleep(1)
            self.exiting_msg()
        else:
            self.balance += deposit
            self.account -= deposit
            time.sleep(1)
            print(f"\nYOUR NEW BALANCE IS ${self.balance}")
            time.sleep(1)
            self.exiting_msg()
    
    def withdraw_func(self):
        time.sleep(1)
        withdraw_amount = int(input("\nHOW MUCH WOULD YOU LIKE TO WITHDRAW?: $"))
        if withdraw_amount > self.balance:
            print("\nNOT ENOUGHT FUNDS!")
        else:
            self.balance -= withdraw_amount
            self.account += withdraw_amount
            time.sleep(1)
            print(f"\nYOUR NEW ACCOUNT STATUS IS: ${self.account}")
            time.sleep(1)
            print(f"\nYOUR NEW BALANCE STATUS IS: ${self.balance}")
            time.sleep(1)
            self.exiting_msg()

    def run(self):
        while True:
            time.sleep(1)
            print("\n----DEDE CASINO----")
            print("1.GRAND ROULETTE")
            print("2.BLACKYJACKY")
            print("3.4 FRUITS")
            print("4.FOOTBALL BET")
            print("5.SHOW ACCOUNT")
            print("6.DEPOSIT")
            print("7.SHOW BALANCE")
            print("8.WITHDRAW")
            print("9.CREDITS")
            print("10.EXIT")
            print("-------------------")

            choice = input("\nPLEASE CHOOSE OPTION (1-10): ")


            if choice == "1":
                while True:
                    final_choice_roulette = input("1.TO PLAY GRAND ROULETTE 2.DEPOSIT FUNDS OR ENTER TO EXIT: ")
                    if final_choice_roulette:
                        roulette = Roulette()
                        self.balance = roulette.play(self.balance)
                    elif final_choice_roulette == "2":
                        self.deposit_func()
                    elif final_choice_roulette == "":
                        print("\nEXITING TO MAIN MENU...")
                        time.sleep(1)
                        break

            elif choice == "2":
                while True:
                    final_choice_blackjack = input("\n1.TO PLAY BLACKYJACKY 2.DEPOSIT FUNDS OR ENTER TO EXIT: ")
                    if final_choice_blackjack:
                        blackjack = Blackjack()
                        self.balance = blackjack.play(self.balance)
                    elif final_choice_blackjack == "2":
                        self.deposit_func()
                    elif final_choice_blackjack == "":
                        print("\nEXITING TO MAIN MENU...")
                        time.sleep(1)
                        break
            elif choice == "3":
                while True:
                    final_choice_machine = input("\n1.TO PLAY 4 FRUITS 2.DEPOSIT FUNDS OR ENTER TO EXIT: ")
                    if final_choice_machine == "1":    
                        machine = Machine()
                        self.balance = machine.play(self.balance)
                    elif final_choice_machine == "2":
                        self.deposit_func()
                    elif final_choice_machine == "":
                        print("\nEXITING TO MAIN MENU...")
                        time.sleep(1)
                        break
            elif choice == "4":
                while True:
                    final_choice_football = input("\n1.TO PLAY FOOTBALL BET 2.DEPOSIT FUNDS OR ENTER TO EXIT: ")
                    if final_choice_football == "1":
                        football = Football()
                        self.balance = football.play(self.balance)
                    elif final_choice_football == "2":
                        self.deposit_func()
                    elif final_choice_football == "":
                        print("\nEXITING TO MAIN MENU...")
                        time.sleep(1)
                        break
            elif choice == "5":
                self.show_account()
            elif choice == "7":
                self.show_balance()
            elif choice == "6":
                self.deposit_func()
            elif choice == "8":
                self.withdraw_func()
            elif choice == "9":
                self.show_credits()
            elif choice == "10":
                self.exiting_msg()
            elif choice == "v":
                print("VERSION: 1.1.0")   
                print("CHANGED TO OPP FORM.")
                print("ADDED MORE FUNCIONALITY AND OPTIONS TO GAMES.")
                print("UPDATED USER EXPERIENCE.") 
                
casino = Casino()
casino.run()

