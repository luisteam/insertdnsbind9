import sys
import os

insercion = sys.argv

zona="luis.gonzalonazareno.org"
file="/var/cache/bind/db.luisgn"

if  "-a" in insercion[1]:
	if "-dir" in insercion[2]:
		tipoa=(insercion[3]+" IN      A "+insercion[4])
		os.system("sudo echo "+tipoa+">> "+file)
		os.system("sudo systemctl restart bind9")

	elif "-alias" in insercion[2]:
		tipoc=(insercion[3]+" IN      CNAME "+insercion[4])
		os.system("sudo echo "+tipoc+">> "+file)
		os.system("sudo systemctl restart bind9")

	else:
		print("Error, el segundo valor no coincide. -dir o -alias.")
elif "-b" in insercion[1]:
	f = open(file,"r")
	lineas = f.readlines()
	f.close()

	f = open(file,"w")
	for linea in lineas:
		if insercion[2] not in linea:
			f.write(linea)
	f.close()
	os.system("sudo systemctl restart bind9")
else:
	print("Error, el primer valor no coincide. -a(anyadir) -b(borrar).")