#Python - utils
#Chrisitan Hernandez

def utf8(string):
	string = string.encode('utf-8')
	return string

def limpiaCadena(string):
	string = string.replace(',','')
	return string

def csvCadena(string):
	string = utf8(limpiaCadena(string))
	return string
