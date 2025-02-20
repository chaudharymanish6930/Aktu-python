import pandas as pd
import numpy as np
df=pd.DataFrame({
    "a":[1,2,np.nan,4,5],
    "b":[np.nan,7,8,9,10],
    "c":[11,12,13,np.nan,15]
})
print(df)
missed_value=df.issna()
print(missed_value)