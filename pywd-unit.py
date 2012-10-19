# -*- coding: utf-8 -*-
# Author: Tomás Hermosilla
# e-mail: thermosilla [at] gmail [dot] com
# Version: 0.2
# Licence: AGPL v3

import unittest

from pyWorkingDays import BusinessCalendar
from datetime import date

cal = BusinessCalendar("standar",[(2012,10,15),(2012,11,1),(2012,11,2)])

class TestCalculoFechas(unittest.TestCase):
	def test_is_business_day(self):
		day = date(2012,10,15)
		self.assertEqual(cal.is_business_day(day), False)

		day = date(2012,10,14)
		self.assertEqual(cal.is_business_day(day), False)	

		day = date(2012,10,16)
		self.assertEqual(cal.is_business_day(day), True)	

	def test_diff_days_standar(self):
		cal = BusinessCalendar("standar",
			[(2012,10,15),(2012,11,1),(2012,11,2)])
		start = date(2012,10,11)
		end = date(2012,10,18)
		self.assertEqual(cal.diff_days(start,end), 4)

		start = date(2012,10,18)
		end = date(2012,10,25)
		self.assertEqual(cal.diff_days(start,end), 5)

		start = date(2012,10,16)
		end = date(2012,10,19)
		self.assertEqual(cal.diff_days(start,end), 3)

	def test_diff_days_extended(self):
		cal.set_weekend("extended")
		
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