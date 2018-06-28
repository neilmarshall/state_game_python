"""
The aim of this program is to require users to name a US state that
begins with a specified letter.
"""

from game import Game


if __name__ == '__main__':
    game = Game("states.txt")
    game.run()
