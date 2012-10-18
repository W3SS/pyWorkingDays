# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
from math import modf

class BusinessCalendar():
	"""documentacion"""

	weekend_type = {"standar" : (6,7), "extended" : (7,), "none" : () }
	calendar = [] # usado para agregar días no laborales
	weekend = weekend_type["standar"] # usado para agregar dias no laborales con peridodicidad semanal

	def __init__(self, wt = "standar", cal=None):
		"""documentacion"""
		if cal == None:
			cal = []
		
		self.calendar = [date(x[0],x[1],x[2]) for x in cal]
		self.weekend = self.weekend_type[wt]

	def isBusinessDay(self, day):
		"""documentacion"""
		if (day.isoweekday() in self.weekend) or (day in self.calendar):
			return False
		else:
			return True

	def isWeekendDay(self, day):
		"""Retorna True si la fecha ingresada es un día de fin de semana o False en caso contrario"""
		if day.isoweekday() in self.weekend:
			return True
		else:
			return False

	def diff_days(self, start, end):
		"""documentacion"""
		days = end - start
		datelist = [(start + timedelta(days=x)) 
					for x in range(0, days.days)]

		return sum([self.isBusinessDay(x) for x in datelist])

	# TODO: ver cómo eliminar recursividad
	def add_days(self, start, days):
		"""documentacion"""
		habf = 0
		if (days < 5):
			#TODO: corregir factor para fin de semanas variables
			factor = (days + start.isoweekday() - 5 -(2-len(self.weekend))) * (1-self.isWeekendDay(start)) 
			if(factor > 0):
				habf = len(self.weekend)
		dowf = (start.isoweekday() - 5)*(-self.isWeekendDay(start)) 
		end = start + timedelta(days  + habf + dowf + modf(days/5)[1]*len(self.weekend)) 

		days = end - start
		datelist = [(start + timedelta(days=x)) 
					for x in range(1, days.days+1)]

		calf = sum([not(self.isBusinessDay(x)) for x in datelist]) - sum([self.isWeekendDay(x) for x in datelist])
		
		if calf == 0:
			return end
		else:
			return self.add_days(end,calf) 	