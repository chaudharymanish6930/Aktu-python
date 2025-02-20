import pandas as pd 
df=pd.DataFrame({
    'A':[2,4,3],
    "b":['a','b','c'],
    'C':[4.5,89.0,98.8]
})
print(df)
filtered_df=df[df["A"]>2]
print(filtered_df)

import pandas as pd
df=pd.DataFrame({
    "a":[1,2,3,4,5],
    "b":[6,7,8,9,10],
    "c":[11,12,13,14,15]
})
print(df)
print("______--------_______")
filtered_df=df[df["a"]>3]
# side by side indexing number in it.....
print(1,filtered_df)
filtered_df=df[df["a"]>1]
print(2,filtered_df)
filtered_df=df[df["a"]>2]
print(3,filtered_df)
filtered_df=df[df["a"]>3]
print(4,filtered_df)
filtered_df=df[df["a"]>4]
print(filtered_df)