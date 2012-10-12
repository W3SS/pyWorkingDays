import unittest

from pybd import BusinessDay
from datetime import date

class TestCalculoFechas(unittest.TestCase):
	def test_diff_default(self):
		start = BusinessDay(2012,10,11)
		end = BusinessDay(2012,10,18)
		days = start.diff(end)
		self.assertEqual(days,5)
		pass

	def test_add_default(self):
		start = BusinessDay(2012,10,11)
		end = start.add(5)
		self.assertEqual(end, date(2012,10,18))
		pass


if __name__ == '__main__':
	unittest.main()