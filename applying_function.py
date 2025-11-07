##This file to know about applying funtions 
import pandas as pd
import numpy as np

df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})


def sqr(x):
    return x*x

df_sqr = df.apply(sqr)
print(df_sqr)


df2 = pd.DataFrame({
   'price': [100, 200, 150, 300],
   'discount': [0.1, 0.2, 0.15, 0.05]
})

def discount(row):
    return row['price'] * (1 - row['discount'])

df2['discounted_final'] = df2.apply(discount,axis=1)

print(df2)

import pandas as pd

df3 = pd.DataFrame({
    'employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'salary': [60000, 80000, 75000, 50000],
    'bonus': [5000, 10000, 6000, 2000]
})

print(df3)

def total(df3):
    return df3['salary']+df3['bonus']

df3['total_sum'] = df3.apply(total,axis=1)
print(df3)

import pandas as pd

df4 = pd.DataFrame({
    'employee': ['Anna', 'Ben', 'Clara', 'Dan'],
    'salary': [65000, 85000, 70000, 76000]
})

def flag(df):
    if df['salary']>75000:
        print(f"The employee with greater salary is {df['employee']}")
    

df4.apply(flag,axis=1)


df5 = pd.DataFrame({
    'name': ['Manager', 'Engineer', 'Analyst', 'Clerk']
})

def count_letter(df):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in df['name']:
        if char in vowels:
            count += 1
    return count

print(df5.apply(count_letter,axis=1))


df6 = pd.DataFrame({
    'math': [78, 85, 90, 65],
    'science': [88, 92, 85, 70],
    'english': [80, 76, 90, 60]
})

def znorm(df):
    average = df.mean()
    standard = df.std()
    a = (df['math']-average)/standard
    b = (df['science']-average)/standard
    c = (df['english']-average)/standard
    print(a,b,c)
print(df6)
df6.apply(znorm,axis=1)



df7 = pd.DataFrame({
    'score1': [10, -5, 8, -2],
    'score2': [-1, 5, -3, 4]
})

print(df7)
def replace(row):
    return [0 if x<0 else x for x in row]

print(df7.apply(replace,axis=1))

