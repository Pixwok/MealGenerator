import jmespath
from time import *
from Meals import *

Food = Meals()

def getSaison(month):
    if (month > 9 and month <=12) or (month >=1 and month < 4):
        return "hiver"
    else:
        return "été"

## Génération de la liste de course
def listeCourse(platList):
    course = []
    fileCourse = open('liste-course.txt', 'w')
    for plat in platList:
        for ingredient in plat['ingredients']:
            if ingredient not in course:
                course.append(ingredient)
                fileCourse.write("\n" + ingredient)
    fileCourse.close()

## Génération de la liste de repas
def listeRepas(platList):
    plats = jmespath.search("[].[name,ingredients]", platList)
    filePlat = open('repas.txt', 'w')
    for plat in plats:
        filePlat.write("\n" + plat[0])
        for ingredient in plat[1]:
            filePlat.write("\n\t" + ingredient)
    filePlat.close()

def modeSaison():
    # Recup saison
    mode = input("Voulez vous des plats de saison Y/N : ")
    # Mode saison
    if mode.upper() == "Y":
        return getSaison(int(strftime("%m", localtime()))) 
    else:
        return ""

while (True):
    print("=====MealGenerator=====")
    print("\r1.Générer des repas")
    print("\r2.Lister les repas")
    print("\r3.Lister repas à partir d'un ingrédient")
    print("\r9.Exit")
    choisse = int(input("Tapper le numéro de l'action: "))
    
    match choisse:
        case 1:
            nbrPlat = int(input("Combien de plat voulez vous générer : "))
            saison = modeSaison()
            listeRepas(Food.GenerateMeals(nbrPlat, saison))
            listeCourse(Food.GenerateMeals(nbrPlat, saison))
        case 2:
            saison = modeSaison()
            print(Food.getAll(saison))
        case 3:
            ingredient = input("Choisir un ingrédient: ")
            print(Food.getByIngredient(ingredient))
        case 9:
            break
        case _:
            nbrPlat = int(input("Combien de plat voulez vous générer : "))
            saison = modeSaison()
            listeRepas(Food.GenerateMeals(nbrPlat, saison))
            listeCourse(Food.GenerateMeals(nbrPlat, saison))