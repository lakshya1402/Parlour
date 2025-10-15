import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
df=pd.read_csv("parlour.csv")
x = df[['Haircut','Eyebrows','Facial','Makeup']]
y = df['Total price']
model = LinearRegression()
model.fit(x,y)
with open("parlour_model.pkl","wb") as f:
    pickle.dump(model,f)
print("Model created as parlour_model.pkl")
