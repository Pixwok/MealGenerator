import json
import jmespath
import random
from time import *

def saison(month):
    if (month > 9 and month <=12) or (month >=1 and month < 4):
        return "hiver"
    else:
        return "été"

def listeCourse(platList):
    course = []
    fileCourse = open('liste-course.txt', 'w')
    for plat in platList:
        for ingredient in plat['ingredients']:
            if ingredient not in course:
                course.append(ingredient)
                fileCourse.write("\n" + ingredient)
    fileCourse.close()


def listePlat(platList):
    plats = jmespath.search("[].[name,ingredients]", platList)
    filePlat = open('repas.txt', 'w')
    for plat in plats:
        filePlat.write("\n" + plat[0])
        for ingredient in plat[1]:
            filePlat.write("\n\t" + ingredient)
    filePlat.close()


## Demande nombre de plat
nbrPlat = int(input("Combien de plat voulez vous générer : "))
mode = input("Voulez vous des plats de saison Y/N : ")

# Chargement fichier JSON
meals = open("meals.json", 'r', encoding='utf-8')
data = json.load(meals)

## Mode saison
if mode.upper() == "Y":
    saison = saison(int(strftime("%m", localtime())))
    platSaison = jmespath.search("[?(season == 'all' || season == '"+ saison +"')]", data['meals'])
    platList = random.sample(platSaison, k=nbrPlat) ## Tirage sans remise
else:
    platList = random.sample(data['meals'], k=nbrPlat) ## Tirage sans remise


listePlat(platList)
listeCourse(platList)

