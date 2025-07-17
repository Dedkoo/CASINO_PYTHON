from football_betting import Football
from slot_machine import Machine
from blackjack import Blackjack
from roulette import Roulette
import time

class Casino:

    def __init__(self) -> None:
        """Initializing casino with starting account and balance budget."""
        # Account status.
        self.account = 5000
        # Casino balance status.
        self.balance = 1000

    def show_account(self) -> None:
        """Display user`s account status."""
        time.sleep(1)
        print(f"\nYOUR BALANCE ON YOUR ACCOUNT IS: ${self.account}.")
        time.sleep(1)
        self.exiting_msg()
        time.sleep(1)
    
    def show_balance(self) -> None:
        """"Display casino balance status."""
        time.sleep(1)
        print(f"\nYOUR CURRENT BALANCE IS: ${self.balance}.")
        time.sleep(1)
        self.exiting_msg()
        time.sleep(1)
    
    def show_credits(self) -> None:
        """Show credits and developer info."""
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

    def exiting_msg(self) -> None:
        """Display returning message."""
        print("\nRETURNING TO MENU...")
        time.sleep(1)

    def deposit_func(self):
        """"Handles transactions from account to balance."""
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
    
    def withdraw_func(self) -> None:
        """Handles withdraw from balance to account."""
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

    def run(self) -> None:
        """Run the casino main loop and menu."""
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

