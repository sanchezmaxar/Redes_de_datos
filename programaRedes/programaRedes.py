def getIP():
	valida=False
	while valida==False:
		ip=raw_input("IP: ")
		if len(ip.split("."))<4:
			print "Error IP no valida"
		else:
			valida=True
			for i in ip.split("."):
				try:
					if int(i) <0 or int(i)>255:
						print i
						print "Rango de direcciones ip no valido"
						valida=False
						break
				except:
					print "Los datos ingresados la IP no son enteros"
					valida=False
					break
			if valida and int(ip.split(".")[0]) ==0:
				print "El primer octeto no puede ser cero"
				valida=False
			ip=[int(i) for i in ip.split(".")]
		clase=getClass(ip)
		if clase=="D" or clase=="E":
			valida=False
	ip.append(clase)
	return ip

def getSub(clase,cadena):
	limite={"A":8388608,"Pruebas de conectividad":8388608,"B":32768,"C":128} #cual es el limite en una red de tipo D?
	num=raw_input(cadena+": ")
	cond=True
	while cond:
		try:
			if int(num)>limite[clase]:
				print "Limite de"+cadena.lower()+ "en la clase de la red superado"
				num=raw_input("Subredes: ")
				cond=True
			else:
				cond=False
		except:
			print "Error no se introdujo un numero"
			num=raw_input("Subredes: ")
			cond=True
	return int(num)

def getClass(ip):
	if ip[0]>1 and ip[0]<127:
		return "A"
	elif ip[0]==127:
		return "Pruebas de conectividad"
	elif ip[0]>127 and ip[0]<192:
		return "B"
	elif ip[0]>191 and ip[0]<224:
		return "C"
	elif ip[0]>223 and ip[0]<240:
		print "Error no se puede subdivir una red de tipo D"
		return "D"
	elif ip[0]>239 and ip[0]<256:
		print "Error no se puede subdivir una red de tipo E"
		return "E"
	else:
		return "Error"

def soloSub():
	NMascaraLimite={"A":24,"Pruebas de conectividad":24,"B":16,"C":8,"D":0,"E":0}
	ip=getIP()
	
	subredes=getSub(ip[-1],"Subredes")	
	act=0
	while (2**act)<subredes:
		act+=1
	nMask=[]
	bits=act
	tRedes=2**act
	tHost=2**(NMascaraLimite[ip[-1]]-act)
	finish(tRedes,tHost,bits,ip,act)

def soloHost():
	NMascaraLimite={"A":24,"Pruebas de conectividad":24,"B":16,"C":8,"D":0,"E":0}
	ip=getIP()
	host=getSub(ip[-1],"Host")
	act=0
	while (2**act)<host+2:
		act+=1
	bits=act
	tHost=2**act
	tRedes=2**(NMascaraLimite[ip[-1]]-act)
	act=NMascaraLimite[ip[-1]]-act
	finish(tRedes,tHost,bits,ip,act)

def finish(tRedes,tHost,bits,ip,act):
	mascaras={"A":[255,0,0,0],"Pruebas de conectividad":[255,0,0,0],"B":[255,255,0,0],"C":[255,255,255,0],"D":[None],"E":[None]}
	nMask=[]
	for i in mascaras[ip[-1]]:
		if i!=255:
			if act>8:
				nMask.append(255)
				act-=8
			else:
				acum=0
				while act>0:
					acum+=2**(8-act)
					act-=1
				nMask.append(acum)
		else:
			nMask.append(255)
	print "La mascara es: "+".".join([str(i) for i in nMask])
	print "Total de subredes: "+str(tRedes)
	print "Total de host: "+str(tHost)
	print "Host utiles: "+str(tHost-2)
	print "Bits prestados: "+str(bits)
	print "Clase: "+ip[-1]
	#talvez falte el rango de direcciones utiles
def sub_host():
	NMascaraLimite={"A":24,"Pruebas de conectividad":24,"B":16,"C":8,"D":0,"E":0}
	ip=getIP()
	subredes=getSub(ip[-1],"Subredes")
	host=getSub(ip[-1],"Host")
	act=0
	while (2**act)<host+2:
		act+=1
	bitsH=act
	act=0
	while (2**act)<subredes+2:
		act+=1
	bitsR=act
	tRedes=2**act
	tHost=2**(NMascaraLimite[ip[-1]]-act)
	if NMascaraLimite[ip[-1]]<(bitsR+bitsH):
		print "Error: no puedes usar mas bits de los que te permite la clase"
	else:
		finish(tRedes,tHost,bitsR,ip,bitsH)

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
