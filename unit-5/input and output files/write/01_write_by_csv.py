import pandas as pd
df=pd.DataFrame({
    'a':[9,8,7,8],
    'name':['manish','sahil','aryan','osheen'],
    "age":[24,32,12,25],
    "city":['new york',"america",'rajasthan','australia']
})
df.to_csv('kcc_python_programs/unit-5/input and output files/write/wite.csv',index=False)