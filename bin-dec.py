# Décimal vers binaire

## Itératif

def it_decimalToBinary(decimalNumber):
    binaryNumber = '' #on initialise 
    while (decimalNumber>0): #tant que le nombre n'est pas nul
        q = decimalNumber//2 #on calcul le quotient
        r = decimalNumber%2 #et le reste
        binaryNumber = str(r) + binaryNumber #on concatène le reste au début résultat
        decimalNumber = q #et on recommence avec le quotient
    return binaryNumber

## Récursif

def rec_decimalToBinary(decimalNumber):
    if (decimalNumber>0): #tant que le nombre n'est pas nul
        return str(rec_decimalToBinary(decimalNumber//2)) + str(decimalNumber%2) #on renvoie la concaténation de la traduction binaire du quotient de la division euclidienne par deux avec son reste (0 ou 1)
    else:
        return '' #cas de base: si le nombre est nul, on arrete la récursion

## Test
inputValue = 54372
outputValue = '1101010001100100'
print("Décimal (" + str(inputValue) + ") vers Binaire (" + outputValue + ") : ")
print("test itératif", it_decimalToBinary(inputValue))
print("test recursif", rec_decimalToBinary(inputValue))

# Binaire vers décimal

## Itératif


def it_binaryToDecimal(binaryNumber):
    """ 
    binaryNumber (input) is an string
    decimalNumber (output) is an integer
    """
    decimalNumber = 0 #on initialise le résultat à 0
    l = len(binaryNumber) - 1 #on défini, par commodité, la valeur l comme la différence entre le nombre de bit et 1
    for i in range(0,len(binaryNumber)): #on parcours les bits
        decimalNumber += int(binaryNumber[i])*(2**(l-i)) #pour chaque, on ajoute au résultat la puissance de deux égal au nombre de bit restant (indice - nombre de bit - 1) si le bit vaut 1
    return decimalNumber

## Récursif 


def rec_binaryToDecimal(binaryNumber):
    """ 
    binaryNumber (input) is an string
    decimalNumber (output) is an integer
    """
    if binaryNumber=="": #cas de base, si tout les bit on était parcouru
        return 0 #on retourne 0
    else: #sinon
        (t,q) = (int(binaryNumber[0]), binaryNumber[1:]) #on extrait le premier bit
        return t*(2**len(q)) + rec_binaryToDecimal(q)   #on le multiplie par la puissance de 2 égale au nombre de bit restant, à laquelle on ajoute la traduction décimal du nombre binaire restant à la queue.

## Test

inputValue = '1101010001100100'
outputValue = 54372
print("Binaire (" + inputValue + ") vers Décimal (" + str(outputValue) + ") : ")
print("test itératif", it_binaryToDecimal(inputValue))
print("test recursif", rec_binaryToDecimal(inputValue))