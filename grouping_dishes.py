def groupingDishes(dishes):
    dishes_dict = {}
    for dish in dishes:
        for ingredient in dish[1:]:
            if ingredient in dishes_dict:
                dishes_dict[ingredient].append(dish[0])
            else:
                dishes_dict[ingredient] = [dish[0]]


    output = []
    for i in sorted(dishes_dict):
        if len(dishes_dict[i]) > 1:
            y = [i] + sorted(dishes_dict[i])
            output.append(y)
    return output




dishes = [
            ["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]
        ]
print(groupingDishes(dishes))
#
#  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
#                             ["Salad", "Salad", "Sandwich"],
#                             ["Sauce", "Pizza", "Quesadilla", "Salad"],
#                             ["Tomato", "Pizza", "Salad", "Sandwich"]]
#
#
#
# dishes = [["Pasta", "Tomato Sauce", "Onions", "Garlic"],
#             ["Chicken Curry", "Chicken", "Curry Sauce"],
#             ["Fried Rice", "Rice", "Onions", "Nuts"],
#             ["Salad", "Spinach", "Nuts"],
#             ["Sandwich", "Cheese", "Bread"],
#             ["Quesadilla", "Chicken", "Cheese"]]
#
#  groupingDishes(dishes) = [["Cheese", "Quesadilla", "Sandwich"],
#                             ["Chicken", "Chicken Curry", "Quesadilla"],
#                             ["Nuts", "Fried Rice", "Salad"],
#                             ["Onions", "Fried Rice", "Pasta"]]
