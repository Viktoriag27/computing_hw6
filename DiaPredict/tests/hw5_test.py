# Import necessary libraries for system and file handling
import sys
import os
import unittest

# Modify the Python path to include the parent directory to allow imports from other modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import specific classes from the DiaPredict.hw5 module for testing
from DiaPredict.hw5 import Patient, Card, Deck, Triangle, Rectangle, Circle

###########################################
# Define a test class for the Patient class
###########################################
class TestPatient(unittest.TestCase):
    
    # Test if the patient is likely to have COVID when they test positive
    def test_has_covid_with_positive_test(self):
        patient = Patient("Alice", ["fever"])  # Create a patient with symptoms
        patient.add_test("covid", True)  # Add a positive COVID test
        self.assertEqual(patient.has_covid(), 0.99)  # Check expected COVID probability

    # Test if the patient is likely not to have COVID when they test negative
    def test_has_covid_with_negative_test(self):
        patient = Patient("Bob", ["cough"])  # Create a patient with symptoms
        patient.add_test("covid", False)  # Add a negative COVID test
        self.assertEqual(patient.has_covid(), 0.01)  # Check expected COVID probability

    # Test COVID probability when no test has been added, based on symptoms alone
    def test_has_covid_without_test(self):
        patient = Patient("Charlie", ["fever", "cough"])  # Create a patient with multiple symptoms
        self.assertEqual(patient.has_covid(), 0.25)  # Check expected default probability

# Define a test class for the Card class
class TestCard(unittest.TestCase):
    
    # Test the string representation of a card instance
    def test_card_representation(self):
        card = Card("Hearts", "A")  # Create a card instance
        self.assertEqual(str(card), "A of Hearts")  # Check if the card is represented correctly

# Define a test class for the Deck class
class TestDeck(unittest.TestCase):
    
    # Test if the deck initializes with 52 cards
    def test_deck_initialization(self):
        deck = Deck()  # Create a deck instance
        self.assertEqual(len(deck.cards), 52)  # Check that the deck has 52 cards

    # Test if the deck's order changes after shuffling
    def test_deck_shuffle(self):
        deck = Deck()  # Create a deck instance
        original_order = deck.cards[:]  # Copy the original order
        deck.shuffle()  # Shuffle the deck
        self.assertNotEqual(original_order, deck.cards)  # Ensure the deck's order is changed

    # Test if drawing a card reduces the deck size by one
    def test_draw_card(self):
        deck = Deck()  # Create a deck instance
        drawn_card = deck.draw()  # Draw a card from the deck
        self.assertIsNotNone(drawn_card)  # Check that a card was drawn
        self.assertEqual(len(deck.cards), 51)  # Check the deck size decreased by one

# Define a test class for the Triangle class
class TestTriangle(unittest.TestCase):
    
    # Test if the triangle perimeter calculation is correct
    def test_triangle_perimeter(self):
        triangle = Triangle(base=3, c1=4, c2=5, h=2)  # Create a triangle instance with specified sides
        self.assertEqual(triangle.compute_perimeter(), 12)  # Verify the perimeter calculation

    # Test if the triangle surface area calculation is correct
    def test_triangle_surface(self):
        triangle = Triangle(base=3, c1=4, c2=5, h=2)  # Create a triangle instance with specified dimensions
        self.assertEqual(triangle.compute_surface(), 3.0)  # Verify the surface area calculation

# Define a test class for the Rectangle class
class TestRectangle(unittest.TestCase):
    
    # Test if the rectangle perimeter calculation is correct
    def test_rectangle_perimeter(self):
        rectangle = Rectangle(a=5, b=7)  # Create a rectangle instance with specified sides
        self.assertEqual(rectangle.compute_perimeter(), 24)  # Verify the perimeter calculation

    # Test if the rectangle surface area calculation is correct
    def test_rectangle_surface(self):
        rectangle = Rectangle(a=5, b=7)  # Create a rectangle instance with specified dimensions
        self.assertEqual(rectangle.compute_surface(), 35)  # Verify the surface area calculation

# Define a test class for the Circle class
class TestCircle(unittest.TestCase):
    
    # Test if the circle perimeter (circumference) calculation is correct
    def test_circle_perimeter(self):
        circle = Circle(radius=3)  # Create a circle instance with specified radius
        self.assertAlmostEqual(circle.compute_perimeter(), 18.84955592153876, places=5)  # Verify circumference

    # Test if the circle surface area calculation is correct
    def test_circle_surface(self):
        circle = Circle(radius=3)  # Create a circle instance with specified radius
        self.assertAlmostEqual(circle.compute_surface(), 28.274333882308138, places=5)  # Verify surface area

# Run all the tests if the script is executed directly
if __name__ == '__main__':
    unittest.main()
