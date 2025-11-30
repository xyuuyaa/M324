import unittest
from src.house import House

class TestHouse(unittest.TestCase):
    house = House()

    def test_create(self):
        self.assertIsInstance(house, House)

    def test_name_valid(self):
        house.set_name("Neverland")
        self.assertEqual(house.name, "Neverland")
       
    def test_name_invalid(self):
        with self.assertRaises(TypeError):
            house.set_name(42)
        
    def test_get_name(self):
        house.set_name("Pineapple")
        self.assertEqual(house.get_name, "Pineapple")

    def test_get_price(self):
        price = house.get_price
        self.assertEqual(price, "50 CHF")

if __name__ == '__main__':
    unittest.main()