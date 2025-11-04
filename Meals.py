import json
import jmespath
import random

class Meals:
    def __init__(self):
        meals = open("meals.json", 'r', encoding='utf-8')
        self.data = json.load(meals)
    ## Liste des plats
    def getAll(self, saison = ""):
        if saison != "":
            platSaison = jmespath.search("[?(season == 'all' || season == '"+ saison +"')].name", self.data['meals'])
        else:
            platSaison = jmespath.search("[].name", self.data['meals'])
        return platSaison

    ## Récupère les plats qui contiennent l'ingrédient passé
    def getByIngredient(self, ingredient):
        platList = []
        for plat in self.data['meals']:
            if ingredient in plat['ingredients']:
                platList.append(plat['name'])
        return platList
    
    ## Génére n plat
    def GenerateMeals(self, nbrPlat, saison = ""):
        if saison != "":
            platSaison = jmespath.search("[?(season == 'all' || season == '"+ saison +"')]", self.data['meals'])
            platList = random.sample(platSaison, k=nbrPlat) ## Tirage sans remise
        else:
            platList = random.sample(self.data['meals'], k=nbrPlat) ## Tirage sans remise
        return platList