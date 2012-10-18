# -*- coding: utf-8 -*-
# pyWorkingDays - Python module for dealing with bussiness days
# Author: Tomás Hermosilla
# e-mail: thermosilla [at] gmail [dot] com
# Version: 0.2
# Licence: AGPL v3
# Notes: this module is not tested in python 3.x

from datetime import datetime, date, timedelta
from math import modf

# TODO: agregar documentación 
class BusinessCalendar():
	"""documentacion"""

	__weekend_type = {"standar" : (6,7), "extended" : (7,), "none" : () }
	__calendar = [] # usado para agregar días no laborales
	__weekend = __weekend_type["standar"] 

	def __init__(self, wt = "standar", cal=None):
		"""documentacion"""
		if cal == None:
			cal = []
		
		self.__calendar = [date(x[0],x[1],x[2]) for x in cal]
		self.__weekend = self.__weekend_type[wt]

	def isBusinessDay(self, day):
		"""documentacion"""
		if (day.isoweekday() in self.__weekend) or (day in self.__calendar):
			return False
		else:
			return True

	def isWeekendDay(self, day):
		"""documentacion"""
		if day.isoweekday() in self.__weekend:
			return True
		else:
			return False

	def setWeekend(self, wt = "standar"):
		self.__weekend = self.__weekend_type[wt]

	def setCalendar(self, cal = None):
		if cal == None:
			cal = []
		
		self.__calendar = [date(x[0],x[1],x[2]) for x in cal]

	def diff_days(self, start, end):
		"""documentacion"""
		days = end - start
		datelist = [(start + timedelta(days=x)) 
					for x in range(0, days.days)]

		return sum([self.isBusinessDay(x) for x in datelist])

	# TODO: ver cómo eliminar recursividad
	# TODO: refactorizar nombres de variables
	def add_days(self, start, days):
		"""documentacion"""
		habf = 0
		if (days < 5):
			if((days + start.isoweekday() - 5 - (2-len(self.__weekend))) * (1-self.isWeekendDay(start)) > 0):
				habf = len(self.__weekend)
		dowf = (start.isoweekday() - 5)*(-self.isWeekendDay(start)) 
		end = start + timedelta(days  + habf + dowf + modf(days/5)[1]*len(self.__weekend)) 

		days = end - start
		datelist = [(start + timedelta(days=x)) for x in range(1, days.days+1)]

		calf = sum([not(self.isBusinessDay(x)) for x in datelist]) - sum([self.isWeekendDay(x) for x in datelist])
		
		if calf == 0:
			return end
		else:
			return self.add_days(end,calf)