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
            print(afterIgual)
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
print(keywords)
print(characters)
print(tokens)
'''
EL METODO PARA REVISAR KEYWORDS
valido, kewordArray = checkKeyWords(keywords)
if(valido):
    print("Todo bien Jose Luis")
    print(kewordArray)
else:
    print("Error")
print("*"*100)
'''
cont = 0
todoB = True
keyArray = []
idents = []
arrayOpIdent = []
arrayOp = []

for i in characters:
    print("-"*50)
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

            x = re.split("\+|\-",afterIgual)
            print("Separadores de mas y menos",x)
            for xs in x:
                if(xs.find("\"") == -1):
                    arrayOpIdent.append(xs)
                else:
                    arrayOp.append(xs)
            print("Array con strings",arrayOp)
            arrayOpIdent = removePunto(arrayOpIdent)
            print("Array con idents",arrayOpIdent)

            '''
            if (afterIgual.find("+") != -1):
                numOp = afterIgual.find("+")
                beforeOp = afterIgual[:numOp]
                afterOP = afterIgual[numOp+1:]
            else:
                numOp = afterIgual.find("-")
                beforeOp = afterIgual[:numOp]
                afterOP = afterIgual[numOp+1:]
            
            print("EL AFTER OP ES",afterOP)
            print("EL beforeOp OP ES",beforeOp)
            '''
            for ide in arrayOpIdent:
                if(ide in idents):
                    print("No problem ident")
                else:
                    print("No hay ident que haga match")


        else:

            if (afterIgual.find("\"") != -1):
                if(afterIgual.count("\"") % 2 == 0 ):
                    print("No problem", afterIgual)
                else:
                    print("FALTA UN \" WEY")
            else:
                afterIgual = afterIgual.replace(".", "")
                print("No tiene strings")
                if(afterIgual in idents):
                    print("No problem ident")
                else:
                    print("No hay ident que haga match")

       
        #print(numIgual)
        print(i)
        print("IDENT", beforeIgual)
        print("El AFTER",afterIgual)
        afterIgual = afterIgual.replace(".", '')
        afterIgual = afterIgual.replace("\"", '')
        #keyArray.append(afterIgual)




