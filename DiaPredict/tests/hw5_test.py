import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DiaPredict.hw5 import Patient, Card, Deck, Triangle, Rectangle, Circle

###########################################
class TestPatient(unittest.TestCase):
    
    def test_has_covid_with_positive_test(self):
        patient = Patient("Alice", ["fever"])
        patient.add_test("covid", True)
        self.assertEqual(patient.has_covid(), 0.99)

    def test_has_covid_with_negative_test(self):
        patient = Patient("Bob", ["cough"])
        patient.add_test("covid", False)
        self.assertEqual(patient.has_covid(), 0.01)

    def test_has_covid_without_test(self):
        patient = Patient("Charlie", ["fever", "cough"])
        self.assertEqual(patient.has_covid(), 0.25)

class TestCard(unittest.TestCase):
    
    def test_card_representation(self):
        card = Card("Hearts", "A")
        self.assertEqual(str(card), "A of Hearts")

class TestDeck(unittest.TestCase):
    
    def test_deck_initialization(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_deck_shuffle(self):
        deck = Deck()
        original_order = deck.cards[:]
        deck.shuffle()
        self.assertNotEqual(original_order, deck.cards)  

    def test_draw_card(self):
        deck = Deck()
        drawn_card = deck.draw()
        self.assertIsNotNone(drawn_card)
        self.assertEqual(len(deck.cards), 51) 

class TestTriangle(unittest.TestCase):
    
    def test_triangle_perimeter(self):
        triangle = Triangle(base=3, c1=4, c2=5, h=2)
        self.assertEqual(triangle.compute_perimeter(), 12)

    def test_triangle_surface(self):
        triangle = Triangle(base=3, c1=4, c2=5, h=2)
        self.assertEqual(triangle.compute_surface(), 3.0)

class TestRectangle(unittest.TestCase):
    
    def test_rectangle_perimeter(self):
        rectangle = Rectangle(a=5, b=7)
        self.assertEqual(rectangle.compute_perimeter(), 24)

    def test_rectangle_surface(self):
        rectangle = Rectangle(a=5, b=7)
        self.assertEqual(rectangle.compute_surface(), 35)

class TestCircle(unittest.TestCase):
    
    def test_circle_perimeter(self):
        circle = Circle(radius=3)
        self.assertAlmostEqual(circle.compute_perimeter(), 18.84955592153876, places=5)

    def test_circle_surface(self):
        circle = Circle(radius=3)
        self.assertAlmostEqual(circle.compute_surface(), 28.274333882308138, places=5)

if __name__ == '__main__':
    unittest.main()