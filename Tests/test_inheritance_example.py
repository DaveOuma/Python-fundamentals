#!/usr/bin/python3

import unittest
from inheritance_example import Animal, Dog, Cat

class TestAnimal(unittest.TestCase):
    def test_animal_speak(self):
        animal = Animal()
        self.assertEqual(animal.speak(), "Animal speaks")

    def test_dog_speak(self):
        dog = Dog()
        self.assertEqual(dog.speak(), "Dog barks")

    def test_cat_speak(self):
        cat = Cat()
        self.assertEqual(cat.speak(), "Cat meows")

if __name__ == '__main__':
    unittest.main()
