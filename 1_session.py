category_a = [200, 220, 185, 250]
category_b = [150, 160, 170, 180]
category_c = [300, 310, 320, 330]

list_2 = [category_a,category_b,category_c]
for i in list_2:
    sum = 0
    for j in i:
        sum += j
    print(f'Sum of {i}={sum}') 


# Using dictionary 
categories = {
    "category_a": [200, 220, 185, 250],
    "category_b": [150, 160, 170, 180],
    "category_c": [300, 310, 320, 330]
}

for name, values in categories.items():
    total = sum(values)
    print(f'sum of {name} is {total}')

