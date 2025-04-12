'''In the code above, the cake factory class and methods 
are defined. Now its time to define the unittest methods 
to test the different functions of the code. The test suite 
includes tests for the cakes flavor, size, toppings, 
ingredients, and price. The first test case in the suite will 
intentionally provide the wrong value—and thats 
what we want! Create specific statements to make sure the 
program is behaving as it should. That includes providing 
incorrect data to determine if the program will provide 
failed results. Because unittest is class-based,  
encapsulate these statements into test methods. '''

import unittest
import CakeFactory

class TestCakeFactory(unittest.TestCase):
 def test_create_cake(self):
   cake = CakeFactory.CakeFactory("vanilla", "small")
   self.assertEqual(cake.cake_type, "vanilla")
   self.assertEqual(cake.size, "small")
   self.assertEqual(cake.price, 8) # Vanilla cake, small size

 def test_add_topping(self):
     cake = CakeFactory.CakeFactory("chocolate", "large")
     cake.add_topping("sprinkles")
     self.assertIn("sprinkles", cake.toppings)

 def test_check_ingredients(self):
     cake = CakeFactory.CakeFactory("chocolate", "medium")
     cake.add_topping("cherries")
     ingredients = cake.check_ingredients()
     self.assertIn("cocoa", ingredients)
     self.assertIn("cherries", ingredients)
     self.assertNotIn("vanilla extract", ingredients)

 def test_check_price(self):
     cake = CakeFactory.CakeFactory("vanilla", "large")
     cake.add_topping("sprinkles")
     cake.add_topping("cherries")
     price = cake.check_price()
     self.assertEqual(price, 14) # Vanilla cake, large size + 2 toppings


# Running the unittests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCakeFactory))