from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipes_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append(
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
            )
        cook_book[recipes_name] = ingredients
        file.readline()

pprint(cook_book, width=100) # sort_dicts=False


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for element in cook_book:
        for menu in dishes:
            if element == menu:
                for i in cook_book[element]:
                    i['quantity'] = int(i['quantity']) * person_count
                    if i['ingredient_name'] not in shop_list:
                        shop_list[i['ingredient_name']] = {'quantity': i['quantity'], 'measure': i['measure']}
                    else:
                        shop_list[i['ingredient_name']]['quantity'] += i['quantity']
    return shop_list


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


