import Rot
import hashlib
def cifrado():
    mensaje='T'
    Lista=[]
    f = open ('mensajedeentrada.txt','r')
    mensaje = f.read()
    f.close()
    Lista.append(mensaje)
    defi=Rot.codificar(mensaje,8)
    definite=Rot.codificar(defi,12)
    Lista.append(definite)
    Texto_Cifrado=hashlib.md5(definite.encode())
    Lista.append(Texto_Cifrado.hexdigest())
    f = open ('mensajeseguro.txt','w')
    f.write(Texto_Cifrado.hexdigest())
    f.close()
    return(Lista)
