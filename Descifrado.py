import Rot
def decifrado(mensaje):
    defi=Rot.decodificar(mensaje,12)
    Texto_Descifrado=Rot.decodificar(defi,8)
    print('mensaje descifrado es el siguiente: ',Texto_Descifrado)
    return(Texto_Descifrado)
