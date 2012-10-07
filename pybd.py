# -*- coding: utf-8 -*-
from datetime import date, timedelta
from math import modf


class BusinessDay(date):
	"""class for dealing with business days"""

	@classmethod
	def fromdate(cls,date):
		return cls(date.year, date.month, date.day)

	def isBusinessDay(self):
		"""Retorna True si la fecha ingresada es un día hábil o False en caso contrario"""
		if self.isoweekday() == 6 or self.isoweekday() == 7 :
			return False
		else:
			return True
	
	def diff(self, date):
		"""
		Devuelve diferencia, en días habiles, entre dos fechas 
		ejemplo: days_habiles = inicio.diff(fin)
		"""
		days = BusinessDay.fromdate(date) - self
		datelist = [BusinessDay.fromdate(self + timedelta(days=x)) 
					for x in range(0, days.days)]
		return sum([x.isBusinessDay() for x in datelist])

	def add(self, days):
		"""
		Devuelve fecha resultante de agregar 'days' días habiles a la date de inicio
			inicio = BusinessDay(2012,8,20)
			fin = inicio.add(7) # fin igual a '29 de agosto 2012'
		"""
		habf = 0
		if (days < 5):
			factor = (days + self.isoweekday() - 5) * self.isBusinessDay()
			if(factor > 0):
				habf = 2
		dowf = (self.isoweekday() - 5)*(self.isBusinessDay() - 1)
		return self + timedelta(days  + habf + dowf + modf(days/5)[1]*2)