
# coding=utf8
import arbol
from graphviz import Digraph
import sys


r = 'ƇƇ"ƆƇƇ\x00Ĭ\x01Ĭ\x02Ĭ\x03Ĭ\x04Ĭ\x05Ĭ\x06Ĭ\x07Ĭ\x08Ĭ\tĬ\nĬ\x0bĬ\x0cĬ\x0eĬ\x0fĬ\x10Ĭ\x11Ĭ\x12Ĭ\x13Ĭ\x14Ĭ\x15Ĭ\x16Ĭ\x17Ĭ\x18Ĭ\x19Ĭ\x1aĬ\x1bĬ\x1cĬ\x1dĬ\x1eĬ\x1fĬ Ĭ!Ĭ#Ĭ$Ĭ%Ĭ&Ĭ\'Ĭ(Ĭ)Ĭ*Ĭ+Ĭ,Ĭ-Ĭ.Ĭ/Ĭ0Ĭ1Ĭ2Ĭ3Ĭ4Ĭ5Ĭ6Ĭ7Ĭ8Ĭ9Ĭ:Ĭ;Ĭ<Ĭ=Ĭ>Ĭ?Ĭ@ĬAĬBĬCĬDĬEĬFĬGĬHĬIĬJĬKĬLĬMĬNĬOĬPĬQĬRĬSĬTĬUĬVĬWĬXĬYĬZĬ[Ĭ\\Ĭ]Ĭ^Ĭ_Ĭ`ĬaĬbĬcĬdĬeĬfĬgĬhĬiĬjĬkĬlĬmĬnĬoĬpĬqĬrĬsĬtĬuĬvĬwĬxĬyĬzĬ{Ĭ|Ĭ}Ĭ~Ĭ\x7fĬ\x80Ĭ\x81Ĭ\x82Ĭ\x83Ĭ\x84Ĭ\x85Ĭ\x86Ĭ\x87Ĭ\x88Ĭ\x89Ĭ\x8aĬ\x8bĬ\x8cĬ\x8dĬ\x8eĬ\x8fĬ\x90Ĭ\x91Ĭ\x92Ĭ\x93Ĭ\x94Ĭ\x95Ĭ\x96Ĭ\x97Ĭ\x98Ĭ\x99Ĭ\x9aĬ\x9bĬ\x9cĬ\x9dĬ\x9eĬ\x9fĬ\xa0Ĭ¡Ĭ¢Ĭ£Ĭ¤Ĭ¥Ĭ¦Ĭ§Ĭ¨Ĭ©ĬªĬ«Ĭ¬Ĭ\xadĬ®Ĭ¯Ĭ°Ĭ±Ĭ²Ĭ³Ĭ´ĬµĬ¶Ĭ·Ĭ¸Ĭ¹ĬºĬ»Ĭ¼Ĭ½Ĭ¾Ĭ¿ĬÀĬÁĬÂĬÃĬÄĬÅĬÆĬÇĬÈĬÉĬÊĬËĬÌĬÍĬÎĬÏĬÐĬÑĬÒĬÓĬÔĬÕĬÖĬ×ĬØĬÙĬÚĬÛĬÜĬÝĬÞĬßĬàĬáĬâĬãĬäĬåĬæĬçĬèĬéĬêĬëĬìĬíĬîĬïĬðĬñĬòĬóĬôĬõĬöĬ÷ĬøĬùĬúĬûĬüĬýĬþĬÿĬ\nĬ\tƆƆƇƇ\x00Ĭ\x01Ĭ\x02Ĭ\x03Ĭ\x04Ĭ\x05Ĭ\x06Ĭ\x07Ĭ\x08Ĭ\tĬ\nĬ\x0bĬ\x0cĬ\x0eĬ\x0fĬ\x10Ĭ\x11Ĭ\x12Ĭ\x13Ĭ\x14Ĭ\x15Ĭ\x16Ĭ\x17Ĭ\x18Ĭ\x19Ĭ\x1aĬ\x1bĬ\x1cĬ\x1dĬ\x1eĬ\x1fĬ Ĭ!Ĭ#Ĭ$Ĭ%Ĭ&Ĭ\'Ĭ(Ĭ)Ĭ*Ĭ+Ĭ,Ĭ-Ĭ.Ĭ/Ĭ0Ĭ1Ĭ2Ĭ3Ĭ4Ĭ5Ĭ6Ĭ7Ĭ8Ĭ9Ĭ:Ĭ;Ĭ<Ĭ=Ĭ>Ĭ?Ĭ@ĬAĬBĬCĬDĬEĬFĬGĬHĬIĬJĬKĬLĬMĬNĬOĬPĬQĬRĬSĬTĬUĬVĬWĬXĬYĬZĬ[Ĭ\\Ĭ]Ĭ^Ĭ_Ĭ`ĬaĬbĬcĬdĬeĬfĬgĬhĬiĬjĬkĬlĬmĬnĬoĬpĬqĬrĬsĬtĬuĬvĬwĬxĬyĬzĬ{Ĭ|Ĭ}Ĭ~Ĭ\x7fĬ\x80Ĭ\x81Ĭ\x82Ĭ\x83Ĭ\x84Ĭ\x85Ĭ\x86Ĭ\x87Ĭ\x88Ĭ\x89Ĭ\x8aĬ\x8bĬ\x8cĬ\x8dĬ\x8eĬ\x8fĬ\x90Ĭ\x91Ĭ\x92Ĭ\x93Ĭ\x94Ĭ\x95Ĭ\x96Ĭ\x97Ĭ\x98Ĭ\x99Ĭ\x9aĬ\x9bĬ\x9cĬ\x9dĬ\x9eĬ\x9fĬ\xa0Ĭ¡Ĭ¢Ĭ£Ĭ¤Ĭ¥Ĭ¦Ĭ§Ĭ¨Ĭ©ĬªĬ«Ĭ¬Ĭ\xadĬ®Ĭ¯Ĭ°Ĭ±Ĭ²Ĭ³Ĭ´ĬµĬ¶Ĭ·Ĭ¸Ĭ¹ĬºĬ»Ĭ¼Ĭ½Ĭ¾Ĭ¿ĬÀĬÁĬÂĬÃĬÄĬÅĬÆĬÇĬÈĬÉĬÊĬËĬÌĬÍĬÎĬÏĬÐĬÑĬÒĬÓĬÔĬÕĬÖĬ×ĬØĬÙĬÚĬÛĬÜĬÝĬÞĬßĬàĬáĬâĬãĬäĬåĬæĬçĬèĬéĬêĬëĬìĬíĬîĬïĬðĬñĬòĬóĬôĬõĬöĬ÷ĬøĬùĬúĬûĬüĬýĬþĬÿĬ\nĬ\tƆƆɘƇƇ"ƆƆƆȞ'
token = {'string': 'Ƈ"ƆƇƇ\x00Ĭ\x01Ĭ\x02Ĭ\x03Ĭ\x04Ĭ\x05Ĭ\x06Ĭ\x07Ĭ\x08Ĭ\tĬ\nĬ\x0bĬ\x0cĬ\x0eĬ\x0fĬ\x10Ĭ\x11Ĭ\x12Ĭ\x13Ĭ\x14Ĭ\x15Ĭ\x16Ĭ\x17Ĭ\x18Ĭ\x19Ĭ\x1aĬ\x1bĬ\x1cĬ\x1dĬ\x1eĬ\x1fĬ Ĭ!Ĭ#Ĭ$Ĭ%Ĭ&Ĭ\'Ĭ(Ĭ)Ĭ*Ĭ+Ĭ,Ĭ-Ĭ.Ĭ/Ĭ0Ĭ1Ĭ2Ĭ3Ĭ4Ĭ5Ĭ6Ĭ7Ĭ8Ĭ9Ĭ:Ĭ;Ĭ<Ĭ=Ĭ>Ĭ?Ĭ@ĬAĬBĬCĬDĬEĬFĬGĬHĬIĬJĬKĬLĬMĬNĬOĬPĬQĬRĬSĬTĬUĬVĬWĬXĬYĬZĬ[Ĭ\\Ĭ]Ĭ^Ĭ_Ĭ`ĬaĬbĬcĬdĬeĬfĬgĬhĬiĬjĬkĬlĬmĬnĬoĬpĬqĬrĬsĬtĬuĬvĬwĬxĬyĬzĬ{Ĭ|Ĭ}Ĭ~Ĭ\x7fĬ\x80Ĭ\x81Ĭ\x82Ĭ\x83Ĭ\x84Ĭ\x85Ĭ\x86Ĭ\x87Ĭ\x88Ĭ\x89Ĭ\x8aĬ\x8bĬ\x8cĬ\x8dĬ\x8eĬ\x8fĬ\x90Ĭ\x91Ĭ\x92Ĭ\x93Ĭ\x94Ĭ\x95Ĭ\x96Ĭ\x97Ĭ\x98Ĭ\x99Ĭ\x9aĬ\x9bĬ\x9cĬ\x9dĬ\x9eĬ\x9fĬ\xa0Ĭ¡Ĭ¢Ĭ£Ĭ¤Ĭ¥Ĭ¦Ĭ§Ĭ¨Ĭ©ĬªĬ«Ĭ¬Ĭ\xadĬ®Ĭ¯Ĭ°Ĭ±Ĭ²Ĭ³Ĭ´ĬµĬ¶Ĭ·Ĭ¸Ĭ¹ĬºĬ»Ĭ¼Ĭ½Ĭ¾Ĭ¿ĬÀĬÁĬÂĬÃĬÄĬÅĬÆĬÇĬÈĬÉĬÊĬËĬÌĬÍĬÎĬÏĬÐĬÑĬÒĬÓĬÔĬÕĬÖĬ×ĬØĬÙĬÚĬÛĬÜĬÝĬÞĬßĬàĬáĬâĬãĬäĬåĬæĬçĬèĬéĬêĬëĬìĬíĬîĬïĬðĬñĬòĬóĬôĬõĬöĬ÷ĬøĬùĬúĬûĬüĬýĬþĬÿĬ\nĬ\tƆƆƇƇ\x00Ĭ\x01Ĭ\x02Ĭ\x03Ĭ\x04Ĭ\x05Ĭ\x06Ĭ\x07Ĭ\x08Ĭ\tĬ\nĬ\x0bĬ\x0cĬ\x0eĬ\x0fĬ\x10Ĭ\x11Ĭ\x12Ĭ\x13Ĭ\x14Ĭ\x15Ĭ\x16Ĭ\x17Ĭ\x18Ĭ\x19Ĭ\x1aĬ\x1bĬ\x1cĬ\x1dĬ\x1eĬ\x1fĬ Ĭ!Ĭ#Ĭ$Ĭ%Ĭ&Ĭ\'Ĭ(Ĭ)Ĭ*Ĭ+Ĭ,Ĭ-Ĭ.Ĭ/Ĭ0Ĭ1Ĭ2Ĭ3Ĭ4Ĭ5Ĭ6Ĭ7Ĭ8Ĭ9Ĭ:Ĭ;Ĭ<Ĭ=Ĭ>Ĭ?Ĭ@ĬAĬBĬCĬDĬEĬFĬGĬHĬIĬJĬKĬLĬMĬNĬOĬPĬQĬRĬSĬTĬUĬVĬWĬXĬYĬZĬ[Ĭ\\Ĭ]Ĭ^Ĭ_Ĭ`ĬaĬbĬcĬdĬeĬfĬgĬhĬiĬjĬkĬlĬmĬnĬoĬpĬqĬrĬsĬtĬuĬvĬwĬxĬyĬzĬ{Ĭ|Ĭ}Ĭ~Ĭ\x7fĬ\x80Ĭ\x81Ĭ\x82Ĭ\x83Ĭ\x84Ĭ\x85Ĭ\x86Ĭ\x87Ĭ\x88Ĭ\x89Ĭ\x8aĬ\x8bĬ\x8cĬ\x8dĬ\x8eĬ\x8fĬ\x90Ĭ\x91Ĭ\x92Ĭ\x93Ĭ\x94Ĭ\x95Ĭ\x96Ĭ\x97Ĭ\x98Ĭ\x99Ĭ\x9aĬ\x9bĬ\x9cĬ\x9dĬ\x9eĬ\x9fĬ\xa0Ĭ¡Ĭ¢Ĭ£Ĭ¤Ĭ¥Ĭ¦Ĭ§Ĭ¨Ĭ©ĬªĬ«Ĭ¬Ĭ\xadĬ®Ĭ¯Ĭ°Ĭ±Ĭ²Ĭ³Ĭ´ĬµĬ¶Ĭ·Ĭ¸Ĭ¹ĬºĬ»Ĭ¼Ĭ½Ĭ¾Ĭ¿ĬÀĬÁĬÂĬÃĬÄĬÅĬÆĬÇĬÈĬÉĬÊĬËĬÌĬÍĬÎĬÏĬÐĬÑĬÒĬÓĬÔĬÕĬÖĬ×ĬØĬÙĬÚĬÛĬÜĬÝĬÞĬßĬàĬáĬâĬãĬäĬåĬæĬçĬèĬéĬêĬëĬìĬíĬîĬïĬðĬñĬòĬóĬôĬõĬöĬ÷ĬøĬùĬúĬûĬüĬýĬþĬÿĬ\nĬ\tƆƆɘƇƇ"ƆƆ'}
excepcion = {}
file2 = open('prueba.txt', 'r',encoding='utf-8')
w = ""
for i in file2:
    w+= i

print("LA FRASE A LEER ES",w)



for k,v in token.items():
    print(k,":",repr(v))

# METODO PARA ASIGNAR QUE OPERACION TIENE MAS PRECEDENCIA QUE OTRO EN ESTE ORDEN DESC: * -> . -> Ĭ
def precedence(op):
    if (op == 'ɘ'):
        return 3
    if (op == 'ȹ'):
        return 2
    if (op == 'Ĭ'):
        return 1
    return 0
# METODO MOVE PARA SIMULAR ALGORITMOS
def mov(statesMov, letraM,transM):
        moveA = []
        arrayNUEVO = statesMov.copy()
        stacker = []
        for vMov in arrayNUEVO:
            for bM in transM:
                if(bM[0] == vMov and bM[1] ==letraM):
                    #arrayNUEVO.append(bM[2])
                    moveA.append(bM[2])
        return moveA

# METODO PARA CONTAR CANTIDAD DE PARENTESIS EN REGEX Y VERIFICAR SI ESTA BIEN INGRESADO
def contar(r):
    cont1 = 0
    cont2 = 0 
    for i in r:
        if(i == "Ƈ"):
            cont1+=1
        if(i=="Ɔ"):
            cont2+=1
    if(cont1 == cont2):
        return True
    else:
        return False

# METODO QUE AGREGA UN OPERADOR "." CADA VEZ QUE SE NECESITE
# CREDITOS: PAUL BELCHES POR DAR SU IDEA DE COLOCAR EL PUNTO PARA FACILITAR LA LECTURA
def arreglar2(r):
    i = 0
    expr = ''
    cont = 0 
    while i < len(r):
        if (r[i] == 'Ĭ'):
            cont = 0
        elif(r[i] == 'Ƈ'):
            if (cont == 1):
                expr = expr + 'ȹ'
                cont = 0;
        elif(r[i] == 'Ɔ' or r[i] == 'ɘ'):
            pass
        else:
            cont = cont + 1
        if(cont == 2):
            expr = expr+'ȹ'+r[i]
            cont = 1
        else:
            expr = expr + r[i]
        i += 1
    return expr

# METODO QUE CONVIERTE LAS EXPRESIONES REGULARES EN SUS OTRAS FORMAS
# (A)+ -> (A)ɘ(A)
# (A)? -> (AĬε)
def arreglar1(r):
    #ε
    i = 0
    expr = ''
    par = []
    sub = ''
    resta = []
    while i <len(r):
        if(r[i] =='Ƈ'):
            par.append(i)
        if  r[i] == 'Ȱ':
            if(r[i-1] == 'Ɔ'):
    
                sub = r[par.pop():i]
                subl = len(sub)-1
                expr = expr[:-subl]
                expr = expr + sub
                expr = expr  +  'Ĭ' + 'εƆ'
            else:
                letra = expr[-1]
                expr = expr[:-1]
                expr = expr + 'Ƈ' + letra + 'Ĭ' + 'εƆ'
        else:
            expr = expr + r[i]
        i+=1

    return expr

## INGRESO DE CADENA Y REGEX

#r = input("ingrese la expresion regular: ")
#w = input("ingrese la cadena a evaluar: ")

# SI LA CADENA ESTA BIEN SIGUE SINO SE ACABA EL PROGRAMA
if(contar(r)):
    pass
else:
    print("Expresion no valida")
    print("Adios")
    sys.exit()

# ALTERACIONES AL REGEX
rAFD = r
r = arreglar1(r)
r = arreglar2(r)
print("EL NUEVO R",repr(r))

# INICIO DE AFD DIRECTO
# PARA FUTURO METERLO EN SU PROPIA CLASE
#print("*------------------AUTOMATA AFD DIRECTO-----------------------------*")

claseAFDD = arbol.Arbol()
values = []
ops = []
i = 0 
nodos = []
# AGREGANDO AL REGEX EL # FINAL Y LAS CONVERSIONES NECESARIA
rAFD = rAFD
rAFD = arreglar1(rAFD)
rAFD = arreglar2(rAFD) 
r = rAFD

#print("LA RE ES ", r)
operadoresUtils = ['ȹ','ɘ','Ƈ','Ɔ','Ĭ']
# SE UTILIZA LA MISMA LECTURA DE DATOS SOLO QUE ESTA VEZ PARA ARMAR EL ARBOL 
while i < len(r):
    if r[i] == 'Ƈ':
        ops.append(r[i])
    elif r[i] not in operadoresUtils:
        values.append(r[i])
    elif r[i] == 'Ɔ':
        while len(ops) != 0 and ops[-1] != 'Ƈ':
            op = ops.pop()
            if op != 'ɘ':
                val2 = values.pop()
                val1 = values.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == 'Ĭ'):
                    claseAFDD.crearHojasPipe(val1,val2,op)
                    #clase.crear_nodosPipe(val1,val2,op)
                    ##print("Para el pipe")
                elif(op == 'ȹ'):
                    #clase.crear_nodosCat(val1,val2,op)
                    claseAFDD.crear_nodosCat(val1,val2,op)
                    ##print("Para el concat")
                values.append(temp)
        ops.pop()
    else:
        if(r[i] != 'ɘ'):
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(r[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == 'Ĭ'):
                    claseAFDD.crearHojasPipe(val1,val2,op)
                    ##print("Para el pipe")
                elif(op == 'ȹ'):
                    claseAFDD.crear_nodosCat(val1,val2,op)
                    ##print("Para el concat")
                values.append(temp)
            ops.append(r[i])
        else:
            ##print("Entro al else")
            val1 = values.pop()
            op = r[i]
            temp = val1+op
            ##print('*------------ESTRELLA-------------*')
            claseAFDD.crear_nodosStar(val1,op)
            ##print("Para la estrella")
            nodos.append(temp)
            values.append(temp)
            #values.append(applyOp(val1, val2, op))
    i+=1
while len(ops) != 0:
    #print("entre aca")
    val2 = values.pop()
    val1 = values.pop()
    op = ops.pop()
    temp = val1+op+val2
    nodos.append(temp)
    if(op == 'Ĭ'):
        #print("Para el pipe")
        claseAFDD.crearHojasPipe(val1,val2,op)
    elif(op == 'ȹ'):
        claseAFDD.crear_nodosCat(val1,val2,op)
        #print("Para el concat")
        
    else:
        print("MMM ESTRELLA?")
    values.append(temp)


#OBTENCION DEL ARBOL
arboles = claseAFDD.get_nodos()
aceptacion = []

# EXTRACCION DE INFORMACION PARA ESTADO DE ACEPTACION
for i in arboles:
    if(i.get_valor() =='Ȟ'):
        aceptacion.append(i.get_iDImportante())
    '''
    if(len(i.get_hijos()) > 1):
        if(i.get_padreID() != ""):
            print("LA HOJA",i.get_id(),i.get_valor(),"ES HIJA DE",i.get_padreID().get_id(),"Y ES PADRE DE",i.get_hijos()[0].get_id(),"Y DE",i.get_hijos()[1].get_id())  
        else:
            print("LA HOJA",i.get_id(),i.get_valor(),"ES LA RAIZ Y ES PADRE DE",i.get_hijos()[0].get_id(), "Y DE",i.get_hijos()[1].get_id())
    elif(len(i.get_hijos()) == 1):
        print("LA HOJA",i.get_id(),i.get_valor(),"ES HIJA DE",i.get_padreID().get_id(),"Y ES PADRE DE",i.get_hijos()[0].get_id())
    else:
        print("LA HOJA",i.get_id(),i.get_valor(),"ES HIJA DE",i.get_padreID().get_id(),"Y NO TIENE HIJOS Y SU ID IMPORTANTE ES",i.get_iDImportante())
    '''
    
importantes = claseAFDD.get_importantValues()
#for elemento in importantes:
#    print(elemento[0].get_valor(), "numero",elemento[1],"id",elemento[2])
simbolos = []

# METODO PARA DETERMINAR SI EL ELEMENTO ES NULLABLE O NO

def nullable(elemento):
    #HAY QUE REVISAR SI ES HOJA O NO, SERA HOJA SI NO TIENE HIJOS
    if(len(elemento.get_hijos()) > 0):
        ##print("NO ES HOJA")
        if(elemento.get_valor() == "Ĭ"):
            ##print("C1 OR C2 NULLABLE")
            c1 = nullable(elemento.get_hijos()[0])
            c2 = nullable(elemento.get_hijos()[1])
            if(c1 or c2):
                ##print("ES NULLABLE")
                return True
            else:
                ##print("NO LO ES")
                return False

        elif(elemento.get_valor() == "ȹ"):
            ##print("C1 AND C2 NULLABLE")
            c1 = nullable(elemento.get_hijos()[0])
            c2 = nullable(elemento.get_hijos()[1])
            if(c1 and c2):
                ##print("ES NULLABLE")
                return True
            else:
                ##print("NO LO ES")
                return False
        else:
            return True
    else:
        ##print("ES HOJA")
        if(elemento.get_valor() != "ε"):
        
            return False
            
        else:
            return True

# METODO PARA OBTENER EL FIRSTPOS DEL ELEMENTO

def firstpos(elemento):
    #HAY QUE REVISAR SI ES HOJA O NO, SERA HOJA SI NO TIENE HIJOS
    if(len(elemento.get_hijos()) > 0):
        ##print("NO ES HOJA")
        if(elemento.get_valor() == "Ĭ"):
            c1 = firstpos(elemento.get_hijos()[0])
            c2 = firstpos(elemento.get_hijos()[1])
            resp = (c1)+(c2)
            return resp
        elif(elemento.get_valor() == "ȹ"):
            h1 = (elemento.get_hijos()[0])
            #print("-"*20)
            #print("EL HIJO 1 DE",elemento.get_valor(),elemento.get_id(),"es",h1.get_valor())
            #print("-"*20)
            if(nullable(h1)):
                c1 = firstpos(elemento.get_hijos()[0])
                c2 = firstpos(elemento.get_hijos()[1])
                resp = (c1)+(c2)
                return resp
            else:
                c1 = firstpos(elemento.get_hijos()[0])
                return c1
        else:
            return firstpos(elemento.get_hijos()[0])
    else:
        if(elemento.get_valor() != "ε"):
            return [elemento.get_iDImportante()]
        else:
            return []

# METODO PARA OBTENER EL LASTPOS DEL ELEMENTO

def lastpos(elemento):
    #HAY QUE REVISAR SI ES HOJA O NO, SERA HOJA SI NO TIENE HIJOS
    if(len(elemento.get_hijos()) > 0):
        ##print("NO ES HOJA")
        if(elemento.get_valor() == "Ĭ"):
            c1 = lastpos(elemento.get_hijos()[0])
            c2 = lastpos(elemento.get_hijos()[1])
            resp = (c1)+(c2)
            return resp
        elif(elemento.get_valor() == "ȹ"):
            h2 = (elemento.get_hijos()[1])
            if(nullable(h2)):
                c1 = lastpos(elemento.get_hijos()[0])
                c2 = lastpos(elemento.get_hijos()[1])
                resp = (c1)+(c2)
                return resp
            else:
                c2 = lastpos(elemento.get_hijos()[1])
                return c2
        else:
            return lastpos(elemento.get_hijos()[0])
    else:
        if(elemento.get_valor() != "ε"):
            return [elemento.get_iDImportante()]
        else:
            return []

# METODO PARA OBTENER EL FOLLOW POS DEL ELEMENTO

def followPos(elemento):
    #HAY QUE REVISAR SI ES HOJA O NO, SERA HOJA SI NO TIENE HIJOS
    if(len(elemento.get_hijos()) > 0):
        ##print("NO ES HOJA")
        if(elemento.get_valor() == "Ĭ"):
            c1 = lastpos(elemento.get_hijos()[0])
            c2 = lastpos(elemento.get_hijos()[1])
            resp = (c1)+(c2)
            return resp
        elif(elemento.get_valor() == "ȹ"):
            h2 = (elemento.get_hijos()[1])
            #print("EL HIJO 2 DE",elemento.get_valor(),"es",h2.get_valor())
            if(nullable(h2)):
                c1 = lastpos(elemento.get_hijos()[0])
                c2 = lastpos(elemento.get_hijos()[1])
                resp = (c1)+(c2)
                return resp
            else:
                c2 = lastpos(elemento.get_hijos()[1])
                return c2
        else:
            return lastpos(elemento.get_hijos()[0])
    else:
        if(elemento.get_valor() != "ε"):
            return [elemento.get_iDImportante()]
        else:
            return []



#OBTENCION DE LOS NOSOS
positions = []
for i in arboles:
    #print("El first pos de", i.get_valor() ,"es",firstpos(i),"y su lastpos es",lastpos(i))
    positions.append((i,firstpos(i),lastpos(i)))

followvalores = []
followPosition = []
followTotal = []
#print("*"*100)

#print("LAS POSITIONS",positions)

#ASIGNACION DEL FOLLOW POS
for i in positions:
    if(i[0].get_valor() == "ȹ"):
        #print("PARA EL PUNTO",i[0].get_valor(), i[0].get_hijos()[0].get_valor(),i[1],i[2])
        #print("PARA EL PUNTO",i[0].get_valor(), i[0].get_hijos()[1].get_valor(),i[1],i[2])
        hijo1 =  i[0].get_hijos()[0]
        hijo2 =  i[0].get_hijos()[1]
        for posicion in positions:
            if(posicion[0]==hijo1):
                #print("PARA LOS POS XD",posicion[2])
                followvalores.append(posicion[2])
                followTotal.append(posicion[2])
            if(posicion[0]==hijo2):
                #print("EL FOLLOW POS XD",posicion[1])
                followPosition.append(posicion[1])
                followTotal.append(posicion[1])

        #for contador in i[2]:
        #    #print("PARA LA POS XD", contador)


    elif(i[0].get_valor() == "ɘ"):
        #print("PARA EL ASTERISCO",i[0].get_valor(), i[0].get_hijos()[0].get_valor(),i[1],i[2])
        #print("PARA LA POS XD", i[2],"EL FOLLOW POS XD", i[1])
        followvalores.append(i[2])
        followPosition.append(i[1])
        followTotal.append(i[2])
        followTotal.append(i[1])




#print("*"*100)
#print("Estas posiciones se les asigna ", followvalores)
#print("Este valor de followpos", followPosition)
#print("*"*100)
def my_function(x):
      return list(dict.fromkeys(x))
diccionarioFollow = {}
conti = 0
for i in followvalores:
    
    for valor in i:
        #print("La posicion",valor,"va con el folllowpos",followPosition[conti])
        if(valor not in diccionarioFollow):
            #print("-------------Creando posicion",valor,"va con el folllowpos",followPosition[conti])
            diccionarioFollow[valor] = followPosition[conti]
        else:
            if(followPosition[conti] not in diccionarioFollow[valor]):
                for x in followPosition[conti]:
                    #print("--------------Sumando posicion",valor,"va con el folllowpos",x)
                    diccionarioFollow[valor].append(x)
    conti +=1

#print(diccionarioFollow)

for k,v in diccionarioFollow.items():
   diccionarioFollow[k] = my_function(v)

diccionarioFollow = {k: diccionarioFollow[k] for k in sorted(diccionarioFollow)}


#OBTENCION DE SIMBOLOS DEL ARBOL
for i in arboles:
    if(i.get_valor() != "Ȟ" and i.get_valor() != "ε" and len(i.get_hijos()) < 1):
        simbolos.append(i.get_valor())
resT = [] 
for i in simbolos: 
    if i not in resT: 
        resT.append(i) 
simbolos = resT

for i in positions:
    if(i[0].get_padreID() == ""):
        firstposRoot = i[1]

#print("-"*100)
#print(diccionarioFollow)    

#print(firstposRoot) 
#print(simbolos)
#print(importantes)
#print("-"*100)

# METODO PARA CREAR LOS ESTADOS DEL AUTOMATA FINAL 
def Directo(firstposRoot, simbolos, importantes):
    dEstates = [firstposRoot]
    numeros = []
    U = []
    transicionesNuevas = []
    for i in dEstates:
        ##print("MJM SIP",dEstates)
        for j in simbolos:
            for k in importantes:

                ##print(i,j,k[0].get_valor())
                ##print(k[0].get_iDImportante(), (k[0].get_iDImportante() in i))

                if(j == k[0].get_valor() and (k[0].get_iDImportante() in i)):
                    ##print("Si existe")
                    numeros.append(k[0].get_iDImportante())

            ##print("Para",i,j,numeros)


            for h in numeros:
                #print("NUMEROS",numeros)
                for k,v in diccionarioFollow.items():
                    if(h == k):
                        #print("********************El follow pos de",k,h,"es",v)
                        U += v                
            #print("U", U)
            test = []
            for letra in U:
                if letra not in test:
                    test.append(letra)
            U = test            
            if(U not in dEstates):
                ##print("Entramos")
                #print("U EN EL IF XD", U)
                dEstates.append(U)
            if(len(U)>=1):
                transicionesNuevas.append([i,j,U])

            U = []
            numeros.clear() 
    return transicionesNuevas, dEstates

#PRINTS NECESARIOS PARA DEBUGEAR
#print("firstposRoot",firstposRoot)
#print("simbolos",simbolos)
#print("importantes",importantes)
#for i in importantes:
#    print("importantes",i[0].get_valor(),i[0].get_id(),i[0].get_iDImportante())


#OBTENCION DE AUTOMATA
transicionesNuevas, dEstates = Directo(firstposRoot, simbolos, importantes)

#PRINTS NECESARIOS PARA DEBUGEAR
#for i in dEstates:
#    print("LA DESTASTE",i)

#PRINTS NECESARIOS PARA DEBUGEAR
#for i in transicionesNuevas:
#    print("LA TRANS",i)

#PRINTS NECESARIOS PARA DEBUGEAR
#for i in aceptacion:
#    print("LA Acept",i)


# SELECCION DE ESTADOS DE ACEPTACION
llave = []
aceptacionA = []
#print("NODOS ACEPTACION", aceptacion)
#print("-"*100)
#for k,v in token.items():
#    print(k,v)

dicAceptado = {}
contadorA = 0
for k,v in token.items():
    dicAceptado[k] = aceptacion[contadorA]
    contadorA +=1

#print("DICCIONARIO ACEPTACION",dicAceptado)
#print("-"*100)

for i in dEstates:
    for j in i:
        for acpt in aceptacion:
            if(j == acpt):
                llave.append(i)
 #PRINTS NECESARIOS PARA DEBUGEAR
#for i in llave:
#    print("LAs que tiene acpet",i)   

# CREACION DE DICCIONARO PARA ASIGNACION DE NUEVOS VALORES PARA LOS ESTADOS DE AUTOAMATA 
nuevoDic = {}
contador = 0
nuevosValores = dEstates.copy()
for i in nuevosValores:
    nuevoDic[tuple(i)] = contador
    contador +=1
for item in llave:
    aceptacionA.append(str(nuevoDic.get(tuple(item))))

for item in transicionesNuevas:
    item[0]= str(nuevoDic.get(tuple(item[0])))
    item[2]= str(nuevoDic.get(tuple(item[2])))

'''
for k, v in nuevoDic.items():
    print("LA LLAVE",k)
    print("EL VALOR",v)
'''

print("ACEPTACIONA",aceptacionA)
def get_key(my_dict,val):
    for key, value in my_dict.items():
        #print("EL VALUE",type(value))
        #print("EL ENCONTRADO",type(val))
        if val == str(value):
            return key
 
    return "key doesn't exist"
#METODO DE SIMULADION DEL AFD DIRECTO
def simulacionAFD(ini,trans,w,position):
    s = ini
    cont = 0
    sigue = True
    check = contadorW = position
    tokenR = ''
    estadoAceptacion = ''
    #print("EL LEN ES ",len(w))
    while(sigue and contadorW < len(w)):
        s = (mov(s, w[contadorW],trans))
        #print("LA S ES",s)
        #print("LA aceptacionA ES",aceptacionA)
        #for i in aceptacionA:
        #print("VERIFICANDO SI ",s[0],"ESTA EN",aceptacionA)

        if(len(s)>0 and str(s[0]) in aceptacionA):
            #print(s[0],"ESTA EN",estadoAceptacion)
            #print("ACEPATDO",w[contadorW])
            #print(get_key(nuevoDic,i))
            #print("-"*50)
            #print(nuevoDic)
            #print(dicAceptado)
            #print("-"*50)
            check = contadorW
            for key,value in dicAceptado.items():
                for x in get_key(nuevoDic,s[0]):
                    if(x == value):
                        estadoAceptacion = key
        if(len(s) == 0):
            #print("PARO")
            sigue = False
        contadorW+=1

    #print("Postion",position)
    #print("Check",check)
    tokenR = w[position:check+1]
    

    return tokenR, check+1, estadoAceptacion
   

# GRAFICACION
fad = Digraph('finite_state_machine', filename='fsmasd.gv')
fad.attr(rankdir='LR', size='8,5')
for i in aceptacionA:
    fad.attr('node', shape='doublecircle')
    fad.node(i)
estadosA = []


for i in transicionesNuevas:
    estadosA.append(i[0])
    estadosA.append(i[2])
    fad.attr('node', shape='circle')
    fad.edge(i[0], i[2], label=i[1])
#fad.view()

#LIMPIEZA DE ESTADOS DE ACEPTACION
resT = [] 
for i in estadosA: 
    if i not in resT: 
        resT.append(i) 
estadosA = resT

#IMPRESION DE DATOS EN TXT
archivo = f'''
*----------------AUTOMATA AFD DIRECTO-------------------------------*"
Estados = {estadosA}
Simbolos = {simbolos}
Inicio = {[transicionesNuevas[0][0]]}
Aceptacion = {aceptacionA}
Transiciones = {transicionesNuevas}
'''
print(archivo)
position = 0
while(position < len(w)):
    tokenR, position, estadoAceptacion = simulacionAFD([transicionesNuevas[0][0]],transicionesNuevas,w,position)

    if(len(estadoAceptacion) == 0):
        print("TOKEN",repr(tokenR)," NO RECONOCIDO")
    else:
        permitido = True
        if(len(excepcion)>0):
            for k,v in excepcion[estadoAceptacion].items():           
                if(tokenR == v):
                    permitido = False
                    print("TOKEN",repr(tokenR),"-> KEYWORD")
                    break
        if(permitido):
            print("TOKEN",repr(tokenR),"->", estadoAceptacion)



with open("FILE.txt", "a", encoding="utf-8") as f:
    f.write(archivo)
f.close()
