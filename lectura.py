import re
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)
def eliminarEspacio(lista):
    cont = 0
    for i in lista:
        if(i == ''):
            lista.pop(cont)
        
        cont+=1
    return lista
def juntar(lista):
    a = []
    for i in lista:
        i = i.replace(" ", '')
        a.append(i)

    return a
def removePunto(lista):
    a = []
    for i in lista:
        i = i.replace(".", '')
        a.append(i)

    return a
def checkCharacters(listaCheck):
    cont = 0
    todoB = True
    keyArray = []
    idents = []
    arrayOpIdent = []
    arrayOpStr = []
    arrayOpCHR = []
    arrayOpCH = []
    nuevoArray = []
    superSrtring = ""

    for i in listaCheck:
        superSrtring = ""
        arrayOpIdent = []
        arrayOpStr = []
        arrayOpCH = []
        arrayOpCHR = []
       # print("*"*50, i)
        #if("+' '." not in i):
        i = i.replace(" ", "")

        if(i != "CHARACTERS"):
            if "=" not in i:
                print("Error falta el signo igual en:",i)
                todoB = False
                break

            numIgual = i.find("=")
            beforeIgual = i[:numIgual]
            idents.append(beforeIgual)
            afterIgual = i[numIgual+1:]

            
            #print("EL AFERT",afterIgual)


            if (afterIgual.find("+") != -1 or afterIgual.find("-") != -1):
                contPuntos = 0
                #print("EL CHARACTER TIENE DENTRO UN SIMBOLO DE MAS O MENOS",i)
                #print("."*100)
                condicion = re.findall(r'\'(.*?)\'', i)
                #print(len(condicion))
                #print(condicion)
                #print("."*100)
                
                x = re.split("\+|\-",afterIgual)
                #print("Separadores de mas y menos",x)
                for xs in x:
                    if(xs.find("\"") != -1):
                        #print("ENTRO A IF 1")
                        arrayOpStr.append(xs)
                        
                    elif(xs.find("CHR") == 0 ):
                        #print("ENTRO A IF 2")
                        arrayOpCHR.append(xs)
                    elif(xs.startswith("'")):
                        #print("HAY UN A COMILLA SIMPLE",i)
                        arrayOpCH.append(xs)
                    elif(xs.find("ANY") != -1):
                        pass
                    else:
                        #print("ENTRO A ELSE")
                        arrayOpIdent.append(xs)
                #print("Array con strings",arrayOpStr)
               # print("Array con CHARS",arrayOpCHR)
                #arrayOpIdent = removePunto(arrayOpIdent)
                #print("Array con idents",arrayOpIdent)

                for charN in arrayOpCH:
                    
                    if(charN.endswith(".")):
                        contPuntos +=1
                    charN = charN.replace(".", "")
                    #print("EL CHAR N ES:", charN, "en",afterIgual)
                    if(charN == "''"):
                        #print("ENTRAMOS")
                        afterIgual = afterIgual.replace(charN,"\' \'")
                    else:
                        if(len(charN)==3):
                            pass
                        else:
                            print("CHAR INVALIDO",i)
                            #todoB = False
                            #break

                for chari in arrayOpCHR:
                    if(chari.endswith(".")):
                        contPuntos +=1
                    
                    chari = chari.replace(".", "")
                    
                    numeroCHR = chari.find("CHR(")
                    finCHR = chari.find(")")
                    aferCHR = chari[numeroCHR+4:finCHR]
                    #print(aferCHR)
                    if(aferCHR.isdigit()):
                        #print("No problem Char",aferCHR)
                        #print("QUE ES AFERCHR",aferCHR)
                        #print("QUE ES CHARI", chari)
                        pass
                        #afterIgual = afterIgual.replace(chari,chr(int(aferCHR)))
                    else:
                        print("Dentro del CHAR no hay un numero valido:",i)
                        todoB = False
                        break
                    if(chari.endswith(")") == False):
                        print("Problema con el CHAR", chari,"de la linea",i)
                        todoB = False
                        break
        
                for ide in arrayOpIdent:
                    if(ide.endswith(".")):
                        contPuntos +=1
                        ide = ide.replace(".", '')
                    if(ide in idents):
                     #   print("No problem ident")
                        pass
                    else:
                        print("No hay ident que haga match en array", i,"ident:", ide)
                        todoB = False
                        break
                for stri in arrayOpStr:
                    if(stri.endswith(".")):
                        contPuntos +=1
                    
                    stri = stri.replace(".", "")
                    
                    if (stri.startswith("\"")):
                        if(stri.count("\"") % 2 == 0 ):
                     #       print("No problem con el string XD", stri)
                            pass
                        else:
                            print("FALTA UN \" WEY en:", stri)
                            todoB = False
                            break
                    else:
                        print("Problema con este string",stri, "de la linea",i)
                        todoB = False
                        break


                #print(contPuntos)
                if(contPuntos == 0 or contPuntos>1):
                    print("Falta un punto o hay uno extra:",i)
                    #todoB = False
                    #break
                else:
                    pass
            else:
                #print("EL CHARACTER NO TIENE DENTRO UN SIMBOLO DE MAS O MENOS",i)
                #print("El AFTER",afterIgual)
                if (afterIgual.startswith("\"")):
                    #print("EL CHARACTER ES STRING",afterIgual)
                    if(afterIgual.count("\"") % 2 == 0 ):
                        pass
                    #    print("No problem", afterIgual)
                    else:
                        print("FALTA UN \" WEY")
                        todoB = False
                        break
                    if(afterIgual.endswith(".")):
                        pass
                    else:
                        print("FALTA EL PUNTO FINAL ",i)
                        todoB = False
                        break
                elif(afterIgual.find("CHR") != -1):
                    #print("EL CHARACTER ES CHAR",afterIgual)
                    #print(afterIgual.find("CHR"))
                    numeroCHR = afterIgual.find("CHR(")
                    finCHR = afterIgual.find(")")
                    aferCHR = afterIgual[numeroCHR+4:finCHR]
                    #print(aferCHR)
                    
                    if(aferCHR.isdigit()):
                        #print("No problem Char")
                        pass
                    else:
                        print("Dentro del CHAR no hay un numero valido:",i)
                        todoB = False
                        break
                    if(afterIgual.endswith(".")):
                        pass
                    else:
                        print("FALTA EL PUNTO FINAL ",i)
                        todoB = False
                        break
                    #print(aferCHR)
                    #afterIgual = chr(int(aferCHR))
                elif(afterIgual.find("..")!=-1):
                    #print("ES UN RANGO CHAR CON COMILLA", afterIgual)
                    if(afterIgual.endswith(".")):
                        pass
                    else:
                        print("LE FALTA UN PUNTO ", afterIgual)
                        todoB = False
                        break
                    afterIgual = afterIgual.replace("\'", "")
                    posiPunto = afterIgual.find("..")
                    charIincial = afterIgual[:posiPunto]
                    
                    charFinal = afterIgual[posiPunto+2:]
                    
                    charFinal = charFinal.replace(".", "")
                    #print(afterIgual)
                    #print(charIincial)
                    #print(charFinal)
                    if(len(charIincial) == 1 and len(charFinal) == 1):
                        
                        #for c in char_range(charIincial, charFinal):
                        #    superSrtring +=  c
                        
                        #afterIgual = superSrtring
                        pass
                    else:
                        print("Entrada no valida")
                        todoB = False
                        break
                    #print(charIincial.isalpha())
                    #print(charFinal.isalpha())
                    if(ord(charIincial) < (ord(charFinal))):
                        pass
                    else:
                        print("RANGO NO VALIDO")
                        todoB = False
                        break
                    
                    #char_range('a', 'z')
                elif(afterIgual.startswith("\'")):
                    if(afterIgual.endswith(".")):
                        pass
                    else:
                        print("LE FALTA UN PUNTO ", afterIgual)
                        todoB = False
                        break
                    #print("ES UN  CHAR CON COMILLA", afterIgual)
                    tempComilla = afterIgual
                    tempComilla = tempComilla.replace("\'", "")
                    tempComilla = tempComilla.replace(".", "")
                    #print(tempComilla)
                    if(len(tempComilla) ==1):
                        pass
                        afterIgual = afterIgual.replace("\'", "")
                    else:
                        print("Entrada no valida")
                        todoB = False
                        break
                elif(afterIgual.find("ANY") != -1):
                    if(afterIgual.endswith(".")):
                        pass    
                    else:
                        print("LE FALTA UN PUNTO ")
                        todoB = False
                        break
                else:
                    print("EL CHARACTER ES IDENT",afterIgual)
                    afterIgual = afterIgual.replace(".", "")
                    #print("No tiene strings")
                    if(afterIgual in idents):
                        pass
                        #print("No problem ident")
                    else:
                        print("No hay ident que haga match")
                        todoB = False
                        break
                    if(afterIgual.endswith(".")):
                        pass
                    else:
                        print("FALTA EL PUNTO FINAL ",i)
                        todoB = False
                        break
            #print(numIgual)
            #print(i)
            #print("IDENT", beforeIgual)
            #print("El AFTER",afterIgual)
            nuevoArray.append(beforeIgual)
            if(afterIgual.endswith(".")):
                afterIgual = afterIgual[:-1]
            nuevoArray.append(afterIgual)
            #afterIgual = afterIgual.replace(".", '')
            #afterIgual = afterIgual.replace("\"", '')
            #keyArray.append(afterIgual)
    return todoB, idents,nuevoArray
def checkKeyWords(listaCheck):
    nuevoArray = []
    cont = 0
    todoB = True
    keyArray = []
    for i in listaCheck:
        i = i.replace(" ", "")
        if(i != "KEYWORDS"):
            if "=" not in i:
                print("Error falta el signo igual en:",i)
                todoB = False
                break
            numIgual = i.find("=")
            # HAY QUE REVISAR SI EL BEFORE IGUAL O SEA EL IDENT NO TENGA COSAS QUE NO SEAN LETRAS O NUMEROS COMO
            # COMILLAS O SIGNOS DE ADMINRACION O COSAS ASI

            beforeIgual = i[:numIgual]
            afterIgual = i[numIgual+1:]
            if(beforeIgual.startswith("\"") == True or beforeIgual.endswith("\"") == True):
                print("Error en el ident en:",i)
                todoB = False
                break
            if(afterIgual.startswith("\"") == False):
                print("Error falta un \" en:",i)
                todoB = False
                break
            if(afterIgual.endswith("\".") == False):
                print("Error falta un \". en:",i)
                todoB = False
                break
            #print(numIgual)
            #print(i)
            #print(beforeIgual)
            #print(afterIgual)
            afterIgual = afterIgual.replace(".", '')
            afterIgual = afterIgual.replace("\"", '')
            keyArray.append(afterIgual)
            nuevoArray.append(beforeIgual)
            nuevoArray.append(afterIgual)
        

    return todoB,keyArray,nuevoArray
def removeExtra(lista):
    a = []
    for i in lista:
        i = " ".join(i.split())
        a.append(i)
    return a
def cantSigno(palabra,signoA,signoC,i):
    if(palabra.count(signoA) == palabra.count(signoC)):
        #print("Todo bien en",signoA,i)
        return True
    else:
        print("Te falta calle", i)
        return False
def checkTokens(lista):
    todoB = True
    llaves = []
    nuevoA = []
    for i in lista:
        #i = i.replace(" ","")
        #print(i)
        if(i != "TOKENS"):
            llaves = []
            #print("-"*50)
            if "=" not in i:
                print("Error falta el signo igual en:",i)
                todoB = False
                break
            else:
                numIgual = i.find("=")
                beforeIgual = i[:numIgual]
                afterIgual = i[numIgual+1:]
                #print(beforeIgual)
                #print(afterIgual)
                nuevoA.append(beforeIgual)
                nuevoA.append(afterIgual)
                #print("HAY",afterIgual.count("{"),"LLAVES")
                if(cantSigno(afterIgual,"{","}",i)):
                    pass
                else:
                    todoB = False
                    break
                if(cantSigno(afterIgual,"[","]",i)):
                    pass
                else:
                    todoB = False
                    break
                if(cantSigno(afterIgual,"(",")",i)):
                    pass
                else:
                    todoB = False
                    break
        
        
    return todoB, nuevoA
def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct
def removerPuntoChar(lista):
    a = [] 
    for i in lista:
        if i.endswith("."):
            i = i[:-1]
        i = i.replace("\"", "")
        a.append(i)
    return a

file = open('cocol.txt', 'r',encoding='utf-8')
compBool = False
charBool = False
keyBool = False
tokBool = False
characters = []
keywords = []
tokens = []
nuevosChars = []
#Lectura
for line in file:
    line = line.rstrip("\n")
    if("COMPILER" in line):
        #print("INICIO")
        compBool = True

    if("CHARACTERS" in line):
        #print("INICIO DE CHAR")
        print(line)
        charBool = True
        keyBool = False
        tokBool = False
    elif("KEYWORDS" in line and not "EXCEPT" in line):
        #print("INICIO DE KEY")
        print(line)
        charBool = False
        keyBool = True
        tokBool = False
    elif("TOKENS" in line):
        #print("INICIO DE TOK")
        print(line)
        charBool = False
        keyBool = False
        tokBool = True
    elif("PRODUCTIONS" in line):
        #print("INICIO DE TOK")
        print(line)
        charBool = False
        keyBool = False
        tokBool = False
    elif("IGNORE" in line):
        #print("INICIO DE TOK")
        print(line)
        charBool = False
        keyBool = False
        tokBool = False
    elif("END" in line):
        #print("INICIO DE TOK")
        print(line)
        charBool = False
        keyBool = False
        tokBool = False
    

    if(charBool):
        if(line.endswith(".") == False and "CHARACTERS" not in line and "=" not in line):
            characters[-1] =  characters[-1] + line
        elif(line.endswith(".") == True and "=" not in line):
            characters[-1] =  characters[-1] + line
        else:
            #print("LA LINEA",line)
            characters.append(line)
      

    elif(tokBool):

        if(line.endswith(".") == False and "TOKENS" not in line and "=" not in line):

            tokens[-1] =  tokens[-1] + line
        elif(line.endswith(".") == True and "=" not in line):
            tokens[-1] =  tokens[-1] + line
        else:
            #print("LA LINEA",line)
            tokens.append(line)

    elif(keyBool):

        if(line.endswith(".") == False and "KEYWORDS" not in line and "=" not in line):
            keywords[-1] =  keywords[-1] + line
        elif(line.endswith(".") == True and "=" not in line):
            keywords[-1] =  keywords[-1] + line
        else:
            #print("LA LINEA",line)
            keywords.append(line)

    else:
        pass


# TRANSFORMACIONES NECESARIAS DE LAS KEYWORDS PARA QUITAR CUALQUIER ESPACIO VACIO COMO POSICION EXTRA
keywords = eliminarEspacio(keywords)
# TRANSFORMACIONES NECESARIAS DE LA KEYWORD PARA QUITAR LOS ESPACIOS EN BLANCO ENTRE CADA POSICION DEL ARRAY
keywords = juntar(keywords)
# TRANSFORMACIONES NECESARIAS DE LAS KEYWORDS PARA QUITAR CUALQUIER ESPACIO VACIO COMO POSICION EXTRA
keywords = removeExtra(keywords)


# TRANSFORMACIONES NECESARIAS DE LOS CHARACTERS PARA QUITAR CUALQUIER ESPACIO VACIO COMO POSICION EXTRA
characters = eliminarEspacio(characters)
# TRANSFORMACIONES NECESARIAS DE LOS CHARACTERS PARA QUITAR CUALQUIER ESPACIO VACIO COMO POSICION EXTRA
characters = removeExtra(characters)

# TRANSFORMACIONES NECESARIAS DE LOS TOKENS PARA QUITAR CUALQUIER ESPACIO VACIO COMO POSICION EXTRA
tokens = eliminarEspacio(tokens)
# TRANSFORMACIONES NECESARIAS DE LOS TOKENS PARA QUITAR CUALQUIER ESPACIO VACIO COMO POSICION EXTRA
tokens = removeExtra(tokens)

print(keywords)
print(characters)
print(tokens)
print("*"*100)
'''
---------------------------------------- EL METODO PARA REVISAR KEYWORDS
'''
validoK, kewordArray, nuevasKeywords = checkKeyWords(keywords)
if(validoK):
    print("Keywords sin problemas")

else:
    print("Error con las Keywords")
'''
---------------------------------------- EL METODO PARA REVISAR CHARACTERS
'''
identsCharacter= []
validoC, identsCharacter,nuevosChars = checkCharacters(characters)
if(validoC):
    print("Characters sin problemas")
else:
    print("Error con los Characters")
'''
---------------------------------------- EL METODO PARA REVISAR TOKENS
'''
validoT, nuevoTokens = checkTokens(tokens)
if(validoT):
    print("Tokens sin problemas")
else:
    print("Error con los Tokens")
print("*"*100)



def sustituirComillas(dicty):
    for k,v in dicty.items():
        temp = ''
        for char in v:
            if(char == "\""):
                temp+=chr(1000)
            else:
                temp+=char
        dicty[k] = temp
    return dicty
def cambioCHR(dicty):
    for k,v in dicty.items():
        superSrtring = ""
        temp =""
        if v.find("..") != -1:
            if(v.find("CHR(") != -1):
                #print("--------------------Entro a chr")
                posCHR = v.find("CHR(")
                finCHR1 = v.find(")")
                aferCHR1 = v[posCHR+4:finCHR1]
                #print("posCHR",posCHR)
                #print("finCHR1",finCHR1)
                #print("aferCHR1*************",aferCHR1)

                posPunto = v.find("..")
                #print("POSPunto----------", posPunto,v)
                #charIincial = v[:posPunto]
                charFinal = v[posPunto+6:-1]
                
                #print("charIincial:",charIincial)
                #print("charFinal********:",charFinal)

                for c in char_range(chr(int(aferCHR1)), chr(int(charFinal))):
                    superSrtring +=  c
                superSrtring = chr(1000)+superSrtring+chr(1000)
                dicty[k] = superSrtring 

            else:
                posPunto = v.find("..")
                #print("POSPunto", posPunto,v)
                charIincial = v[:posPunto]
                charFinal = v[posPunto+2:]
                #print("charIincial:",charIincial)
                #print("charFinal:",charFinal)
                for c in char_range(charIincial, charFinal):
                    superSrtring +=  c
                superSrtring = chr(1000)+superSrtring+chr(1000)
                #print("el superSrtring",superSrtring)
                dicty[k] = superSrtring 
        else:
            for i in v:
                if(i == "\""):
                    temp+=chr(1000)
                else:
                    temp+=i
            superSrtring = temp

            if(v.find("CHR(") != -1):
                temp = superSrtring
                
                while(temp.find("CHR(")!=-1):
                    #print("--------------temp Inicio---",temp)
                    numeroCHR = temp.find("CHR(")
                    #print("------INICIO CHR---",numeroCHR)
                    finCHR = temp.find(")",numeroCHR)
                    #print("------FIN CHR---",finCHR)
                    aferCHR = temp[numeroCHR+4:finCHR]
                    #print("---------EL VALOR A CAMBIAR---",aferCHR)
                    #print("*********",aferCHR)
                    temp  = temp[:numeroCHR]+ chr(1000)+chr(int(aferCHR))+chr(1000)+temp[finCHR+1:]
                    #print("--------------temp---",temp)

                superSrtring = temp
                dicty[k] = superSrtring 
    return dicty
def cambioAny(dicty):
    
    for k,v in dicty.items():
        superSrtring =""
        if(v.find("ANY") !=-1):
            posAny = v.find("ANY")
            for c in char_range(chr(0), chr(255)):
                superSrtring +=  c
            
            superSrtring = chr(1000)+superSrtring+chr(1000)
            superSrtring = v.replace("ANY",superSrtring)

            dicty[k] = superSrtring
    return dicty
def sustitucionVariables(dicty):
    llavesT = []

    for key in sorted(dicty,key=len, reverse=True):
        llavesT.append(key)

    #print("------------LLAVES",llaves)

    for key in sorted(dicty,key=len, reverse=True):
        for i in llavesT:
            if(i in dicty[key]):
                dicty[key] = dicty[key].replace(i ,dicty[i])
    return dicty
def operaciones(dicty):
    for k,v in dicty.items():
        string = False
        posSignos = []
        primera = False
        calculo = False
        tmep = ""
        segunda =""
        operador=""
        cont=0
        #print("*-*-*-*-*-*-",len(v))
        while cont < len(v):
            if (not(primera)):
                if (v[cont] == chr(1000)):
                    string = not(string)
                if string:
                    #print(tmep)
                    tmep+=v[cont]
                else:
                    primera = True
                    respuesta = tmep[1:]
            else:
                if v[cont] == chr(1000):
                    string = not(string)
                if(not(string) and v[cont] == "+") or (not(string) and v[cont] =="-"):
                    operador = v[cont]
                else:
                    if string:
                        segunda += v[cont]
                    else:
                        if operador == "+" and not(string):
                            segunda=segunda[1:]
                            respuesta = respuesta+segunda
                            calculo = True
                        elif(operador =="-" and not(string)):
                            segunda = segunda[1:]
                            respuesta = respuesta.translate({ord(i): None for i in segunda})
                            calculo = True
                        if calculo:
                            op = ""
                            segunda = ""
            cont+=1
        dicty[k] = respuesta
    return dicty
def pipesChar(dicty):
    for key, value in dicty.items():
        megaString = ""
        pos = -1
        for i in value:
            pos += 1
            if pos != len(value) - 1:
                megaString += i+"|"
            else:
                megaString += i
        dicty[key] = megaString
    return dicty
def modoAutomata(dictyT):
    for key, value in dictyT.items():
        for i in value:
            if(i == "{"):
                dictyT[key] = dictyT[key].replace(i, "(")
            elif(i == "}"):
                dictyT[key] = dictyT[key].replace(i, ")*")
    return dictyT
def modoAuto2(dictyT,dicty):
    for key, value in dictyT.items():
        for i in reversed(dicty):
            dictyT[key] = dictyT[key].replace(i, "("+dicty[i]+")")
    return dictyT
def exceptiones(dictyE, dictyT, dictyK):
    
    for k,v in dictyT.items():
        for k1,v1 in dictyK.items():
            if("EXCEPT KEYWORDS" in v):
                dictyE[k] = dictyK
            else:
                dictyE[k] = {}
    return dictyE
def removeExcept(dictyT):
    for k,v in dictyT.items():
        temp = {}
        tempS = ""
        ex = v.find("EXCEPT")
        #print("EX",ex,"PARA",v)
        if(ex != -1):
            temp[k] = v[:ex-1].lstrip()
        else:
            temp[k] = v[:-1].lstrip()
        dictyT[k] = temp[k]
    return dictyT

nuevoDic = Convert(nuevosChars)
#print("DICCIONARIO SIN PUNTOS",nuevoDic   )
#print()
nuevoDic = sustituirComillas(nuevoDic)
#print("DICCIONARIO SIN COMILLAS",nuevoDic   )
nuevoDic = cambioCHR(nuevoDic)
#print()
#print("DICCIONARIO SIN ..",nuevoDic   )
nuevoDic = cambioAny(nuevoDic)
#print()
#print("DICCIONARIO SIN ANY.",nuevoDic   )
nuevoDic = sustitucionVariables(nuevoDic)
#print()
#print("DICCIONARIO SUSTITUIDO", nuevoDic)
#print()
nuevoDic = operaciones(nuevoDic)
print("DICCIONARIO OPERADO", nuevoDic)
print()


nuevoDicK = Convert(nuevasKeywords)
nuevodicT = Convert(nuevoTokens)
print("NUEVO DICT 1",nuevodicT)
print()
#print("REMPLAZO DE PIPES")
nuevoDic = pipesChar(nuevoDic)

#REEMPLAZO DE LOS PARENTESIS Y DE LOS CORCHETES POR SIMBOLOS DE AUTOMATA
nuevodicT = modoAutomata(nuevodicT)
print("NUEVO DICT modoAutomata",nuevodicT)
print()
#SUSTITUYENDO EN TOKENS EN PARENTESIS
nuevodicT = modoAuto2(nuevodicT,nuevoDic)
print("NUEVO DICT MODOAUTO2",nuevodicT)
print()
#CREANDO DICCIONARIO CON LAS EXCEPCIONES
dictExcept = {}   
dictExcept = exceptiones(dictExcept, nuevodicT, nuevoDicK)
#QUITAMOS LOS EXPET DE LOS TOKENS
nuevodicT = removeExcept(nuevodicT)

print("*"*100)
print("FINAL")
print("*"*100)
print("TOKENS QUE VAN AL AUTOMATA")
print(nuevodicT)
print()
print()
print("*"*100)
print("KEYWORDS PARA REVISAR EN EL EXCEPT")
print(nuevoDicK)
print()
print("*"*100)
print("EXCEPT")
print(dictExcept)

superToken = ""
#print("---------------------------------------",)
for k,v in nuevodicT.items():
    if(nuevodicT[k] != nuevodicT[list(nuevodicT)[-1]] ):
        superToken += "("+v+")#|"
    else:
        superToken +=  "("+v+")#"

print("EL SUPER TOKEN")
print(repr(superToken))


multiline_str = """
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
rAFD = rAFD
rAFD = arreglar1(rAFD)
rAFD = arreglar2(rAFD) 
r = rAFD

#print("LA RE ES ", r)

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
    #print("entre aca")
    val2 = values.pop()
    val1 = values.pop()
    op = ops.pop()
    temp = val1+op+val2
    nodos.append(temp)
    if(op == '|'):
        #print("Para el pipe")
        claseAFDD.crearHojasPipe(val1,val2,op)
    elif(op == '.'):
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
    if(i.get_valor() =='#'):
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

#print("LAS POSITIONS",positions)

#ASIGNACION DEL FOLLOW POS
for i in positions:
    if(i[0].get_valor() == "."):
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


    elif(i[0].get_valor() == "*"):
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
                #print("--------------Sumando posicion",valor,"va con el folllowpos",followPosition[conti][0])
                diccionarioFollow[valor].append(followPosition[conti][0])
    conti +=1

#print(diccionarioFollow)

for k,v in diccionarioFollow.items():
   diccionarioFollow[k] = my_function(v)

diccionarioFollow = {k: diccionarioFollow[k] for k in sorted(diccionarioFollow)}

# ARRAY DE DE TAMAÑO PARA RECIBIR LOS VALORES DE FOLLOW POS
respuesta = []
for i in followvalores:
    for j in i:
        respuesta.append([j])

#PRINTS NECESARIOS PARA DEBUGEAR
#print("POSICIONES A LLENAR FOLLOW POS",respuesta)
#for i in respuesta:
#    print("POSICIONES A LLENAR FOLLOW POS",i)

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
#print("LA REST",rest)

respuesta = rest
for i in respuesta:
    if(len(i) < 1):
        ##print("LA",i)
        respuesta.remove(i)


#PRINTS NECESARIOS PARA DEBUGEAR
#print("Llenar con",respuesta)
#for i in respuesta:
#    print("LLENAR CON",i)


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

#print("-"*100)
#print(diccionarioFollow)    
#print(respuesta)   
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

#print("LA RESPUESTA3",respuesta)
#for i in respuesta:
#    print("LA RESPUESTA3",i)

# SELECCION DE ESTADOS DE ACEPTACION
llave = []
aceptacionA = []
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
"""

#file1 = open("programaGenerado.py", "w+")
#with open("programaGenerado.py","w+") as file1:
#    file1.writelines(multiline_str)
#file1.close()

import io
with io.open("programaGenerado.py", "w", encoding="utf-8") as f:
    f.write(multiline_str)