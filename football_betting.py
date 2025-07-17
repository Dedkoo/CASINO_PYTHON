import time
import random

class Football:

    def __init__(self) -> None:
        # Initialize team pools and other match state variables.
        # Add/remove as you wish.
        self.team_1 = ["MANCHESTER CITY","CHELSEA","BARCELONA"]
        self.team_2 = ["MANCHESTER UNITED","ARSENAL","REAL MADRID"]
        # If goal = 1 | if not 0
        self.is_goal = 1
        self.not_goal = 0
        # Random team picker for both teams.
        self.random_team_1 = random.choice(self.team_1)
        self.random_team_2 = random.choice(self.team_2)
        # Starting score.
        self.goals_1 = 0
        self.goals_2 = 0
        # Starting betting team.
        self.team_to_bet = ""
        # Random attack picker.
        self.attack_random = [self.team_1_match, self.team_2_match]

    def menu(self) -> tuple[str, int]:
        """"Display betting menu and get user input for team and bet amount."""
        print("\n-----WELCOME TO THE BETTING ARENA!-----\n")
        time.sleep(0.5)
        print("\nMATCH BEGINS!")
        print(f"\n| {self.random_team_1} - {self.goals_1} || {self.goals_2} - {self.random_team_2}|")
        self.choice_team = input("\nWHAT TEAM TO BET ON?: ").upper()
        if self.choice_team == self.random_team_1:
            print(f"\nYOU ARE BETTING ON: {self.random_team_1}")
            self.team_to_bet = self.random_team_1
        elif self.choice_team == self.random_team_2:
             print(f"\nYOU ARE BETTING ON: {self.random_team_2}")
             self.team_to_bet = self.random_team_2       
        
        self.choice_bet = int(input("\nHOW MUCH TO BET?: $"))
        
        
        print(f"\nYOU ARE BETTING ${self.choice_bet} ON {self.team_to_bet}")
        return self.team_to_bet, self.choice_bet
        

    def team_1_match(self) -> None:
        """Simulates an attack from Team 1."""
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

    def team_2_match(self) -> None:
        """Simulates an attack from Team 2."""
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
        
    def result(self) -> None:
        """Prints the result of the match."""
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

    def attack(self) -> None:
        """Randomly chooses a team to perform an attack."""
        random_choice = random.choice(self.attack_random)
        if random_choice == self.team_1_match:
            self.team_1_match()
        else:
            self.team_2_match()

    def play(self,balance: int) -> int:
        """Plays the football betting game and returns updated balance."""
        self.menu()
        if self.choice_bet <= 0:
            print("\nINVALID CHOICE! RETURNING TO MENU.")
            return balance

        # Match simulation
        for _ in range(6):
            time.sleep(0.5)
            self.attack()
            
        # Match results
        self.result()
        
        # Balance update
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