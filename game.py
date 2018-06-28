"""
This module contains the Game class, which runs the game.
"""

import os
import random


class Game():

    def __init__(self, fpath):
        """Class constructor - reads states into a list"""
        self.state_list = Game.load_data(fpath)

    @staticmethod
    def load_data(fpath):
        with open(fpath) as states:
            state_list = [state.strip() for state in states]
        random.shuffle(state_list)
        return state_list

    def run(self):
        """
        Function to control running the game - launches once (if states deque
        not empty) and subsequently loops as long as user indicates they want
        to continue
        """
        play_again_choice = 'Y'
        while self.state_list and play_again_choice in ['Y', 'y']:
            os.system("clear")
            self.play_round()
            print("Play again? ('Y' / 'y' to continue, any other key to exit)")
            play_again_choice = input(">>> ")
        print("Game Exited!!!")

    def play_round(self):
        """
        Function to play an individual round - called by 'run' repeatedly; reads
        a state and prompts user to guess the state (compares guess again state
        on a case-less basis for simplicity)
        """ 
        countdown = 0
        state = self.state_list.pop()

        while countdown < len(state):
            countdown += 1;
            print("Identify the state: " + state[:countdown] + "___")
            guess = input(">>> ")
            os.system("clear")
            if guess.lower() == state.lower():
                break
            print("You guessed " + guess + " - that is not correct. ",
                  "Please guess again")
        
        if guess.lower() == state.lower():
            print("Congratulations - you guessed '" + state + "' correctly!!!")
        else:
            print("Unlucky - you did not guess '" + state,
                  "' - better luck next time!!!")
