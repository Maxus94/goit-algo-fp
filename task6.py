
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

items = {
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
    "pepsi": {"cost": 10, "calories": 100},
    "hot-dog": {"cost": 30, "calories": 200},
    "hamburger": {"cost": 40, "calories": 250},
    "pizza": {"cost": 50, "calories": 300}  
}


# print(items["cola"])

# for item in items:
#     # print(item)
#     print(item, int(items[item]['calories']) / int(items[item]['cost']))
#     # print(item["calories"] / item["cost"])

def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    for item in items:
        if int(items[item]['cost']) <= remaining_budget:
            remaining_budget = remaining_budget - int(items[item]['cost'])
            total_calories = total_calories + int(items[item]['calories'])
            chosen_items.append(item)
    return total_calories, budget - remaining_budget, chosen_items

def dynamic_programming(items, budget):
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    chosen_items = []
    temp_budget = budget

    return dp_table[len(items)][budget], budget - temp_budget, chosen_items

print(greedy_algorithm(items, 100))