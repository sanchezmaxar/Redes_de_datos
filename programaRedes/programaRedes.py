from opMenu import *
from get import *

print "Programa de redes"
print "a) solo subredes"  #sub ip
print "b) solo Host"	#numero de host
print "c) ambos subredes y host" #ip y bits numero de host
print "d) ip/bits" #ip/bits
op='e'
while  op=='e':
	op=raw_input("Opcion: ")
	if op=='a' or op=='A':
		soloSub()
	elif op=='b' or op=='B':
		soloHost()
	elif op=='c' or op=='C':
		sub_host()
	elif op=='d' or op=='D':
		ip_bits()
	else: 
		print "opcion no valida"
		op='e'
