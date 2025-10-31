import json
import jmespath

meals = open("meals.json", 'r', encoding='utf-8')

data = json.load(meals)

platSaison = jmespath.search("[?(season == 'all' || season == 'été')].name", data['meals'])

print(platSaison)