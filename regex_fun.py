import pandas as pd
df=pd.DataFrame({"e_mail":['sachin','sachin@gmail.com','xyz@gmail.com'],
                 "number":['1234654','38452462k']})
x=df['e_mail'].str.match(r'^[a-zA-Z0-9@#$%^&*]+@[gmail.com]$')
print(x)
y=df['number'].str.match(r'^[0-9]\d{10}$')