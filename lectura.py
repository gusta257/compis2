import re
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

    for i in listaCheck:
        arrayOpIdent = []
        arrayOpStr = []
        arrayOpCHR = []
       # print("*"*50, i)
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


            if (afterIgual.find("+") != -1 or afterIgual.find("-") != -1):
                contPuntos = 0
                #print("EL CHARACTER TIENE DENTRO UN SIMBOLO DE MAS O MENOS")
                x = re.split("\+|\-",afterIgual)
                #print("Separadores de mas y menos",x)
                for xs in x:
                    if(xs.find("\"") != -1):
                        #print("ENTRO A IF 1")
                        arrayOpStr.append(xs)
                        
                    elif(xs.find("CHR") == 0 ):
                        #print("ENTRO A IF 2")
                        arrayOpCHR.append(xs)
                    else:
                        #print("ENTRO A ELSE")
                        arrayOpIdent.append(xs)
                #print("Array con strings",arrayOpStr)
                #print("Array con CHARS",arrayOpCHR)
                #arrayOpIdent = removePunto(arrayOpIdent)
                #print("Array con idents",arrayOpIdent)

            
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
                        pass
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
                #print("EL CHARACTER NO TIENE DENTRO UN SIMBOLO DE MAS O MENOS")
                #print("El AFTER",afterIgual)
                if (afterIgual.startswith("\"")):
                    #print("EL CHARACTER ES STRING")
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
                elif(afterIgual.find("CHR") != 1):
                    #print("EL CHARACTER ES CHAR")
                    numeroCHR = afterIgual.find("CHR(")
                    finCHR = afterIgual.find(")")
                    aferCHR = afterIgual[numeroCHR+4:finCHR]
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
                else:
                    #print("EL CHARACTER ES IDENT")
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
            afterIgual = afterIgual.replace(".", '')
            afterIgual = afterIgual.replace("\"", '')
            #keyArray.append(afterIgual)
    return todoB, idents
def checkKeyWords(listaCheck):
    
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
        

    return todoB,keyArray

file = open('cocol.txt', 'r')
compBool = False
charBool = False
keyBool = False
tokBool = False
characters = []
keywords = []
tokens = []
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
        characters.append(line)
        #print("Entre a char")
    elif(tokBool):
        if(line.endswith(".")):
            print("Si es valida")
        tokens.append(line)
       #print("Entre a tok")
    elif(keyBool):
        
        keywords.append(line)
        #print("Entre a key")
    else:
        pass



keywords = eliminarEspacio(keywords)
keywords = juntar(keywords)
characters = eliminarEspacio(characters)
tokens = eliminarEspacio(tokens)
#print(keywords)
#print(characters)
print(tokens)
print("-"*100)
'''
EL METODO PARA REVISAR KEYWORDS

validoK, kewordArray = checkKeyWords(keywords)
if(validoK):
    print("Todo bien Jose Luis")
    print(keywords)
else:
    print("Error")
print("*"*100)

EL METODO PARA REVISAR CHARACTERS

identsCharacter= []
validoC, identsCharacter = checkCharacters(characters)
if(validoC):
    print("Todo bien Jose Luis")
    print(characters)

else:
    print("Error")




#checkTokens

for i in tokens:
    i = i.replace(" ","")
    print(i)
    if(i != "TOKENS"):
        if "=" not in i:
            print("Error falta el signo igual en:",i)
            todoB = False
            break
        else:
            numIgual = i.find("=")
            beforeIgual = i[:numIgual]
            afterIgual = i[numIgual+1:]
            print(afterIgual)
            #corchetes = afterIgual.find("{")
            

            

    '''

            