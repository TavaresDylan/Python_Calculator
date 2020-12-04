# Définition de la class calculator
class Calculator:
    
    # Constructeur
    def __init__(self, base_nb = 0, result= 0):
        self.__base_nb = base_nb
        self.__result = result + base_nb
        
    # Fonction d'additon
    def add(self, nb):
        self.__result = self.__base_nb + nb
        return self.__result
        
    # Fonction de soustraction
    def substract(self, nb):
        self.__result = self.__base_nb - nb 
        return  self.__result
        
    # Fonction de multiplication
    def multiply(self, nb):
        self.__result = self.__base_nb * nb 
        return  self.__result
        
    # Fonction de division
    def divide(self, nb):
        self.__result = self.__base_nb / nb 
        return  self.__result
     
    # Fonction pour afficher le résultat du calcul
    def getResult(self):
        if self.__base_nb == 0:
            print("Error")
        else:
            print(self.__result)
    
    # Fonction de remise à zero de la calculatrice
    def reset(self):
        self.__result = 0
        return self.__result
    
    # Fonction de puissance
    def power(self, nb):
        self.__result = self.__base_nb * self.__base_nb 
        return  self.__result
    
    # Fonction qui revoie True si le nombre est un multiple sinon False
    def isMultipleOf(self, nb):
        if self.__base_nb % nb == 0:
            self.__result = True
            
        else:
            self.__result = False
            
    # Fonction qui renvoie True si le nombre d'entré est dans la liste sinon False
    def isInList(self, nb):
        if self.__base_nb in nb:
            self.__result = True
        else:
            self.__result = False
            
    # Fonction qui rend le quotien de la division et son reste 
    def getQuotientAndRemainderBy(self, nb):
        # récupération de l'int
        str_nb_int = str(int(self.__base_nb / nb))
        integer = int(self.__base_nb / nb)
        float_int = self.__base_nb / nb
        # récupération de la longeur de l'int
        int_len = len(str_nb_int)
        # récupération du reste
        remainder = str_integer[1:2]
        str_remainder = str(remainder)
        print("debugg remainder "+str_nb_int)
        self.__result = str("Quotien "+str_integer)+str(" reste "+str_remainder) 
        return  self.__result
        
        
# Revoie du nombre d'entré , lance une erreur si le nombre d'entré est 0
print("Revoie du nombre d'entré , lance une erreur si le nombre d'entré est 0")
my_calc = Calculator(6.4)
my_calc.getResult()
print("\n")

# Test d'une addition
print("Résultat de l'addition")
my_calc.add(6)
my_calc.getResult()
print("\n")

# Test d'une soustraction
print("Résultat de la soustraction")
my_calc.substract(2)
my_calc.getResult()
print("\n")

# Test d'une multiplication
print("Résultat de la multiplication")
my_calc.multiply(2)
my_calc.getResult()
print("\n")

# Test d'une multiplication
print("Résultat de la division")
my_calc.divide(2)
my_calc.getResult()
print("\n")

# Test d'une remise à zéro
print("Remise à zéro")
my_calc.reset()
my_calc.getResult()
print("\n")

# Définition d'une nouvelle entrée
print("Nouvelle entré")
my_calc = Calculator(10)
my_calc.getResult()
print("\n")

# Test d'une puissance
print("Résultat de la puissance")
my_calc.power(2)
my_calc.getResult()
print("\n")

# Test du multiple
print("Résultat du multiple")
my_calc.isMultipleOf(3)
my_calc.getResult()
print("\n")

# Test de la liste
print("Résultat de la liste")
my_calc.isInList([2,3,6,50, 10])
my_calc.getResult()
print("\n")

# Définition d'une nouvelle entrée
print("Nouvelle entré")
my_calc = Calculator(10)
my_calc.getResult()
print("\n")

# Test du Quotien et du reste
print("Résultat du quotien avec le reste")
my_calc.getQuotientAndRemainderBy(3)
my_calc.getResult()
print("\n")