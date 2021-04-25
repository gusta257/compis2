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
                print("."*100)
                condicion = re.findall(r'\'(.*?)\'', i)
                print(len(condicion))
                print(condicion)
                print("."*100)
                
                x = re.split("\+|\-",afterIgual)
                print("Separadores de mas y menos",x)
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
                    else:
                        #print("ENTRO A ELSE")
                        arrayOpIdent.append(xs)
                #print("Array con strings",arrayOpStr)
                print("Array con CHARS",arrayOpCHR)
                #arrayOpIdent = removePunto(arrayOpIdent)
                #print("Array con idents",arrayOpIdent)

                for charN in arrayOpCH:
                    
                    if(charN.endswith(".")):
                        contPuntos +=1
                    charN = charN.replace(".", "")
                    print("EL CHAR N ES:", charN)
                    if(charN == "''"):
                        print("ENTRAMOS")
                        afterIgual = afterIgual.replace(charN,"\' \'")
                    else:
                        if(len(charN)==3):
                            pass
                        else:
                            print("CHAR INVALIDO",i)
                            todoB = False
                            break

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
                        afterIgual = afterIgual.replace(chari,chr(int(aferCHR)))
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
                        print("No hay ident que haga match en", i,"ident:", ide)
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
                    todoB = False
                    break
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
                    afterIgual = chr(int(aferCHR))
                elif(afterIgual.find("..")!=-1):
                    #print("ES UN RANGO CHAR CON COMILLA", afterIgual)
                    if(afterIgual.endswith(".")):
                        pass
                    else:
                        print("LE FALTA UN PUNTO ")
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
                        
                        for c in char_range(charIincial, charFinal):
                            superSrtring +=  c
                        
                        afterIgual = superSrtring
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
                        print("LE FALTA UN PUNTO ")
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
            nuevoArray.append(afterIgual)
            afterIgual = afterIgual.replace(".", '')
            afterIgual = afterIgual.replace("\"", '')
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

file = open('cocol.txt', 'r')
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



keywords = eliminarEspacio(keywords)
keywords = juntar(keywords)
keywords = removeExtra(keywords)
characters = eliminarEspacio(characters)
characters = removeExtra(characters)
tokens = eliminarEspacio(tokens)
print(keywords)
print(characters)
tokens = removeExtra(tokens)
print(tokens)

print("*"*100)
'''
EL METODO PARA REVISAR KEYWORDS
'''
validoK, kewordArray, nuevasKeywords = checkKeyWords(keywords)
if(validoK):
    print("Todo bien Jose Luis keywords")
    #print(keywords)
else:
    print("Error")
#print("*"*100)
'''
EL METODO PARA REVISAR CHARACTERS
'''
identsCharacter= []
validoC, identsCharacter,nuevosChars = checkCharacters(characters)
if(validoC):
    print("Todo bien Jose Luis characters")
    #print(characters)

else:
    print("Error")
#print("*"*100)
'''
EL METODO PARA REVISAR TOKENS
'''
validoT, nuevoTokens = checkTokens(tokens)
if(validoT):
    print("Todo bien Jose Luis tokens")
    #print(tokens)

else:
    print("Error")




llaves = []
nuevosChars = removerPuntoChar(nuevosChars)

nuevoDic = Convert(nuevosChars)
nuevoDicK = Convert(nuevasKeywords)
nuevodicT = Convert(nuevoTokens)
'''
print("-"*100)
print("CHARS PASADO A DIC")
print(nuevoDic)
print("-"*100)
print("KEYS PASADO A DIC")
print(nuevoDicK)
print("-"*100)
print("TOKENS PASADO A DIC")
print(nuevodicT)
print("-"*100)
'''
prueba = ""

for key in sorted(nuevoDic,key=len, reverse=True):
    llaves.append(key)

for key in sorted(nuevoDic,key=len, reverse=True):
    for i in llaves:
        if(i in nuevoDic[key]):
            nuevoDic[key] = nuevoDic[key].replace(i ,nuevoDic[i])

#print("*"*100)
#print("EL REEMPLAZO DE VARIABLES")
#print(nuevoDic)

for key, values in nuevoDic.items():
    
    while nuevoDic[key].find("-") > -1:
        #print("EL DIC DE PORQUEERIA",nuevoDic[key])
    #if(values.find("-")>-1):
        #print(key)
        temp_index =  nuevoDic[key].find("-")
        #print("El temp_index del inicio del ciclo",temp_index)
        if( nuevoDic[key].find("+",temp_index+1) > -1):
            next_index =  nuevoDic[key].find("+",temp_index+1)
        elif( nuevoDic[key].find("-",temp_index+1) > -1):
            next_index =  nuevoDic[key].find("-",temp_index+1)
        else:
            next_index = -1
        #print("next_index",next_index)
        first_element =  nuevoDic[key][:temp_index]
        #print("first element",first_element)
        if next_index > -1:
            second_element =  nuevoDic[key][temp_index+1:next_index]
            #print("second_element",second_element)
            cont_word =  nuevoDic[key][next_index:]
            new_word = first_element.translate({ord(i): None for i in second_element})
            #print("la cont_word",cont_word)
            #print("la new_word",new_word)
            nuevoDic[key] = new_word+cont_word
            #print("el nuevo value",nuevoDic[key])
        else:
            second_element =  nuevoDic[key][temp_index+1:]
            #print("el second_element",second_element)
            new_word = first_element.translate({ord(i): None for i in second_element})
            nuevoDic[key] = new_word
        
    if("+" in  values):
        #print("HAY CAMBIO DE SUMA", key, values)
        nuevoDic[key] = nuevoDic[key].replace("+", "")
    
    
        
#print("*"*100)
#print("REMPLAZO DE SUAS Y RESTAS")
#print(nuevoDic)


for key, value in nuevoDic.items():
    megaString = ""
    pos = -1
    for i in value:
        pos += 1
        if pos != len(value) - 1:
            megaString += i+"|"
        else:
            megaString += i
    nuevoDic[key] = megaString

#print("*"*100)
#print("REMPLAZO DE PIPES")
#print(nuevoDic)
#print("*"*100)



for key, value in nuevodicT.items():
    for i in value:
        if(i == "{"):
            nuevodicT[key] = nuevodicT[key].replace(i, "(")
        elif(i == "}"):
            nuevodicT[key] = nuevodicT[key].replace(i, ")*")

for key, value in nuevodicT.items():
    for i in nuevoDic:
        nuevodicT[key] = nuevodicT[key].replace(i, "("+nuevoDic[i]+")")

dictExcept = {}
for k,v in nuevodicT.items():
    for k1,v1 in nuevoDicK.items():
        if("EXCEPT KEYWORDS" in v):
            dictExcept[k] = nuevoDicK
        else:
            dictExcept[k] = {}

        
'''
cont = 0
    print(len(value))
    print("EL VALUE",value)
    while(0 < len(value)-1):
        if(value[cont] == "{"):
            print(nuevodicT[key])
        cont+=1

'''
print("*"*100)
print("FINAL")
print("*"*100)
print("TOKENS QUE VAN AL AUTOMATA")
print(nuevodicT)
print("*"*100)
print("KEYWORDS PARA REVISAR EN EL EXCEPT")
print(nuevoDicK)
print("*"*100)
print("EXCEPT")
print(dictExcept)









#PASARLO A TU AUTOMATA
#LITO

