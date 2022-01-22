from django.shortcuts import render
import random
import requests


def home(request):
    if request.POST:
        query = request.POST.get("query")
        url = f'https://api.edamam.com/api/recipes/v2?type=public&q={query}&app_id=25229fb0&app_key=7e3b95c0e3f703a04e4fbf26e1542d96'
        res = requests.get(url, headers={'Accept': 'application/json'})
        recipe_list = []
        for i in res.json()['hits']:
            recipe = {'name': i['recipe']['label'],
                      'image': i['recipe']['image'],
                      'source': i['recipe']['source'],
                      'url': i['recipe']['url'],
                      'caution': i['recipe']['cautions'],
                      'ingredients': i['recipe']["ingredientLines"],
                      'shareAs': i['recipe']['shareAs'],
                      'diet': i['recipe']['dietLabels'],
                      'meal': i['recipe']['mealType'],
                      'dish': i['recipe']['dishType'],
                      }
            # recipe = (i['recipe']['label'], i['recipe']['image'], i['recipe']['source'], i['recipe']['url'])
            recipe_list.append(recipe)
        return render(request, 'Food/index.html', {'recipe_list': recipe_list})
    else:
        sample_list = ['FryPan', 'cakes', 'Chicken', 'Mutton', 'Fish']
        url = f'https://api.edamam.com/api/recipes/v2?type=public&q={random.choice(sample_list)}&app_id=25229fb0&app_key=7e3b95c0e3f703a04e4fbf26e1542d96'
        res = requests.get(url, headers={'Accept': 'application/json'})
        recipe_list = []
        for i in res.json()['hits']:
            recipe = {'name': i['recipe']['label'],
                      'image': i['recipe']['image'],
                      'source': i['recipe']['source'],
                      'url': i['recipe']['url'],
                      'caution': i['recipe']['cautions'],
                      'ingredients': i['recipe']["ingredientLines"],
                      'shareAs': i['recipe']['shareAs'],
                      'diet': i['recipe']['dietLabels'],
                      'meal': i['recipe']['mealType'],
                      'dish': i['recipe']['dishType'],
                      }
            recipe_list.append(recipe)
        return render(request, 'Food/index.html', {'recipe_list': recipe_list})
