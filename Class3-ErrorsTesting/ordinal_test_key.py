import unittest
from ordinal_dc import ordinal

class OrdinalTest(unittest.TestCase):

  def setup(self):
    pass 

  def test_zero(self):
    self.assertEqual("0th", ordinal(0))

  def test_first(self):
    self.assertEqual("1st", ordinal(1))

  def test_second(self):
    self.assertEqual("2nd", ordinal(2))

  def test_third(self):
    self.assertEqual("3rd", ordinal(3))

  def test_fourth(self):
    self.assertEqual("4th", ordinal(4))

  def test_eleventh(self):
    self.assertEqual("11th", ordinal(11))

  def test_twelfth(self):
    self.assertEqual("12th", ordinal(12))

  def test_one_thousand_two(self):
    self.assertEqual("1002nd", ordinal(1002))

  def test_negative_one(self):
    self.assertEqual("-1st", ordinal(-1))

  def test_decimal(self):
    self.assertEqual("1st", ordinal(1.0))

  def test_string_input(self):
    with self.assertRaises(TypeError):	
    	ordinal("b")

if __name__ == '__main__':
  unittest.main()