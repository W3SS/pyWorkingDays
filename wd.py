# -*- coding: utf-8 -*-
from datetime import date, timedelta
from math import modf


class WorkingDay(date):
	"""Clase para el manejo de días habiles"""

	@classmethod
	def fromfecha(cls,fecha):
		return cls(fecha.year, fecha.month, fecha.day)

	def isWorkingDay(self):
		"""Retorna True si la fecha ingresada es un día hábil o False en caso contrario"""
		if self.isoweekday() == 6 or self.isoweekday() == 7 :
			return False
		else:
			return True
	
	def diff(self, fecha):
		"""
		Devuelve diferencia, en días habiles, entre dos fechas 
		ejemplo: dias_habiles = inicio.diff(fin)
		"""
		dias = WorkingDay.fromfecha(fecha) - self
		datelist = [WorkingDay.fromfecha(self + timedelta(days=x)) 
					for x in range(0, dias.days)]
		return sum([x.isWorkingDay() for x in datelist])

	def add(self, dias):
		"""
		Devuelve fecha resultante de agregar 'dias' días habiles a la fecha de inicio
			inicio = WorkingDay(2012,8,20)
			fin = inicio.add(7) # fin igual a '29 de agosto 2012'
		"""
		habf = 0
		if (dias < 5):
			factor = (dias + self.isoweekday() - 5) * self.isWorkingDay()
			print factor
			if(factor > 0):
				habf = 2
		dowf = (self.isoweekday() - 5)*(self.isWorkingDay() - 1)
		return self + timedelta(dias  + habf + dowf + modf(dias/5)[1]*2)