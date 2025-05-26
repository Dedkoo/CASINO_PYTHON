import random
import time

team_1 = ["MANCHESTER CITY","CHELSEA","BARCELONA"]
team_2 = ["MANCHESTER UNITED","ARSENAL","REAL MADRID"]
is_goal = 1
not_goal = 0
random_numbers = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
symbols = ["🍇","🍉","🍒","🍀"]
choices_of_roulette = ["BLACK","RED"]
account = 5000
balance = 0


while True:

    print("\n----DEDE CASINO----")
    print("1.ROULETTE")
    print("2.SLOT MACHINE")
    print("3.BLACKJACK")
    print("4.SPORT BETTING")
    print("5.SHOW ACCOUNT")
    print("6.DEPOSIT")
    print("7.SHOW BALANCE")
    print("8.WITHDRAW")
    print("9.CREDITS")
    print("10.EXIT")
    print("-------------------")

    choice = input("\nENTER WHAT YOU WANT TO DO: (1-10): \n")

    if choice == "1":
        print("---WELCOME TO THE GRAND ROULLETE!---")
        player_choice = input("\nENTER YOUR CHOICE (RED/BLACK) OR ENTER TO RETURN TO MAIN MENU: \n")

        if player_choice == "BLACK":
            time.sleep(1)
            print("\nYOU CHOSE BLACK.\n")
        elif player_choice == "RED":
            time.sleep(1)
            print("\nYOU CHOSE RED.\n")

        elif player_choice == "":
            print("THANKS FOR PLAYING! RETURNING TO MENU.")
            time.sleep(1)
            continue

        else:
            print("INVALID INPUT! RETURNING TO MENU.")
            time.sleep(1)
            continue

        new_bet = int(input("HOW MUCH TO BET?: "))
        time.sleep(1)
        if new_bet > balance:
            print("\nINVALID FUNDS!")
            continue
        else:
            print(f"\nYOU ARE BETTING ${new_bet}!\n")

        computer_choice = random.choice(choices_of_roulette)
        time.sleep(1)
        print(f"COMPUTER HAS CHOSEN!: {computer_choice}\n")

        if player_choice == computer_choice:
            time.sleep(1)
            print("YOU HAVE WON!")
            balance += new_bet
            print(f"NEW BALANCE: {balance}")
            time.sleep(1)

        else:
            time.sleep(1)
            print("YOU HAVE LOST!")
            balance -= new_bet
            print(f"NEW BALANCE: {balance}")

    elif choice == "2":
                while True:
                    print("\n---WELCOME TO 4 FRUITS!---")
                    print("\n1.MAKE A BET")
                    print("2.EXIT 4 FRUITS!\n")
                    menu_1_choice = input("ENTER YOUR CHOICE (1-2): ")

                    if menu_1_choice == "1":
                        time.sleep(1)
                        new_bet = int(input("HOW MUCH TO BET?: "))
                        time.sleep(1)
                        if new_bet > balance:
                            print("\nINVALID FUNDS!")
                            continue
                        else:
                            print(f"\nYOU ARE BETTING ${new_bet}!\n")

                        random_symbol = [random.choice(symbols) for _ in range(3)]

                        print(" | ".join(random_symbol))

                        if random_symbol[0] == random_symbol[1] == random_symbol[2]:
                            time.sleep(1)
                            print("YOU WIN!")
                            balance += new_bet
                            time.sleep(1)
                            print(f"NEW BALANCE: {balance}")
                        else:
                            time.sleep(1)
                            print("YOU LOSE!")
                            balance -= new_bet
                            time.sleep(1)
                            print(f"NEW BALANCE: {balance}")

                    elif menu_1_choice == "2":
                        print("\nEXITING!")
                        time.sleep(1)
                        break

                    else:
                        print("INVALID CHOICE!")
                        continue
    
    elif choice == "3":
                time.sleep(1)  
                while True:
                    print("\n---WELCOME TO BLACKYJACKY!---")
                    print("\n1.MAKE A BET.")
                    print("2.EXIT")
                    menu_2_choice = input("\nENTER YOUR CHOICE (1-2): ")

                    if menu_2_choice == "1":
                        choices_player = [random.choice(random_numbers) for _ in range(2)]
                        total_player = sum(choices_player)
                        choices_bot = [random.choice(random_numbers) for _ in range(2)]
                        total_bot = sum(choices_bot)
                        new_bet = int(input("\nHOW MUCH TO BET?: "))
                        if new_bet > balance:
                            print("\nINVALID FUNDS!")
                            continue
                        else:
                            print(f"\nYOU ARE BETTING ${new_bet}!\n")

                        print(f"PLAYER CARDS: {choices_player} | TOTAL: {total_player}")
                        print(f"BOT CARDS: {choices_bot} | TOTAL: {total_bot}\n")

                        if total_player and total_bot == 21:
                            print("DOUBLE BLACKAJACK! ITS A TIE.")
                            print(f"YOUR BALANCE IS: {balance}")
                        elif total_player == 21:
                            print("PLAYER BLACKJACK! PLAYER WINS.")
                            balance += new_bet
                            print(f"YOUR BALANCE IS: {balance}")
                        elif total_bot == 21:
                            print("BOT BLACKJACK! BOT WINS.")
                            balance -= new_bet
                            print(f"YOUR BALANCE IS: {balance}")
                        elif total_player > total_bot:
                            print("PLAYER WINS!")
                            balance += new_bet
                            print(f"YOUR BALANCE IS: {balance}")
                        elif total_player == total_bot:
                            print("TIE!")
                            print(f"YOUR BALANCE IS: {balance}")
                        else:
                            print("BOT WINS!")
                            balance -= new_bet
                            print(f"YOUR BALANCE IS: {balance}")
                    elif menu_2_choice == "2":
                        print("\nEXITING...")
                        time.sleep(1)
                        break
    elif choice == "4":
                time.sleep(1)
                while True:
                    print("\n---WELCOME TO SPORT BETTING ARENA!---")
                    print("\n1.MAKE A BET")
                    print("2.EXIT")
                    menu_3_choice = input("\nENTER YOUR CHOICE (1-2): ")

                    goals_1 = 0
                    goals_2 = 0
                    random_team_1 = random.choice(team_1)
                    random_team_2 = random.choice(team_2)

                    if menu_3_choice == "1":
                        time.sleep(1)
                        print(f"\nTEAM PLAYING TODAY: | {random_team_1} VS {random_team_2} |")
                        time.sleep(1)
                        new_bet = int(input("\nHOW MUCH TO BET?: "))
                        time.sleep(1)
                        team_to_bet = input("ON WHAT TEAM TO BET? (ENTER FULL NAME OF A TEAM): ")
                        if team_to_bet not in [random_team_1,random_team_2]:
                            print("\nINVALID CHOICE!")
                            continue
                        if new_bet > balance:
                            print("\nINVALID FUNDS!")
                            continue
                        else:
                            print(f"\nYOU ARE BETTING ${new_bet}!\n")
                    

                        print("MATCH BEGINS!")
                        print(f"| {random_team_1} - {goals_1} || {goals_2} - {random_team_2}|")

                        time.sleep(1)
                        print(f"\n{random_team_1} IS ATTACKING!")
                        time.sleep(1)
                        if random.choice([is_goal, not_goal]) == is_goal:
                            time.sleep(1)
                            print(f"\n{random_team_1} HAS SCOOORED!")
                            goals_1 += is_goal
                            time.sleep(0.5)
                            print(f"\nNEW SCORE: {goals_1}:{goals_2}")
                        else:
                            time.sleep(1)
                            print(f"\n{random_team_1} HAS MISSED THE CHANGE!")
                            time.sleep(0.5)
                            print(f"\nSCORE REMAINS THE SAME!")

                        time.sleep(1)
                        print(f"\n{random_team_2} IS ATTACKING!")
                        time.sleep(1)
                        if random.choice([is_goal, not_goal]) == is_goal:
                            time.sleep(1)
                            print(f"\n{random_team_2} HAS SCOOORED!")
                            goals_2 += is_goal
                            time.sleep(0.5)
                            print(f"\nNEW SCORE: {goals_1}:{goals_2}")
                        else:
                            time.sleep(1)
                            print(f"\n{random_team_2} HAS MISSED THE CHANGE!")
                            time.sleep(0.5)
                            print(f"\nSCORE REMAINS THE SAME!")

                        time.sleep(1)
                        print(f"\n{random_team_1} IS ATTACKING!")
                        time.sleep(1)
                        if random.choice([is_goal, not_goal]) == is_goal:
                            time.sleep(1)
                            print(f"\n{random_team_1} HAS SCOOORED!")
                            goals_1 += is_goal
                            time.sleep(0.5)
                            print(f"\nNEW SCORE: {goals_1}:{goals_2}")
                        else:
                            time.sleep(1)
                            print(f"\n{random_team_1} HAS MISSED THE CHANGE!")
                            time.sleep(0.5)
                            print(f"\nSCORE REMAINS THE SAME!")

                        time.sleep(1)
                        print(f"\n{random_team_2} IS ATTACKING!")
                        time.sleep(1)
                        if random.choice([is_goal, not_goal]) == is_goal:
                            time.sleep(1)
                            print(f"\n{random_team_2} HAS SCOOORED!")
                            goals_2 += is_goal
                            time.sleep(0.5)
                            print(f"\nNEW SCORE: {goals_1}:{goals_2}")
                        else:
                            time.sleep(1)
                            print(f"\n{random_team_2} HAS MISSED THE CHANGE!")
                            time.sleep(0.5)
                            print(f"\nSCORE REMAINS THE SAME!")

                        time.sleep(1)
                        print(f"\n{random_team_1} IS ATTACKING!")
                        time.sleep(1)
                        if random.choice([is_goal, not_goal]) == is_goal:
                            time.sleep(1)
                            print(f"\n{random_team_1} HAS SCOOORED!")
                            goals_1 += is_goal
                            time.sleep(0.5)
                            print(f"\nNEW SCORE: {goals_1}:{goals_2}")
                        else:
                            time.sleep(1)
                            print(f"\n{random_team_1} HAS MISSED THE CHANGE!")
                            time.sleep(0.5)
                            print(f"\nSCORE REMAINS THE SAME!")

                        time.sleep(1)
                        print(f"\n{random_team_2} IS ATTACKING!")
                        time.sleep(1)
                        if random.choice([is_goal, not_goal]) == is_goal:
                            time.sleep(1)
                            print(f"\n{random_team_2} HAS SCOOORED!")
                            goals_2 += is_goal
                            time.sleep(0.5)
                            print(f"\nNEW SCORE: {goals_1}:{goals_2}")
                        else:
                            time.sleep(1)
                            print(f"\n{random_team_2} HAS MISSED THE CHANGE!")
                            time.sleep(0.5)
                            print(f"\nSCORE REMAINS THE SAME!")

                        if goals_1 > goals_2:
                            time.sleep(1)
                            print(f"\n{random_team_1} HAS WON THE MATCH!")
                            time.sleep(0.5)
                            print(f"\nWITH SCORE OF {goals_1} : {goals_2}")
                        elif goals_1 == goals_2:
                            time.sleep(1)
                            print(f"\nITS A TIE!")
                            time.sleep(0.5)
                            print(f"\nWITH SCORE OF {goals_1} : {goals_2}")
                        else:
                            time.sleep(1)
                            print(f"\n{random_team_2} HAS WON THE MATCH!")
                            time.sleep(0.5)
                            print(f"\nWITH SCORE OF {goals_1} : {goals_2}")

                        if team_to_bet == random_team_1 and goals_1 > goals_2:
                            balance += new_bet
                            time.sleep(1)
                            print("\nYOU HAVE WON!")
                            time.sleep(0.5)
                            print(f"NEW BALANCE IS: {balance}")
                        elif team_to_bet == random_team_2 and goals_2 > goals_1:
                            balance += new_bet
                            time.sleep(1)
                            print("\nYOU HAVE WON!")
                            time.sleep(0.5)
                            print(f"NEW BALANCE IS: {balance}")
                        elif team_to_bet != random_team_1 or goals_2 > goals_1:
                            balance -= new_bet
                            time.sleep(1)
                            print("\nYOU HAVE LOST!")
                            time.sleep(0.5)
                            print(f"NEW BALANCE IS: {balance}")
                        elif team_to_bet != random_team_2 or goals_1 > goals_2:
                            balance -= new_bet
                            time.sleep(1)
                            print("\nYOU HAVE LOST!")
                            time.sleep(0.5)
                            print(f"NEW BALANCE IS: {balance}")
                        else:
                            balance -= new_bet
                            time.sleep(1)
                            print("\nYOU HAVE LOST!")
                            time.sleep(0.5)
                            print(f"NEW BALANCE IS: {balance}")
                    


                    if menu_3_choice == "2":
                        print("\nEXITING...")
                        time.sleep(1)
                        break

    elif choice == "5":
        time.sleep(1)
        print(F"\nYOUR ACCOUNT STATUS: ${account}")

    elif choice == "6":
        time.sleep(1)
        get_balance = int(input("\nHOW MUCH TO DEPOSIT?: $"))

        time.sleep(1)
        if get_balance > account:
            print("NOT ENOUGH FUNDS IN ACCOUNT!")
        else:
            balance += get_balance
            account -= get_balance
            print(f"\nAMOUNT OF ${get_balance} WAS DEPOSITED!")
            print(f"YOUR NEW BALANCE IS: ${balance}")
            print(f"YOUR NEW ACCOUNT BALANCE IS: ${account}")

    elif choice == "7":
        time.sleep(1)
        print(f"\nYOUR BALANCE IS: {balance}")

    elif choice == "8":
        time.sleep(1)
        withdraw_amount = int(input("\nHOW MUCH WOULD YOU LIKE TO WITHDRAW?: $\n"))

        if withdraw_amount > balance:
            time.sleep(1)
            print("\nNOT ENOUGH FUNDS IN ACCOUNT!")
        else:
            time.sleep(1)
            print(f"\nAMOUNT OF ${withdraw_amount} WAS WITHDRAWN!")
            balance -= withdraw_amount
            account += withdraw_amount

    elif choice == "9":
        print("\n-----------------------------")
        print("-THIS CASINO WAS CREATED BY:-")
        print("----DAVID DROBNAK - DEDE-----")
        print("-----THANKS FOR PLAYING!-----")
        print("-----------------------------")
        

    elif choice == "10":
        time.sleep(1)
        print("\nEXITING DEDE`S CASINO")
        time.sleep(1)
        print("THANKS FOR PLAYING!")
        time.sleep(1)
        break

    elif choice == "v":
        print("VERSION 1.0.0")
        print("FIRST VERSION OF CASINO.")

