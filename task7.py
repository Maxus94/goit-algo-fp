import random

numbers = {2 :0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

def simulate_dice_rolls(rolls_number):   

    for _ in range(0, rolls_number):
        first = random.randint(1, 6)    
        second = random.randint(1, 6)        
        numbers[first + second] += 1

    sum_prob = 0

    for number in range(2, 13):
        numbers[number] = numbers[number] / rolls_number
        sum_prob += numbers[number]
        print(number, numbers[number])
    print(sum_prob)
    return(numbers)

probabilities = simulate_dice_rolls(10000)   



