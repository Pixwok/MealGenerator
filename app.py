import json
import jmespath
import random
from time import *

## Demande nombre de plat
nbrPlat = int(input("Combien de plat voulez vous générer : "))
mode = input("Voulez vous des plats de saison Y/N : ")

def saison(month):
    if (month > 9 and month <=12) or (month >=1 and month < 4):
        return "hiver"
    else:
        return "été"

# Chargemetn fichier JSON
meals = open("meals.json", 'r', encoding='utf-8')
data = json.load(meals)

## Mode saison
if mode.upper() == "Y":
    saison = saison(int(strftime("%m", localtime())))
    platSaison = jmespath.search("[?(season == 'all' || season == '"+ saison +"')].name", data['meals'])
    platList = random.choices(platSaison, k=nbrPlat)
else:
    platSaison = jmespath.search("[].name", data['meals'])
    platList = random.choices(platSaison, k=nbrPlat)

print(platList)