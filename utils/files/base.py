#!/usr/bin/python
import logging
import datetime
import os

"""
Archivo de utilerias para archivos 

"""

__author__ =  'Christian Hernandez'
__version__=  '1.0'


class Archivo():
	"""
	Clase Archivo 
	Ayudara a la lectura y escritura de un archivo   
	"""

	def __init__(self,name):
		"""
		Constructor init

		param name: Nombre del archivo a crear
			    o nombre de archivo a usar
		"""
		
		self.handle = open(name, 'w+')
		

	def write(self, cadena):
		"""
		Escribe una cadena dentro de un archivo previmente 'abierto'
		
		param cadena: Cadena que se usara para plazmar en el archivo.
		return : No retorna nada
		"""
		try:
			logging.info("Escribindo cadena")		
			self.handle.write(cadena)
		except:
			logging.info("Error escrbiendo cadena al archivo")

	def close (self):
		"""
		Cierra el handle establecido
		
		return : No retorna nada
		"""

		try:
			self.close
		except:
			logging.info("Cierre de archivo")
		

if __name__ == '__main__':

	sDate = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
	logName = sDate + "_prueba.log" 
        logging.basicConfig(filename=logName, level=logging.INFO)
	print logName	

    	archivo = Archivo("pruebai.csv")
	archivo.write("cadena de prueba")
	print "Fin"

