import pandas as pd
df=pd.read_csv('ipl.csv')
print(df)
print(df.columns)
df1=df[['Batsman','Runs']]
print("Most Run Scorer :",df1.head(1))
print("Highest runs in one inning ")
print(df['Highest_score'].max())
high=df['Highest_score'].max()
print(df[['Batsman','Highest_score']][df['Highest_score'] == high])
maxx=df['Sixes'].max()
print(maxx)
print(df[['Batsman','Sixes']][df['Sixes']==maxx])
most_fours=df['Fours'].max()
print(df[['Batsman','Fours']][df['Fours']==most_fours])
