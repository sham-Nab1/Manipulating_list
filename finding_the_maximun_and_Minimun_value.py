# Finding the Maximun and Minimun value

# Python List

flower_cost = [70, 80, 90, 100, 120]

def maxCustom(flower_cost):
    max_cost = 0
    for cost in flower_cost:
        if cost > max_cost:
            max_cost = cost
    return max_cost

# Built-in Function
print("The max is ", max(flower_cost))
print("The min is ", min(flower_cost))

# Custom Function
print(maxCustom(flower_cost))