

fich = open ("/etc/passwd","r");
Lineas = fich.readlines();

for Linea in Lineas:
	usuario = Linea.split(':')
	print ("Usuario: " ,usuario[0], ", Shell: " , usuario[6] )

fich.close()
