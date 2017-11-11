#biblioteca de metodos
def getAll(variable,caso,ip):
	NMascaraLimite={"A":24,"Pruebas de conectividad":24,"B":16,"C":8,"D":0,"E":0}
	#la variable solo cambia entre el caso en que se recibe un host o subredes
	act=0
	while (2**act)<variable:
		act+=1
	bits=act
	tRedes=2**act
	tHost=2**(NMascaraLimite[ip[-1]]-act)
	if caso=='host':
		act=NMascaraLimite[ip[-1]]-act
		finish(tHost,tRedes,NMascaraLimite[ip[-1]]-bits,ip,act)
	if caso=='subredes':
		finish(tRedes,tHost,bits,ip,act)

def getIP():
	valida=False
	while valida==False:
		ip=raw_input("IP: ")
		valida=validaIP(ip)
		if valida:
			ip=[int(i) for i in ip.split(".")]
			clase=getClass(ip)
			if clase=="D" or clase=="E":
				print"Este Programa no sirve prar clases de tipo D o E"
				valida=False
	ip.append(clase)
	return ip

def validaIP(ip):
	if len(ip.split("."))<4:
		print "Error IP no valida"
	else:
		valida=True
		for i in ip.split("."):
			try:
				if int(i) <0 or int(i)>255:
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
	return valida

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

def validaMask(ip,mask):
	NMascaraLimite={"A":8,"Pruebas de conectividad":8,"B":16,"C":24,"D":0,"E":0}
	try:
		if int(mask)>=NMascaraLimite[getClass(ip)] and int(mask)<31:
			return True
		else:
			print "La mascara no concuerda con la ip"
			return False
	except:
		print "La mascara no son digitos "
		return False

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
	impUtiles(ip[:-1],tHost,tRedes,mascaras[ip[-1]])

def getIpMask():
	valida=False
	while valida==False:
		try:
			ipMask=raw_input("IP/MASK: ")
			valida=validaIP(ipMask.split("/")[0])
			if valida:
				ip=ipMask.split("/")[0]
				ip=[int(i) for i in ip.split(".")]
				ip.append(getClass(ip))
				valida=valida and validaMask(ip,ipMask.split("/")[1])
		except:
			print "Error de formato en la IP"
			valida=False
	return ip+[int(ipMask.split("/")[1])]


def impUtiles(ip,host,subredes,mascara):
	anterior=[]
	for i in range(len(mascara)):
		if mascara[i]==255:
			anterior.append(ip[i])
		else:
			anterior.append(0)
	anterior=int(ipToBin(anterior),2)
	for i in range(subredes):
		siguiente=anterior+host-1
		print str(i+1)+".-\t"+".".join(str(i) for i in BinToIP(IntToBin(anterior,32)))+"\t-\t"+".".join(str(i) for i in BinToIP(IntToBin(siguiente,32)))
		anterior=siguiente+1

def ipToBin(ip):
	salida=""
	for i in ip:
		salida=salida+IntToBin(i,8)
	return salida

def BinToIP(binary):
	salida=[]
	for i in range(0,32,8):
		salida.append(int(binary[i:(i+8)],2))
	return salida

def IntToBin(entero,nBits):
	aux=bin(entero)[2:]
	aux="".join("0" for i in range(nBits-len(aux)))+aux
	return aux