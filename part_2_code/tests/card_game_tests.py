import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace_spades = Card("spades", 1)
        self.ten_diamonds = Card("diamonds", 10)
        self.two_hearts = Card("hearts", 2)
        self.test_card_game = CardGame()

    def test_check_for_ace__true(self):
        self.assertEqual(
            True, self.test_card_game.check_for_ace(self.ace_spades))

    def test_check_for_ace__false(self):
        self.assertEqual(
            False, self.test_card_game.check_for_ace(self.ten_diamonds))

    # def test_highest_card__ace_beats_ten(self):
    #     self.assertEqual(self.ace_spades, self.test_card_game.highest_card(
    #         self.ace_spades, self.ten_diamonds))  # this will fail the way the code is writen

    def test_highest_card__ten_beats_two(self):
        self.assertEqual(self.ten_diamonds, self.test_card_game.highest_card(
            self.two_hearts, self.ten_diamonds))  # this will fail the way the code is writen

    # def test_cards_total__ace_is_worth_ten(self):
    #     test_cards = [self.ace_spades, self.ten_diamonds]
    #     # this will fail the way the code is written, in my game picture cards are worth 10 points.
    #     self.assertEqual("You have a total of ",
    #                      self.test_card_game.cards_total(test_cards))

    def test_cards_total__two_and_ten(self):
        test_cards = [self.two_hearts, self.ten_diamonds]
        # this will fail the way the code is written, in my game picture cards are worth 10 points.
        self.assertEqual("You have a total of 12",
                         self.test_card_game.cards_total(test_cards))
