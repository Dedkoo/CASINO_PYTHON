import time
import random

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