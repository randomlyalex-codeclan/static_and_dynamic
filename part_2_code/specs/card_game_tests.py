import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.ace_spades = Card("spades", 1)
        self.ten_diamonds = Card("diamonds", 10)

    def test_check_for_ace__true(self):
        self.assertEqual(True, CardGame.check_for_ace(self.ace_spades))

    def test_check_for_ace__false(self):
        self.assertEqual(False, CardGame.check_for_ace(self.ten_diamonds))

    def test_highest_card__ace_beats_ten(self):
        self.assertEqual(self.ace_spades, CardGame.highest_card(
            self.ace_spades, self.ten_diamonds))  # this will fail the way the code is written

    def test_cards_total__ace_is_worth_ten(self):
        test_cards = [self.ace_spades, self.ten_diamonds]
        # this will fail the way the code is written, in my game picture cards are worth 10 points.
        self.assertEqual(20, CardGame.cards_total(test_cards))
