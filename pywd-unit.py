# -*- coding: utf-8 -*-
import unittest

from pyWorkingDays import BusinessCalendar
from datetime import date

class TestCalculoFechas(unittest.TestCase):
	def test_isBusinessDay(self):
		day = date(2012,10,15)
		cal = BusinessCalendar("standar",[(2012,10,15),(2012,11,1),(2012,11,2)])
		self.assertEqual(cal.isBusinessDay(day), False)

		day = date(2012,10,14)
		self.assertEqual(cal.isBusinessDay(day), False)	

		day = date(2012,10,16)
		self.assertEqual(cal.isBusinessDay(day), True)	

	def test_diff_days(self):
		cal = BusinessCalendar("standar",[(2012,10,15),(2012,11,1),(2012,11,2)])
		
		start = date(2012,10,11)
		end = date(2012,10,18)
		self.assertEqual(cal.diff_days(start,end), 4)

		start = date(2012,10,18)
		end = date(2012,10,25)
		self.assertEqual(cal.diff_days(start,end), 5)

		start = date(2012,10,16)
		end = date(2012,10,19)
		self.assertEqual(cal.diff_days(start,end), 3)

		cal = BusinessCalendar("extended",[(2012,10,15),(2012,11,1),(2012,11,2)])
		
		start = date(2012,10,11)
		end = date(2012,10,18)
		self.assertEqual(cal.diff_days(start,end), 5)

		start = date(2012,10,18)
		end = date(2012,10,25)
		self.assertEqual(cal.diff_days(start,end), 6)

		start = date(2012,10,16)
		end = date(2012,10,19)
		self.assertEqual(cal.diff_days(start,end), 3)

	def test_add_days(self):
		cal = BusinessCalendar("standar",[(2012,10,15),(2012,11,1),(2012,11,2)])

		start = date(2012,10,29)
		days = 3
		self.assertEqual(cal.add_days(start,days), date(2012,11,5))

		start = date(2012,10,18)
		days = 5
		self.assertEqual(cal.add_days(start,days), date(2012,10,25))

		start = date(2012,10,16)
		days = 3
		self.assertEqual(cal.add_days(start,days), date(2012,10,19))


if __name__ == '__main__':
	unittest.main()