from get import *
#opciones del menu
def soloSub():
	ip=getIP()	
	subredes=getSub(ip[-1],"Subredes")	
	getAll(subredes,"subredes",ip)

def soloHost():
	ip=getIP()
	host=getSub(ip[-1],"Host")
	getAll(host+2,"host",ip)

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
	while (2**act)<subredes:
		act+=1
	bitsR=act
	tRedes=2**act
	tHost=2**(NMascaraLimite[ip[-1]]-act)
	if NMascaraLimite[ip[-1]]<(bitsR+bitsH):
		print "Error: no puedes usar mas bits de los que te permite la clase"
	else:
		finish(tRedes,tHost,bitsR,ip,bitsR)

def ip_bits():
	bitsMascaraNormal={"A":8,"Pruebas de conectividad":8,"B":16,"C":24}
	ipmask=getIpMask()
	bitsR=ipmask[-1]-bitsMascaraNormal[ipmask[-2]]
	bitsH=32-ipmask[-1]
	finish(2**bitsR,2**bitsH,bitsR,ipmask[:-1],bitsR)
