# -*- coding: utf-8 -*-
from datetime import date, timedelta
from math import modf


class BusinessDay(date):
	"""Class for dealing with business days"""

	calendar = None # usado para agregar días no laborales
	weekend = [6,7] # usado para agregar dias no laborales con peridodicidad semanal

	@classmethod
	def fromdate(cls,date):
		"""Crea objeto BusinessDay a partir de un objeto datetime.date"""
		return cls(date.year, date.month, date.day)

	def __str__(self):
		return "%s-%s-%s" % (self.year,self.month,self.day)

	def toDate(self):
		"""Retorna un objeto datetime.date"""
		return date(self.year, self.month, self.day)

	def setCalendar(self,dates):
		"""Fija fechas no laborales específicas"""
		self.calendar = []
		for date in dates:
			year,month,day=date
			self.calendar.append(BusinessDay(year,month,day))

	def setWeekends(self,weekend):
		"""Fija fechas no laborales repetitivas"""
		self.weekend = weekend


	#TODO: integrar fechas desde calendario
	#TODO: reemplazar por isWeekEndDay en calculos
	def isBusinessDay(self):
		"""Retorna True si la fecha ingresada es un día hábil o False en caso contrario"""
		if self.isoweekday() in self.weekend:
			return False
		elif self.toDate() in [x.toDate() for x in self.calendar]: # Hago la transformación para poder comparar las fechas
			return False
		else:
			return True
	
	def isWeekendDay(self):
		"""Retorna True si la fecha ingresada es un día de fin de semana o False en caso contrario"""
		if self.isoweekday() in self.weekend:
			return True
		else:
			return False

	def diff(self, date):
		"""
		Devuelve diferencia, en días habiles, entre dos fechas 
		ejemplo: days_habiles = inicio.diff(fin)
		"""
		days = BusinessDay.fromdate(date) - self
		datelist = [BusinessDay.fromdate(self + timedelta(days=x)) 
					for x in range(0, days.days)]
		return sum([not(x.isWeekendDay()) for x in datelist])

	#TODO: agregar corrección por dias calendario
	def add(self, days):
		"""
		Devuelve fecha resultante de agregar 'days' días habiles a la date de inicio
			inicio = BusinessDay(2012,8,20)
			fin = inicio.add(7) # fin igual a '29 de agosto 2012'
		"""
		habf = 0
		if (days < 5):
			factor = (days + self.isoweekday() - 5) * (1-self.isWeekendDay()) #TODO: corregir para fin de semanas variables
			if(factor > 0):
				habf = len(self.weekend)
		dowf = (self.isoweekday() - 5)*(-self.isWeekendDay()) 
		return self + timedelta(days  + habf + dowf + modf(days/5)[1]*len(self.weekend))