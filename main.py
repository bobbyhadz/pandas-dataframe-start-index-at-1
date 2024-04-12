# How to Start the Index of a Pandas DataFrame at 1

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 1, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

print(df.index)

print('-' * 50)

df.index += 1

print(df.index)

print('-' * 50)

print(df)