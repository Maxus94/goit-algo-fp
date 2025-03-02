
items = {
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
    "pepsi": {"cost": 10, "calories": 100},
    "hot-dog": {"cost": 30, "calories": 200},
    "hamburger": {"cost": 40, "calories": 250},
    "pizza": {"cost": 50, "calories": 300}  
}

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
    item_names = list(items.keys())    
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]    
    
    for i in range(len(items) + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']
        item_calories = items[item_name]['calories']
        for b in range(budget + 1):                        
            if item_cost <= b:
                dp_table[i][b] = max(item_calories + dp_table[i - 1][b - item_cost], dp_table[i - 1][b])                
            else:
                dp_table[i][b] = dp_table[i - 1][b]                
    
    chosen_items = []    
    i = len(items)
    b = budget
    while i >= 0:
        if dp_table[i][b] != dp_table[i - 1][b]:            
            item_name = item_names[i - 1]
            item_cost = items[item_name]['cost']
            item_calories = items[item_name]['calories']
            chosen_items.append(item_name)                        
            b -= item_cost
        i -= 1
    return dp_table[len(items)][budget], budget - b, chosen_items

print("greedy_algorithm")
print(greedy_algorithm(items, 100))
print()
print("dynamic_programming")
print(dynamic_programming(items, 100))
