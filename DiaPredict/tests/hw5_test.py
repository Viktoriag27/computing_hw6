# Importing necessary libraries
import sys
import os
import unittest  # Importing unittest module for writing unit tests

# Adding the parent directory to the system path so that modules from the parent folder can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(_file_), '..')))

# Importing classes to be tested from DiaPredict.hw5 module
from DiaPredict.hw5 import Patient, Card, Deck, Triangle, Rectangle, Circle

###########################################
# Test class for the Patient class
###########################################
class TestPatient(unittest.TestCase):
    
    # Test method for has_covid() with a positive test result
    def test_has_covid_with_positive_test(self):
        patient = Patient("Alice", ["fever"])  # Create a patient with symptom "fever"
        patient.add_test("covid", True)  # Adding a COVID test with a positive result
        self.assertEqual(patient.has_covid(), 0.99)  # Asserting that has_covid() returns 0.99 (high probability)

    # Test method for has_covid() with a negative test result
    def test_has_covid_with_negative_test(self):
        patient = Patient("Bob", ["cough"])  # Create a patient with symptom "cough"
        patient.add_test("covid", False)  # Adding a COVID test with a negative result
        self.assertEqual(patient.has_covid(), 0.01)  # Asserting that has_covid() returns 0.01 (low probability)

    # Test method for has_covid() without any test conducted
    def test_has_covid_without_test(self):
        patient = Patient("Charlie", ["fever", "cough"])  # Create a patient with multiple symptoms
        self.assertEqual(patient.has_covid(), 0.25)  # Asserting that has_covid() returns a default probability of 0.25

###########################################
# Test class for the Card class
class TestCard(unittest.TestCase):
    
    # Test method to check the string representation of a Card object
    def test_card_representation(self):
        card = Card("Hearts", "A")  # Creating an Ace of Hearts card
        self.assertEqual(str(card), "A of Hearts")  # Asserting that str(card) returns "A of Hearts"

###########################################
# Test class for the Deck class
class TestDeck(unittest.TestCase):
    
    # Test method to check that a new deck contains 52 cards
    def test_deck_initialization(self):
        deck = Deck()  # Creating a new Deck
        self.assertEqual(len(deck.cards), 52)  # Asserting that the deck has 52 cards

    # Test method to check that the deck can be shuffled and the order changes
    def test_deck_shuffle(self):
        deck = Deck()  # Creating a new Deck
        original_order = deck.cards[:]  # Storing the original order of cards
        deck.shuffle()  # Shuffling the deck
        self.assertNotEqual(original_order, deck.cards)  # Asserting that the order has changed after shuffling

    # Test method to draw a card from the deck
    def test_draw_card(self):
        deck = Deck()  # Creating a new Deck
        drawn_card = deck.draw()  # Drawing a card from the deck
        self.assertIsNotNone(drawn_card)  # Asserting that a card was drawn
        self.assertEqual(len(deck.cards), 51)  # Asserting that the deck now has 51 cards remaining

###########################################
# Test class for the Triangle class
class TestTriangle(unittest.TestCase):
    
    # Test method to calculate the perimeter of a Triangle
    def test_triangle_perimeter(self):
        triangle = Triangle(base=3, c1=4, c2=5, h=2)  # Creating a triangle with specified dimensions
        self.assertEqual(triangle.compute_perimeter(), 12)  # Asserting that the perimeter is correctly calculated

    # Test method to calculate the surface area of a Triangle
    def test_triangle_surface(self):
        triangle = Triangle(base=3, c1=4, c2=5, h=2)  # Creating a triangle with specified dimensions
        self.assertEqual(triangle.compute_surface(), 3.0)  # Asserting that the surface area is correctly calculated

###########################################
# Test class for the Rectangle class
class TestRectangle(unittest.TestCase):
    
    # Test method to calculate the perimeter of a Rectangle
    def test_rectangle_perimeter(self):
        rectangle = Rectangle(a=5, b=7)  # Creating a rectangle with specified dimensions
        self.assertEqual(rectangle.compute_perimeter(), 24)  # Asserting that the perimeter is correctly calculated

    # Test method to calculate the surface area of a Rectangle
    def test_rectangle_surface(self):
        rectangle = Rectangle(a=5, b=7)  # Creating a rectangle with specified dimensions
        self.assertEqual(rectangle.compute_surface(), 35)  # Asserting that the surface area is correctly calculated

###########################################
# Test class for the Circle class
class TestCircle(unittest.TestCase):
    
    # Test method to calculate the perimeter (circumference) of a Circle
    def test_circle_perimeter(self):
        circle = Circle(radius=3)  # Creating a circle with a specified radius
        self.assertAlmostEqual(circle.compute_perimeter(), 18.84955592153876, places=5)  # Asserting that the perimeter is close to expected value

    # Test method to calculate the surface area of a Circle
    def test_circle_surface(self):
        circle = Circle(radius=3)  # Creating a circle with a specified radius
        self.assertAlmostEqual(circle.compute_surface(), 28.274333882308138, places=5)  # Asserting that the surface area is close to expected value

# Running the unit tests when the script is executed directly
if _name_ == '_main_':
    unittest.main()