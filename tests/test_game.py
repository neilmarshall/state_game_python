import unittest
import unittest.mock as mock

from game import Game


class TestGameWithMockData(unittest.TestCase):

    @mock.patch.object(Game, "load_data")
    def setUp(self, load_data_patch):
        load_data_patch.return_value = ['Iowa', 'Ohio', 'Utah']
        self.game = Game(None)
        
    def test_class_instantiation(self):
        self.assertListEqual(self.game.state_list, ['Iowa', 'Ohio', 'Utah'])

    @mock.patch('builtins.input')
    @mock.patch('builtins.print')
    @mock.patch.object(Game, "play_round")
    def test_class_run_method_without_continue(self, play_round_patch, print_patch, input_patch):
        input_patch.return_value = 'N'
        self.game.run()
        play_round_patch.assert_called_once()
        self.assertEqual(2, print_patch.call_count)
        self.assertEqual(1, input_patch.call_count)

    @mock.patch('builtins.input')
    @mock.patch('builtins.print')
    @mock.patch.object(Game, "play_round")
    def test_class_run_method_with_continue(self, play_round_patch, print_patch, input_patch):
        input_patch.side_effect = ['Y', 'N']
        self.game.run()
        self.assertEqual(2, play_round_patch.call_count)
        self.assertEqual(3, print_patch.call_count)
        self.assertEqual(2, input_patch.call_count)
        print_patch.assert_called_with("Game Exited!!!")

    @mock.patch('builtins.input')
    @mock.patch('builtins.print')
    def test_class_play_round_method_correct_guess_with_upper_case(self, print_patch, input_patch):
        input_patch.return_value = 'UTAH'
        self.game.play_round()
        print_patch.assert_called_with("Congratulations - you guessed 'Utah' correctly!!!")

    @mock.patch('builtins.input')
    @mock.patch('builtins.print')
    def test_class_play_round_method_correct_guess_with_lower_case(self, print_patch, input_patch):
        input_patch.return_value = 'utah'
        self.game.play_round()
        print_patch.assert_called_with("Congratulations - you guessed 'Utah' correctly!!!")

    @mock.patch('builtins.input')
    @mock.patch('builtins.print')
    def test_class_play_round_method_correct_guess_with_mismatched_case(self, print_patch, input_patch):
        input_patch.return_value = 'uTaH'
        self.game.play_round()
        print_patch.assert_called_with("Congratulations - you guessed 'Utah' correctly!!!")
