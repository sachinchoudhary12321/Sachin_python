import pandas as pd
df=pd.DataFrame({"col1":range(10),"col2":["a","b","c","a","b","c","a","b","c","a"],"date":pd.to_datetime([
    "2025-06-22","2025-06-23"
]*5)})
print(df)

