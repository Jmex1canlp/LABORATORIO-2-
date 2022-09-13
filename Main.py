import Cifrado
import Descifrado
Cont=True
Lista=[]
incripta={}
while(Cont):
    print('1)Cifrado')
    print('2)Descifrado')
    print('3)Salir del programa')
    opcion=input('Que opcion desea: ')
    if opcion == '1':
        print('***********************************************')
        Lista=Cifrado.cifrado()
        incripta[Lista[0]]=(Lista[1],Lista[2])
        print('Mensaje de entrada ya fue cifrado')
        print('***********************************************')
    elif opcion == '2':
        print('***********************************************')
        mensaje='t'
        f = open ('mensajedeentrada.txt','r')
        mensaje = f.read()
        f.close()
        if mensaje in incripta:
            incriptado='t'
            f = open ('mensajeseguro.txt','r')
            incriptado = f.read()
            f.close()
            if incriptado == incripta[mensaje][1]:
                mensaje_descriptado=Descifrado.decifrado(incripta[mensaje][0])
            else:
                print('El mensaje seguro fue modificado favor de revisar')   
        else:
            if len(incripta) == 0:
                print('al ser la primera vez no hay Mensaje seguro favor de codificar algo')
            else:
                print('Modificacion de la palabra entrante.')
        print('***********************************************')
    elif opcion == '3':
        print('***********************************************')
        print('Gracias por ocupar este programa')
        Cont=False
    else:
        print('esta opcion no es correcta intente nuevamente')
        print('***********************************************')
