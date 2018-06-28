import unittest
import unittest.mock as mock

from game import Game

class TestGameWithMockData(unittest.TestCase):

    @mock.patch.object(Game, "load_data")
    def setUp(self, game_patch):
        game_patch.return_value = ['Iowa', 'Ohio', 'Utah']
        self.game = Game()
        
    def test_class_instantiation(self):
        self.assertListEqual(self.game.state_list, ['Iowa', 'Ohio', 'Utah'])
