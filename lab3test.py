#test ordinal function

import unittest
import lab3

class ordnialtest(unittest.TestCase):
	
	def test_st(self):
		self.assertEqual('31st',lab3.ord_int(31))
		self.assertNotEqual('31th',lab3.ord_int(31))
	
	def test_nd(self):
		self.assertEqual('22nd',lab3.ord_int(22))
		
	def test_rd(self):
		self.assertEqual('103rd',lab3.ord_int(103))
	
	def test_th(self):
		self.assertEqual('11th', lab3.ord_int(11))
		self.assertEqual('12th', lab3.ord_int(12))
		self.assertEqual('13th', lab3.ord_int(13))
		self.assertEqual('8th', lab3.ord_int(8))
		
	def test_stringtype(self):
		self.assertEqual('Enter a number.', lab3.ord_int('smething'))
	
	def test_floattype(self):
		self.assertEqual("This number has decimal points.", lab3.ord_int(11.1))
		
	
		
if __name__ == '__main__':
    unittest.main()

