import pandas as pd
import numpy as np


data = {
    'Имя': ['Аня', 'Борис', 'Вика'],
    'Возраст': [23, 35, 29],
    'Город': ['Москва', 'Казань', 'Сочи']
}

b = pd.DataFrame(data)

print(b)

data2 = {
    'город': ['Moscow', 'SBP', 'Minsk'],
    'Metro': ['yes', 'yes' , 'yes'],
    'KM': ['~449', '~124', '~40']
}
a = pd.DataFrame(data2)

print(a)