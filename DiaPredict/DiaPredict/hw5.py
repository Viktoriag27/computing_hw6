###########################################
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters (in addition to self, of course):
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes called "name" and "symptoms" respectively

# 1.2)
# Create a method called "add_test" which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

# 1.3)
# Create a method called has_covid() which takes no parameters.
# "has_covid" returns a float, between 0.0 and 1.0, which represents the probability of the patient to have Covid-19
#
# The probability should work as follows:
# 1. If the user has had the test "covid" then it should return .99 if the test is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05 and increases by 0.1 for each of the following symptoms:
#    ['fever', 'cough', 'anosmia']


class Patient:
    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        self.tests = {}                                   # 1.1) Creating a dictionary to store test results

    def add_test(self, test_name: str, result: bool):
        self.tests[test_name] = result                    # 1.2) Storing the test name and result

    def has_covid(self) -> float:
        if 'covid' in self.tests:
            return 0.99 if self.tests['covid'] else 0.01  # 1.3) Returning based on test result
    
        probability = 0.05  # Base probability
        for symptom in ['fever', 'cough', 'anosmia']:
            if symptom in self.symptoms:
               probability += 0.1  # Increasing probability if symptom is present
    
        return min(probability, 1.0)  # Ensuring the probability does not exceed 1.0
    
##EXAMPLE USAGE:

# Creating an instance of the Patient class
patient_1 = Patient(name="John Doe", symptoms=["fever", "cough"])

# Adding a covid test result
patient_1.add_test("covid", True)

# Displaying the patient's name and test results
print(f"Patient Name: {patient_1.name}")
print(f"Symptoms: {patient_1.symptoms}")
print(f"Test Results: {patient_1.tests}")

# Displaying the probability of the patient having covid
print(f"COVID Probability: {patient_1.has_covid()}")

##OUTPUT:
# Patient Name: John Doe
# Symptoms: ['fever', 'cough']
# Test Results: {'covid': True}
# COVID Probability: 0.99


######################
# 2. 
# In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.
    
import random

class Deck:
    def __init__(self):
        # Defining suits and values for the deck
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # Creating a list of Card objects for each suit and value
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle(self):
        # Shuffling the cards randomly
        random.shuffle(self.cards)
    
    def draw(self):
        # Draw a card from the deck, if available
        if self.cards:
            drawn_card = self.cards.pop()           # Removing the last card from the deck
            print(f"Drawn Card: {drawn_card}")      # Printing the suit and value of the drawn card
            return drawn_card                       # Returning the drawn card object 
        else:
            print("The deck is empty!")             # Informing the user if the deck is empty
            return None                             # Returning None if no cards are available

##EXAMPLE USAGE:
deck = Deck()                                       # Creates a deck
deck.shuffle()                                      # Shuffles the deck
deck.draw()                                         # Prints the suit and value of the drawn card

##Example Output: 
# Drawn Card: Q of Spades


###################
# 3. In this exercise you will create an interface that will serve as template for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimeter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

from abc import ABC, abstractmethod

class PlaneFigure(ABC):
    @abstractmethod
    def compute_perimeter(self):
        pass
    
    @abstractmethod
    def compute_surface(self):
        pass


# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

class Triangle(PlaneFigure):
    def __init__(self, base: float, c1: float, c2: float, h: float):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h
    
    def compute_perimeter(self):
        return self.base + self.c1 + self.c2
    
    def compute_surface(self):
        return 0.5 * self.base * self.h
    

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

class Rectangle(PlaneFigure):
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def compute_perimeter(self):
        return 2 * (self.a + self.b)
    
    def compute_surface(self):
        return self.a * self.b
    

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

import math

class Circle(PlaneFigure):
    def __init__(self, radius: float):
        self.radius = radius
    
    def compute_perimeter(self):
        return 2 * math.pi * self.radius
    
    def compute_surface(self):
        return math.pi * self.radius ** 2
    

##EXAMPLE USAGE
# Creating a Triangle object
triangle = Triangle(base=3, c1=4, c2=5, h=2)
print(f"Triangle Perimeter: {triangle.compute_perimeter()}")
print(f"Triangle Surface: {triangle.compute_surface()}")

# Creating a Rectangle object
rectangle = Rectangle(a=5, b=7)
print(f"Rectangle Perimeter: {rectangle.compute_perimeter()}")
print(f"Rectangle Surface: {rectangle.compute_surface()}")

# Creating a Circle object
circle = Circle(radius=3)
print(f"Circle Perimeter: {circle.compute_perimeter()}")
print(f"Circle Surface: {circle.compute_surface()}")    

##Output:
# Triangle Perimeter: 12
# Triangle Surface: 3.0
# Rectangle Perimeter: 24
# Rectangle Surface: 35
# Circle Perimeter: 18.84955592153876
# Circle Surface: 28.274333882308138

