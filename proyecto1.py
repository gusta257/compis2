import arbol
from graphviz import Digraph
import sys

# METODO PARA ASIGNAR QUE OPERACION TIENE MAS PRECEDENCIA QUE OTRO EN ESTE ORDEN DESC: * -> . -> |
def precedence(op):
    if (op == '*'):
        return 3
    if (op == '.'):
        return 2
    if (op == '|'):
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
        if(i == "("):
            cont1+=1
        if(i==")"):
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
        if (r[i] == '|'):
            cont = 0
        elif(r[i] == '('):
            if (cont == 1):
                expr = expr + '.'
                cont = 0;
        elif(r[i] == ')' or r[i] == '*'):
            pass
        else:
            cont = cont + 1
        if(cont == 2):
            expr = expr+'.'+r[i]
            cont = 1
        else:
            expr = expr + r[i]
        i += 1
    return expr

# METODO QUE CONVIERTE LAS EXPRESIONES REGULARES EN SUS OTRAS FORMAS
# (A)+ -> (A)*(A)
# (A)? -> (A|ε)
def arreglar1(r):
    #ε
    i = 0
    expr = ''
    par = []
    sub = ''
    resta = []
    while i <len(r):
        if(r[i] =='('):
            par.append(i)
        if r[i] == '+':
            
            if(r[i-1] == ')'):

                sub = r[par.pop():i]
                
                expr = expr + '*' + sub
            else:
                expr = expr + '*' + r[i-1]
        elif r[i] == '?':
            if(r[i-1] == ')'):
    
                sub = r[par.pop():i]
                subl = len(sub)-1
                expr = expr[:-subl]
                expr = expr + sub
                expr = expr  +  '|' + 'ε)'
            else:
                letra = expr[-1]
                expr = expr[:-1]
                expr = expr + '(' + letra + '|' + 'ε)'
        else:
            expr = expr + r[i]
        i+=1

    return expr

## INGRESO DE CADENA Y REGEX

r = input("ingrese la expresion regular: ")
w = input("ingrese la cadena a evaluar: ")

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


# INICIO DE AFD DIRECTO
# PARA FUTURO METERLO EN SU PROPIA CLASE
#print("*------------------AUTOMATA AFD DIRECTO-----------------------------*")

claseAFDD = arbol.Arbol()
values = []
ops = []
i = 0 
nodos = []
# AGREGANDO AL REGEX EL # FINAL Y LAS CONVERSIONES NECESARIA
rAFD = "("+rAFD+")#"
rAFD = arreglar1(rAFD)
rAFD = arreglar2(rAFD) 
r = rAFD

# SE UTILIZA LA MISMA LECTURA DE DATOS SOLO QUE ESTA VEZ PARA ARMAR EL ARBOL 
while i < len(r):
    if r[i] == '(':
        ops.append(r[i])
    elif r[i].isalpha() or r[i].isdigit() or r[i] == '#':
        values.append(r[i])
    elif r[i] == ')':
        while len(ops) != 0 and ops[-1] != '(':
            op = ops.pop()
            if op != '*':
                val2 = values.pop()
                val1 = values.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == '|'):
                    claseAFDD.crearHojasPipe(val1,val2,op)
                    #clase.crear_nodosPipe(val1,val2,op)
                    ##print("Para el pipe")
                elif(op == '.'):
                    #clase.crear_nodosCat(val1,val2,op)
                    claseAFDD.crear_nodosCat(val1,val2,op)
                    ##print("Para el concat")
                values.append(temp)
        ops.pop()
    else:
        if(r[i] != '*'):
            while (len(ops) != 0 and precedence(ops[-1]) >= precedence(r[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()
                temp = val1+op+val2
                nodos.append(temp)
                if(op == '|'):
                    claseAFDD.crearHojasPipe(val1,val2,op)
                    ##print("Para el pipe")
                elif(op == '.'):
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
    ##print("entre aca")
    val2 = values.pop()
    val1 = values.pop()
    op = ops.pop()
    temp = val1+op+val2
    nodos.append(temp)
    if(op == '|'):
        ##print("Para el pipe")
        claseAFDD.crearHojasPipe(val1,val2,op)
    elif(op == '.'):
        claseAFDD.crear_nodosCat(val1,val2,op)
        ##print("Para el concat")
        
    else:
        print("MMM ESTRELLA?")
    values.append(temp)


#OBTENCION DEL ARBOL
arboles = claseAFDD.get_nodos()
aceptacion = []

# EXTRACCION DE INFORMACION PARA ESTADO DE ACEPTACION
for i in arboles:
    if(i.get_valor() =='#'):
        aceptacion.append(i.get_iDImportante())
    #if(len(i.get_hijos()) > 1):
    #    if(i.get_padreID() != ""):
    #        print("LA HOJA",i.get_id(),i.get_valor(),"ES HIJA DE",i.get_padreID().get_id(),"Y ES PADRE DE",i.get_hijos()[0].get_id(),"Y DE",i.get_hijos()[1].get_id())  
    #    else:
    #        print("LA HOJA",i.get_id(),i.get_valor(),"ES LA RAIZ Y ES PADRE DE",i.get_hijos()[0].get_id(), "Y DE",i.get_hijos()[1].get_id())
    #elif(len(i.get_hijos()) == 1):
    #    print("LA HOJA",i.get_id(),i.get_valor(),"ES HIJA DE",i.get_padreID().get_id(),"Y ES PADRE DE",i.get_hijos()[0].get_id())
    #else:
    #    print("LA HOJA",i.get_id(),i.get_valor(),"ES HIJA DE",i.get_padreID().get_id(),"Y NO TIENE HIJOS Y SU ID IMPORTANTE ES",i.get_iDImportante())

importantes = claseAFDD.get_importantValues()
#for elemento in importantes:
#    print(elemento[0].get_valor(), "numero",elemento[1],"id",elemento[2])
simbolos = []

# METODO PARA DETERMINAR SI EL ELEMENTO ES NULLABLE O NO

def nullable(elemento):
    #HAY QUE REVISAR SI ES HOJA O NO, SERA HOJA SI NO TIENE HIJOS
    if(len(elemento.get_hijos()) > 0):
        ##print("NO ES HOJA")
        if(elemento.get_valor() == "|"):
            ##print("C1 OR C2 NULLABLE")
            c1 = nullable(elemento.get_hijos()[0])
            c2 = nullable(elemento.get_hijos()[1])
            if(c1 or c2):
                ##print("ES NULLABLE")
                return True
            else:
                ##print("NO LO ES")
                return False

        elif(elemento.get_valor() == "."):
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
        if(elemento.get_valor() == "|"):
            c1 = firstpos(elemento.get_hijos()[0])
            c2 = firstpos(elemento.get_hijos()[1])
            resp = (c1)+(c2)
            return resp
        elif(elemento.get_valor() == "."):
            h1 = (elemento.get_hijos()[0])
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
        if(elemento.get_valor() == "|"):
            c1 = lastpos(elemento.get_hijos()[0])
            c2 = lastpos(elemento.get_hijos()[1])
            resp = (c1)+(c2)
            return resp
        elif(elemento.get_valor() == "."):
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
        if(elemento.get_valor() == "|"):
            c1 = lastpos(elemento.get_hijos()[0])
            c2 = lastpos(elemento.get_hijos()[1])
            resp = (c1)+(c2)
            return resp
        elif(elemento.get_valor() == "."):
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



#OBTENCION DE LOS NOSOS
positions = []
for i in arboles:
    #print("El first pos de", i.get_valor() ,"es",firstpos(i),"y su lastpos es",lastpos(i))
    positions.append((i,firstpos(i),lastpos(i)))
followvalores = []
followPosition = []
followTotal = []
#print("*"*100)

#ASIGNACION DEL FOLLOW POS
for i in positions:
    if(i[0].get_valor() == "."):
        ##print(i[0].get_valor(), i[0].get_hijos()[0].get_valor(),i[1],i[2])
        ##print(i[0].get_valor(), i[0].get_hijos()[1].get_valor(),i[1],i[2])
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


    elif(i[0].get_valor() == "*"):
        #print(i[0].get_valor(), i[0].get_hijos()[0].get_valor(),i[1],i[2])
        #print("PARA LA POS XD", i[2],"EL FOLLOW POS XD", i[1])
        followvalores.append(i[2])
        followPosition.append(i[1])
        followTotal.append(i[2])
        followTotal.append(i[1])




# ARRAY DE DE TAMAÑO PARA RECIBIR LOS VALORES DE FOLLOW POS
respuesta = []
for i in followvalores:
    for j in i:
        respuesta.append([j])

#LLENADO DE VALORES DE FOLLOW POS
for i in range(len(followvalores)):
    for j in followvalores[i]:
        for asd in followPosition[i]:
            respuesta[j-1].append(asd)
for i in respuesta:
    i.pop(0)
cont = 0
for i in (respuesta):
    if(len(i)==0):
        cont+=1
    if (cont>1 and len(i)==0):
        respuesta.remove(i)
rest = []
for elem in respuesta: 
    a = list(set(elem))
    rest.append(a)
respuesta = rest
for i in respuesta:
    if(len(i) < 1):
        ##print("LA",i)
        respuesta.remove(i)


#OBTENCION DE SIMBOLOS DEL ARBOL
for i in arboles:
    if(i.get_valor() != "#" and i.get_valor() != "ε" and len(i.get_hijos()) < 1):
        simbolos.append(i.get_valor())
resT = [] 
for i in simbolos: 
    if i not in resT: 
        resT.append(i) 
simbolos = resT

for i in positions:
    if(i[0].get_padreID() == ""):
        firstposRoot = i[1]

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
                ##print("el index",h)
                U += respuesta[h-1]
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

#OBTENCION DE AUTOMATA
transicionesNuevas, dEstates = Directo(firstposRoot, simbolos, importantes)

# SELECCION DE ESTADOS DE ACEPTACION
llave = []
aceptacionA = []
for i in dEstates:
    for j in i:
        if(j == aceptacion[0]):
            llave.append(i)

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


#METODO DE SIMULADION DEL AFD DIRECTO
def simulacionAFD(ini,trans):
    s = ini
    cont = 0
    for c in w:
        s = (mov(s, c,trans))
    for i in aceptacionA:
        if(i in s):
            cont+=1
    if(cont>=1):
        print("SI PARA EL AFD")
    else:
        print("NO PARA EL AFD")

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
fad.view()

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
simulacionAFD([transicionesNuevas[0][0]],transicionesNuevas)
with open("FILE.txt", "a", encoding="utf-8") as f:
    f.write(archivo)
f.close()